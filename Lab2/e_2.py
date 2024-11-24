##-----------------------------------------------------LABORATORIO 2-------------------------------------------------
# Exercise 2. Using 4 LEDs and 2 buttons make a binary counter with the values
#             from table 1. The counter should have the following features:
#                           • When button 1 is pushed, the binary counter increases 1 value.
#                           • When button 2 is pressed, the binary counter decreases 1 value.
#                           • Each led represent the binary values.
#                           • When the counter reaches the value 15 it should return to the first value
#                           • When the counter is 0 it shouldn´t keep reducing the value (should stay in 0 after the button press)

#########################################################################################################################################

from gpiozero import LED, Button
import time 

class BinaryCounter:
    def __init__(self):
        #led
        self.leds = [LED(12), LED(16), LED(20), LED(21)]
   
        self.button_increase = Button(14, pull_up=True)
        self.button_decrease = Button(15, pull_up=True)
        self.counter = 0  # Iniciar contador en 0

        self.button_increase.when_pressed = self.increment_counter
        self.button_decrease.when_pressed = self.decrement_counter

    def update_leds(self):
        """Actualiza los LEDs para representar el valor binario del contador."""
        for i in range(4):
            if self.counter & (1 << i):
                self.leds[i].on()
            else:
                self.leds[i].off()

    def increment_counter(self):
        """Incrementa el contador y actualiza los LEDs."""
        self.counter += 1
        if self.counter > 15:
            self.counter = 0
        self.update_leds()
        self.print_values()
        
    def decrement_counter(self):
        """Decrementa el contador y actualiza los LEDs."""
        self.counter -= 1
        if self.counter < 0:
            self.counter = 0
        self.update_leds()
        self.print_values()

    def print_values(self):
        """Imprime el valor del contador en formato hexadecimal, binario y decimal."""
        print(f"Decimal: {self.counter}, Hexadecimal: {hex(self.counter)}, Binario: {bin(self.counter)}")

    def run(self):
        """Método principal para mantener el programa en ejecución."""
        try:
            while True:
                time.sleep(0.1)  
        except KeyboardInterrupt:
           
            for led in self.leds:
                led.off()
            print("Programa terminado.")

if __name__ == "__main__":
    counter = BinaryCounter()
    counter.run()
