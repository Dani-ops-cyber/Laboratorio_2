##                                                                                EJERCICIO 1.
# #########################################################################################################################################################################  
# Exercise 1. Using a button and 2 LEDs develop a system that can modify the
#               LED status. The system should:
#• State 1: Blink both LEDs alternating the sequence with 1 second intervals (when LED 1 is turned on LED 2 is turned off).
#• State 2: Both LEDs have to blink simultaneously with 2 seconds intervals.
#• State 3: In this state both LEDS have to be turned ON indefinitely.
#• State 4: This state turns off both LEDs.
from gpiozero import LED, Button
from time import sleep
from signal import pause

# Configura los LEDs y el botón
led1 = LED(18)  # Pin GPIO 18 (pin físico 12)
led2 = LED(15)  # Pin GPIO 15 (pin físico 10)
button = Button(23)  # Pin GPIO 23 (pin físico 16)

# Estado inicial
estado = 1

# Función para cambiar el estado cuando se presiona el botón
def cambiar_estado():
    global estado
    estado = (estado % 4) + 1  # Cambia el estado de 1 a 4 en ciclos

# Asocia la función cambiar_estado al botón
button.when_pressed = cambiar_estado

# Bucle principal
while True:
    if estado == 1:
        # Estado 1: Parpadear alternando la secuencia con intervalos de 1 segundo
        led1.on()
        led2.off()
        sleep(1)
        led1.off()
        led2.on()
        sleep(1)
    elif estado == 2:
        # Estado 2: Parpadear simultáneamente con intervalos de 2 segundos
        led1.on()
        led2.on()
        sleep(2)
        led1.off()
        led2.off()
        sleep(2)
    elif estado == 3:
        # Estado 3: Ambos LEDs encendidos indefinidamente
        led1.on()
        led2.on()
    elif estado == 4:
        # Estado 4: Apagar ambos LEDs
        led1.off()
        led2.off()

    # Pequeña pausa para evitar consumir demasiados recursos
    sleep(0.1)

# Mantén el script corriendo
pause()
