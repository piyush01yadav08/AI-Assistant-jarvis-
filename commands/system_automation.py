import os, pyautogui, keyboard
from utils.speak import speak

def system_control(command):

    if "shutdown" in command:
        speak("Shutting down")
        os.system("shutdown /s /t 1")

    elif "restart" in command:
        speak("Restarting")
        os.system("shutdown /r /t 1")

    elif "screenshot" in command:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot taken")

    elif "volume up" in command:
        pyautogui.press("volumeup")

    elif "volume down" in command:
        pyautogui.press("volumedown")

    elif "copy" in command:
        keyboard.press_and_release("ctrl+c")

    elif "paste" in command:
        keyboard.press_and_release("ctrl+v")

    else:
        return False

    return True
