import pyautogui
import keyboard
import os

def take_screenshot():
    filename = input("Enter the filename (without extension): ") + ".png"
    screenshot = pyautogui.screenshot()
    save_path = os.path.join(os.getcwd(), filename)
    screenshot.save(save_path)
    print(f"Screenshot saved as {save_path}")

print("Press 'S' to take a screenshot. Press 'Q' to quit.")

while True:
    if keyboard.is_pressed('s'):
        take_screenshot()
    elif keyboard.is_pressed('q'):
        print("Exiting program.")
        break
