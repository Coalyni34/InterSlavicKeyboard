from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import logging

class controllerKeyboard:
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

    def __init__(self, prefiks):
        self.listener = None
        self.listener_thread = None
        self.stop_event = threading.Event()
        
        self.buffer = []  
        self.kbd = Controller() 
        self.prefix_key = prefiks
        self.logger = logging.getLogger('KeyboardController')
        self.logger.setLevel(logging.INFO)
        
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(ch)
        self.logger.info("Controller initialized with prefix: %s", prefiks)
    
    def start(self):
        if self.listener and self.listener.running:
            self.logger.info("Listener already running")
            return
            
        self.stop_event.clear()
        try:
            self.listener = keyboard.Listener(
                on_press=self.on_press,
                suppress=False  
            )
            self.listener_thread = threading.Thread(target=self.listener.start)
            self.listener_thread.daemon = True
            self.listener_thread.start()
            self.logger.info("Listener started successfully")
            return True
        except Exception as e:
            self.logger.error("Failed to start listener: %s", str(e))
            return False

    def stop(self):
        if self.listener is None:
            self.logger.warning("Stop called but listener is None")
            return
            
        try:
            if self.listener.running:
                self.listener.stop()
                self.listener_thread.join(timeout=1.0)
                self.logger.info("Listener stopped successfully")
            else:
                self.logger.warning("Stop called but listener not running")
        except Exception as e:
            self.logger.error("Error stopping listener: %s", str(e))
        finally:
            self.listener = None
            self.stop_event.set()
            self.buffer = []

    def on_press(self, key):
        if self.stop_event.is_set():
            return
            
        try:
            if hasattr(key, 'char') and key.char:
                char = key.char
                self.buffer.append(char)
                self.logger.debug("Key pressed: %s, Buffer: %s", char, ''.join(self.buffer))
                
                if char == self.prefix_key and len(self.buffer) >= 2:
                    self.replace_previous_char()
                elif key == Key.space:
                    self.buffer.clear()
        except Exception as e:
            self.logger.error("Error in on_press: %s", str(e))

    def replace_previous_char(self):
        if len(self.buffer) < 2:
            return
            
        prev_char = self.buffer[-2]
        self.logger.debug("Attempting replacement for: %s", prev_char)

        if prev_char in self.symbols:
            new_symbol = self.symbols[prev_char]
            self.logger.info("Replacing '%s' with '%s'", prev_char, new_symbol)

            for _ in range(2):
                self.kbd.tap(Key.backspace)

            self.kbd.type(new_symbol)                
            self.buffer = self.buffer[:-2]  
            self.buffer.append(new_symbol) 
        else:
            self.logger.debug("No replacement found for '%s'", prev_char)
            self.buffer.pop() 