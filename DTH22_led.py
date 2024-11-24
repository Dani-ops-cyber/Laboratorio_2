#############################################  LABORATORIO 2   #################################################
# Exercise 3. 
#  We have a greenhouse that needs to cultivate different types of
#  vegetables. After some studies the team determined that the optimal temperature
#  for a good crop goes from 12 to 20 °C. To improve the greenhouse the team
#  decided to develop a temperature control system with the following features:

#         • Turn on the heater if the temperature register is below 12 °C.
#         • Turn on the fan when the temperature goes above 20 °C.
#         • Turn off both devices if the temperature is optimal.
##################################################################################################################


from gpiozero import LED
import Adafruit_DHT
import time

# Configuramos los pines de los LEDs
led_1 = LED(18)  # Pin físico 12
led_2 = LED(23)  # Pin físico 16

# Configuramos el sensor DHT22
sensor = Adafruit_DHT.DHT22
pin_sensor = 4  # Pin físico 7 (GPIO 4)

def leer_temperatura():
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin_sensor)
    if temperatura is not None:
        return temperatura
    else:
        return None

try:
    while True:
        temperatura = leer_temperatura()

        if temperatura is not None:
            print(f'Temperatura: {temperatura:.1f}°C')

            # Control de los LEDs según la temperatura
            if temperatura > 19:
                led_1.on()
            else:
                led_1.off()

            if temperatura < 18:
                led_2.on()
            else:
                led_2.off()

        else:
            print('Error al leer la temperatura.')

        time.sleep(2)

except KeyboardInterrupt:
    print("Programa finalizado.")
finally:
    led_1.off()
    led_2.off()


