from gpiozero import OutputDevice, InputDevice
import time


led1 = OutputDevice(12)   
led2 = OutputDevice(16)   
led3 = OutputDevice(20)  
led4 = OutputDevice(21)  

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
    
    if not button1.is_active:  
        while not button1.is_active:
            
            leds[current_led].on()
            print(f"LED {current_led + 1} encendido por {sleep_times[current_led]} segundos.")
            time.sleep(sleep_times[current_led])
            leds[current_led].off()
            print(f"LED {current_led + 1} apagado por {sleep_times[current_led]} segundos.")
            time.sleep(sleep_times[current_led])
     
        change_led()

        
        while not button1.is_active:
            time.sleep(0.1)
    
    
    if not button2.is_active:
        sleep_times[current_led] += 1  
        print(f"Tiempo de sleep del LED {current_led + 1} incrementado a {sleep_times[current_led]} segundos.")
        
        
        while not button2.is_active:
            time.sleep(0.1)
    
    time.sleep(0.1)  
