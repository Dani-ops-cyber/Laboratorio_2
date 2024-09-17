from gpiozero import LED, Button
import time

class BinaryCounter:
    def __init__(self):
        
        self.leds = [LED(12), LED(16), LED(20), LED(21)]
        self.button_increase = Button(14, pull_up=True)
        self.button_decrease = Button(15, pull_up=True)
        self.counter = 0  

        
        self.button_increase.when_pressed = self.increment_counter
        self.button_decrease.when_pressed = self.decrement_counter

    def update_leds(self):
        
        for i in range(4):
            if self.counter & (1 << i):
                self.leds[i].on()
            else:
                self.leds[i].off()

    def increment_counter(self):
        
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
       
        print(f"Decimal: {self.counter}, Hexadecimal: {hex(self.counter)}, Binario: {bin(self.counter)}")

    def run(self):
        
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
