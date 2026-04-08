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

    elif "click" in command:
        pyautogui.click()
        speak("Clicked")

    elif "right click" in command:
        pyautogui.rightClick()
        speak("Right clicked")

    elif "double click" in command:
        pyautogui.doubleClick()
        speak("Double clicked")

    elif "scroll up" in command:
        pyautogui.scroll(10)
        speak("Scrolled up")

    elif "scroll down" in command:
        pyautogui.scroll(-10)
        speak("Scrolled down")

    elif "type" in command:
        text = command.replace("type", "").strip()
        pyautogui.typewrite(text)
        speak(f"Typed {text}")

    elif "enter" in command:
        pyautogui.press("enter")
        speak("Pressed enter")

    elif "space" in command:
        pyautogui.press("space")
        speak("Pressed space")

    elif "backspace" in command:
        pyautogui.press("backspace")
        speak("Pressed backspace")

    elif "tab" in command:
        pyautogui.press("tab")
        speak("Pressed tab")

    else:
        return False

    return True
