import pyautogui as pyg
import os
from time import sleep
import keyboard
# ИМПОРТЫ ФРЕЙМВОРКОВ

if not os.path.exists("C:/DermaAccept"):
    os.makedirs("C:/DermaAccept")   

os.system('cls & title DermaAccept')
sleep(1)
print('Successfully loaded!. Press "INSERT" on your keyboard.')
active = False
def find_and_click(button_image):
    if active:
        button_location = None
        while button_location is None:
            button_location = pyg.locateOnScreen(button_image, grayscale=True, confidence=0.8)
        button_x, button_y = pyg.center(button_location)
        sleep(0.5)
        print('[DEBUG]', 'button coords', button_x, button_y)
        pyg.click(button_x, button_y)
def toggle_activation():
    global active
    active = not active
    if active:
        pyg.alert(text='Enabled', title='★DermaAlert★', button='OK')
        print('Activated')
    else:
        pyg.alert(text='Disabled', title='★DermaAlert★', button='OK')
        print('Deactivated')
keyboard.add_hotkey('insert', toggle_activation)
while True:
    try:
        sleep(1)
        find_and_click(r"C:/DermaAccept/ready.png")
    except pyg.ImageNotFoundException:  
        pass
