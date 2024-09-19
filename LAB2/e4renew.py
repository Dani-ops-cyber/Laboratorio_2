from gpiozero import OutputDevice, InputDevice
import time


led1 = OutputDevice(12)  
led2 = OutputDevice(16)  
led3 = OutputDevice(20)   
led4 = OutputDevice(21)  

# Pull-up 
button1 = InputDevice(14, pull_up=True)  
button2 = InputDevice(15, pull_up=True)  

leds = [led1, led2, led3, led4]
sleep_times = [1, 1, 1, 1]  
current_led = 0 

def apagar_leds():
    
    for led in leds:
        led.off()

def encender_led():
    
    leds[current_led].on()
    print(f"LED {current_led + 1} encendido por {sleep_times[current_led]} segundos.")
    time.sleep(sleep_times[current_led])
    leds[current_led].off()
    print(f"LED {current_led + 1} apagado.")

def cambiar_led():
    
    global current_led
    apagar_leds()
    current_led = (current_led + 1) % len(leds)
    sleep_times[current_led] = 1  # Reiniciar el tiempo a 1 segundo
    print(f"Cambiado al LED {current_led + 1} con tiempo reiniciado a 1 segundo.")

def incrementar_tiempo():
    
    sleep_times[current_led] += 1
    print(f"Tiempo de encendido del LED {current_led + 1} incrementado a {sleep_times[current_led]} segundos.")

def esperar_soltura_boton(button):
    
    while not button.is_active:
        time.sleep(0.1)

def main_loop():
    
    while True:
        
        if not button1.is_active:
            encender_led()
            esperar_soltura_boton(button1)
            cambiar_led()
        
        
        if not button2.is_active:
            incrementar_tiempo()
            esperar_soltura_boton(button2)

        time.sleep(0.1) 
# Iniciar el programa
if __name__ == "__main__":
    main_loop()

