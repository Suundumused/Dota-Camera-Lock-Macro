from pynput.keyboard import Listener
from time import sleep
from win32api import mouse_event, GetSystemMetrics, keybd_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, KEYEVENTF_KEYUP, VK_F1

import gc
gc.disable()


class CameraLockMacro(object):
    def __init__(self) -> None:
        self.win_size = (GetSystemMetrics(0), GetSystemMetrics(1))
        self.x = int(0.32 * self.win_size[0])
        self.y = int(0.93 * self.win_size[1])
        self.middle_x = int(0.5 * self.win_size[0])
        self.middle_y = int(0.5 * self.win_size[1])
        #self.favorite_key = keyboard.Key.f1
        self.favorite_key = "b"
        self.target_key = VK_F1
        self.executing = False
        self.sleep = 0.0625 #ms
        self.rate = 0.00138888889 #720Hz

        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
    
    def left_click(self) -> None:
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        sleep(self.sleep)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
    
    def press_release_key(self) -> None:
        if not self.executing:
            keybd_event(self.target_key, 0, 0, 0)
            self.executing = True
        else:
            keybd_event(self.target_key, 0, KEYEVENTF_KEYUP, 0)
            self.executing = False
            

    def on_press(self, key) -> None:
        try:
            if key.char == self.favorite_key:
                self.press_release_key()
                
        except AttributeError:
            pass        
        
       
if __name__ == "__main__":
    CameraLockMacro()
    
