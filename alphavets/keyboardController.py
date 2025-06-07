from pynput import keyboard
from pynput.keyboard import Key, Controller

class controllerKeyboard(object):

    symbols = {
        'c': 'č',
        'e': 'ě',
        's': 'š', 
        'z': 'ž',
        'э': 'є',
        'й': 'j', 
        'л': 'љ',
        'н': 'њ'
    }
    

    def __init__(self, prefiks, isPrefiksActive, isAlwaysActive, isAutoStart, isProgramActive):
        self.listener = None
        self.buffer = []  
        self.kbd = Controller() 

        self.is_prefiks_active = isPrefiksActive
        self.is_always_active = isAlwaysActive
        self.is_auto_start = isAutoStart
        self.is_program_active = isProgramActive

        self.prefix_key = prefiks
    
    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.listener.join()
    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char:
                char = key.char
                self.buffer.append(char)
                if char == self.prefix_key and len(self.buffer) >= 2:
                    self.replace_previous_char()
                elif key == Key.space:
                    self.buffer.clear()
        except Exception as e:
            print(f"Ошибка: {e}")

    def replace_previous_char(self):
        if len(self.buffer) < 2:
            return            
        
        prev_char = self.buffer[-2]

        if prev_char in self.symbols:
            new_symbol = self.symbols[prev_char]

            for _ in range(2):
                self.kbd.tap(Key.backspace)

            self.kbd.type(new_symbol)                

            self.buffer.clear()
            

        

    

        
