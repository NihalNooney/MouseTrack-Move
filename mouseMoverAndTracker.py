import pyautogui
import time

def move_mouse():
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y + 1)
        time.sleep(0.1) 
        pyautogui.moveTo(x, y)
        
        time.sleep(10)

if __name__ == "__main__":
    try:
        print("Press Ctrl+C to stop the program")
        move_mouse()
    except KeyboardInterrupt:
        print("\nProgram stopped")
