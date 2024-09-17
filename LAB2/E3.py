from gpiozero import LED, OutputDevice, InputDevice
import time


class DHT11():
   MAX_DELAY_COUNT = 100
   BIT_1_DELAY_COUNT = 10
   BITS_LEN = 40

   def __init__(self, pin, pull_up=False):
      # Conectar el pin de datos del DHT11 al GPIO especificado
      self._pin = pin
      self._pull_up = pull_up

   def read_data(self):
      bit_count = 0
      delay_count = 0
      bits = ""

      # -------------- send start signal --------------
      gpio = OutputDevice(self._pin)
      gpio.off()
      time.sleep(0.02)  # Señal de inicio para el DHT11: 20 ms

      gpio.close()
      gpio = InputDevice(self._pin, pull_up=self._pull_up)

      # -------------- wait for response --------------
      while gpio.value == 1:
            pass

      # -------------- read data --------------
      while bit_count < self.BITS_LEN:
            while gpio.value == 0:
               pass

            while gpio.value == 1:
               delay_count += 1
               if delay_count > self.MAX_DELAY_COUNT:
                  break
            if delay_count > self.BIT_1_DELAY_COUNT:
               bits += "1"
            else:
               bits += "0"

            delay_count = 0
            bit_count += 1

      # -------------- verify data and extract temperature and humidity --------------
      humidity = int(bits[0:8], 2)  # La humedad es un número entero en el DHT11
      temperature = int(bits[16:24], 2)  # La temperatura es un número entero en el DHT11
      check_sum = int(bits[32:40], 2)

      _sum = (int(bits[0:8], 2) + int(bits[8:16], 2) +
              int(bits[16:24], 2) + int(bits[24:32], 2)) & 0xFF

      if check_sum != _sum:
            humidity = 0
            temperature = 0

      return humidity, temperature


if __name__ == '__main__':
   
   led_heater = LED(18)  
   led_fan = LED(23)  
   dht11 = DHT11(17)

   try:
      while True:
         humidity, temperature = dht11.read_data()
         print(f"{time.time():.3f}  temperature: {temperature}°C  humidity: {humidity}%")

         # Control de LEDs basado en la temperatura
         if temperature < 12:
            led_heater.on()
         else:
            led_heater.off()

         if temperature > 20:
            led_fan.on()
         else:
            led_fan.off()

         time.sleep(2)

   except KeyboardInterrupt:
      print("Programa finalizado.")
   finally:
      led_heater.off()
      led_fan.off()

