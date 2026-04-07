import webbrowser, datetime, os
from utils.speak import speak
from commands.system_automation import system_control

def handle_command(command):

    if system_control(command):
        return "Executing system command"

    if "time" in command:
        t = datetime.datetime.now().strftime("%H:%M")
        speak(t)
        return t

    elif "google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "search" in command:
        q = command.replace("search", "")
        webbrowser.open(f"https://google.com/search?q={q}")
        return f"Searching {q}"

    elif "chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"

    return "Command not found"
