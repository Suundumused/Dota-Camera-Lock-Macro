from threading import Thread
from pynput.keyboard import Listener
from time import sleep
from win32api import mouse_event, SetCursorPos, GetSystemMetrics
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP


class CameraLockMacro(object):
    def __init__(self) -> None:
        self.x = int(0.32 * GetSystemMetrics(0))
        self.y = int(0.93 * GetSystemMetrics(1))
        #self.favorite_key = keyboard.Key.f1
        self.favorite_key = "b"
        self.executing = False
        self.sleep_a = 0.126
        self.sleep_b = 0.24

        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
    
    def left_click(self) -> None:
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        sleep(self.sleep_a)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
    
    def move_mouse(self) -> None:
        self.executing = True
        while self.executing:
            SetCursorPos((self.x, self.y))
            
    
    def on_press(self, key) -> None:
        try:
            if key.char == self.favorite_key:
                Thread(target=self.move_mouse).start()
                sleep(self.sleep_a)
                self.left_click()
                sleep(self.sleep_b)
                self.left_click()
                self.executing = False
                
        except AttributeError:
            pass        
        
       
if __name__ == "__main__":
    CameraLockMacro()
    
