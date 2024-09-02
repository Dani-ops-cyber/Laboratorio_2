from gpiozero import LED, Button
from signal import pause

# Configuración de los pines
led1 = LED(18)  # GPIO 18 corresponde al pin físico 12
led2 = LED(23)  # GPIO 23 corresponde al pin físico 16

button1 = Button(17)  # GPIO 17 corresponde al pin físico 11
button2 = Button(27)  # GPIO 27 corresponde al pin físico 13

# Funciones para encender y apagar los LEDs
def toggle_led1():
    if led1.is_lit:
        led1.off()
        print("LED 1 apagado")
    else:
        led1.on()
        print("LED 1 encendido")

def toggle_led2():
    if led2.is_lit:
        led2.off()
        print("LED 2 apagado")
    else:
        led2.on()
        print("LED 2 encendido")

# Asignar las funciones a los botones
button1.when_pressed = toggle_led1
button2.when_pressed = toggle_led2

# Mantener el programa en ejecución
pause()

