####################################  LABORATORIO 2   ##############################################################
# Exercise 4. 
#  Generate a program that will turn on 1 of 4 possible LEDs. To
#  achieve this the system will have 2 buttons, the first one will select the LED to
#  turn on and the second one will increase 1 second to the time the LED is turned
#  on. When the first button is pressed the LED to activate will change to the next
#  one and the time to turn on will reset to 1 second.
from gpiozero import OutputDevice, InputDevice
import time

# Configuración de los pines de los LEDs
led1 = OutputDevice(12)  # LED 1 en el pin físico 12 
led2 = OutputDevice(16)  # LED 2 en el pin físico 16 
led3 = OutputDevice(20)  # LED 3 en el pin físico 22 
led4 = OutputDevice(21)  # LED 4 en el pin físico 24 

#pull-up
button1 = InputDevice(14, pull_up=True)  
button2 = InputDevice(15, pull_up=True)  

leds = [led1, led2, led3, led4]
sleep_times = [1, 1, 1, 1]  
current_led = 0

def change_led():
    global current_led
    
    for led in leds:
        led.off()
    current_led = (current_led + 1) % len(leds)


while True:
    #  botón 1
    if not button1.is_active:  #up
        while not button1.is_active:
            #
            leds[current_led].on()
            print(f"LED {current_led + 1} encendido por {sleep_times[current_led]} segundos.")
            time.sleep(sleep_times[current_led])
            leds[current_led].off()
            print(f"LED {current_led + 1} apagado por {sleep_times[current_led]} segundos.")
            time.sleep(sleep_times[current_led])
     
        change_led()

        # Esperar waiting
        while not button1.is_active:
            time.sleep(0.1)
    
    # botón 2
    if not button2.is_active:
        sleep_times[current_led] += 1  
        print(f"Tiempo de sleep del LED {current_led + 1} incrementado a {sleep_times[current_led]} segundos.")
        
        
        while not button2.is_active:
            time.sleep(0.1)
    
    time.sleep(0.1)  # pausitah
