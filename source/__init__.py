from threading import Thread
from pynput.keyboard import Listener
from time import sleep
from win32api import mouse_event, SetCursorPos, GetSystemMetrics
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP

import gc
gc.disable()


class CameraLockMacro(object):
    def __init__(self) -> None:
        self.x = int(0.32 * GetSystemMetrics(0))
        self.y = int(0.93 * GetSystemMetrics(1))
        #self.favorite_key = keyboard.Key.f1
        self.favorite_key = "b"
        self.executing = False
        self.sleep = 0.08

        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
    
    def left_click(self) -> None:
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        sleep(self.sleep)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
    
    def move_mouse(self) -> None:
        self.executing = True
        while self.executing:
            SetCursorPos((self.x, self.y))
            sleep(0.00277777778)
            
    
    def on_press(self, key) -> None:
        try:
            if key.char == self.favorite_key:
                process = Thread(target=self.move_mouse)
                process.daemon = True
                process.start()
                sleep(self.sleep)
                self.left_click()
                sleep(self.sleep)
                self.left_click()
                self.executing = False
                sleep(self.sleep)
                gc.collect()
                
        except AttributeError:
            pass        
        
       
if __name__ == "__main__":
    CameraLockMacro()
    
