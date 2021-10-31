
import pyautogui
import pynput
import pyfiglet
from pynput.keyboard import Key, Listener

result = pyfiglet.figlet_format("Scrot remastered", font = "slant"  )
print(result)
print("Press TAB key to screenshot, this works when the terminal is minimized too!")
print("To exit press Delete key.")
def screenshot():
    while True:
        def show(key):
            
            if key == Key.tab:
                image = pyautogui.screenshot('Screenshot.png')
                print("Image saved as Screenshot.png")
            if key == Key.delete:
                print("Thank you for using SCROT remastered! Do star us on GitHub.")
                exit()
          
        # Collect all event until released
        with Listener(on_press = show) as listener:
            listener.join()

screenshot()


            


