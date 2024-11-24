######################################################LABORATORIO 2##############################################################
#-------------------------------------------------------Exercise 1. 
#   Using a button and 2 LEDs develop a system that can modify the LED status. The system should:
#   • State 1: Blink both LEDs alternating the sequence with 1 second intervals
#              (when LED 1 is turned on LED 2 is turned off).
#   • State 2: Both LEDs have to blink simultaneously with 2 seconds intervals.
#   • State 3: In this state both LEDS have to be turned ON indefinitely.
#   • State 4: This state turns off both LEDs
##################################################################################################################################


from gpiozero import LED, Button
import time

led1 = LED(12)  #=GPI 12
led2 = LED(16)  # PIO 16
button = Button(14, pull_up=True)  #GPIO 14up

state_led = 0

def increment_state():
    global state_led
    state_led += 1
    if state_led > 4:
        state_led = 0
    time.sleep(1)  

button.when_pressed = increment_state

#estaditos
def state_0():
    print("Estado 0: LED 1 parpadeando, LED 2 apagado")
    led1.on()  
    led2.off()  
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

switch = {
    0: state_0,
    1: state_1,
    2: state_2,
    3: state_3,
    4: state_4
}

while True:
   
    print(f"Ejecutando estado {state_led}")
    switch[state_led]()
