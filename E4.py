from gpiozero import LED
from time import sleep

# Definir el pin físico 12 como LED
led = LED(18)  # GPIO 18 corresponde al pin físico 12

# Encender el LED
led.on()
print("LED encendido")

# Mantener el LED encendido durante 5 segundos
sleep(5)

# Apagar el LED
led.off()
print("LED apagado")
