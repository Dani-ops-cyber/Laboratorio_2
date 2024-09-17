from gpiozero import LED, Button
import time

led1 = LED(12)  # LED conectado al pin GPIO 12
led2 = LED(16)  # LED conectado al pin GPIO 16
button = Button(14, pull_up=True)  # Botón conectado al pin GPIO 14, con pull-up interno

state_led = 0

def increment_state():
    global state_led
    state_led += 1
    if state_led > 4:
        state_led = 0
    time.sleep(1)  # Pequeño retardo para evitar el rebote del botón

button.when_pressed = increment_state

# Definición de las funciones para cada estado
def state_0():
    print("Estado 0: LED 1 parpadeando, LED 2 apagado")
    led1.on()  # Encender led1
    led2.off()  # Apagar led2
    time.sleep(1)
    led1.off()
    led2.on()
    time.sleep(1)

def state_1():
    print("Estado 1: LED 1 encendido por 2 segundos, LED 2 apagado y luego alterna")
    led1.on()
    led2.off()
    time.sleep(2)
    led1.off()
    led2.on()
    time.sleep(2)

def state_2():
    print("Estado 2: Ambos LEDs parpadeando juntos")
    led1.on()
    led2.on()
    time.sleep(1)
    led1.off()
    led2.off()
    time.sleep(1)

def state_3():
    print("Estado 3: Ambos LEDs encendidos y apagados cada 2 segundos")
    led1.on()
    led2.on()
    time.sleep(2)
    led1.off()
    led2.off()
    time.sleep(2)

def state_4():
    print("Estado 4: Ambos LEDs apagados")
    led1.off()
    led2.off()

# Diccionario de funciones para simular un switch
switch = {
    0: state_0,
    1: state_1,
    2: state_2,
    3: state_3,
    4: state_4
}

while True:
    # Mostrar en el shell el estado actual y ejecutar la función correspondiente
    print(f"Ejecutando estado {state_led}")
    switch[state_led]()
