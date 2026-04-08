import webbrowser, datetime, os, glob
from utils.speak import speak
from commands.system_automation import system_control

# Dictionary of common apps and their executable names
apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "wordpad": "wordpad.exe",
    "explorer": "explorer.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "edge": "msedge.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "outlook": "outlook.exe",
    "access": "msaccess.exe",
    "onenote": "onenote.exe",
    "skype": "skype.exe",
    "teams": "teams.exe",
    "zoom": "zoom.exe",
    "vlc": "vlc.exe",
    "spotify": "spotify.exe",
    "discord": "discord.exe",
    "steam": "steam.exe",
    "photoshop": "photoshop.exe",
    "vscode": "code.exe",
    "sublime": "sublime_text.exe",
    "notion": "notion.exe",
    "slack": "slack.exe",
    "whatsapp": "whatsapp.exe",
    "telegram": "telegram.exe",
    "firefox": "firefox.exe",
    "opera": "opera.exe",
    "brave": "brave.exe",
    "safari": "safari.exe",  # if installed
    "itunes": "itunes.exe",
    "quicktime": "quicktimeplayer.exe",
    "adobe reader": "acrord32.exe",
    "pdf reader": "acrord32.exe",
    "winrar": "winrar.exe",
    "7zip": "7z.exe",
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "settings": "start ms-settings:",
    "registry editor": "regedit.exe",
    "event viewer": "eventvwr.exe",
    "services": "services.msc",
    "device manager": "devmgmt.msc",
    "disk management": "diskmgmt.msc",
    "computer management": "compmgmt.msc",
    "system properties": "sysdm.cpl",
    "run": "start run",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "bash": "bash.exe",  # if wsl
}

# Add shortcuts from Desktop and Start Menu
shortcuts = {}
desktop_path = os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop')
start_menu_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

for folder in [desktop_path, start_menu_path]:
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.lnk'):
                    name = os.path.splitext(file)[0].lower()
                    path = os.path.join(root, file)
                    shortcuts[name] = f'"{path}"'  # Quote for paths with spaces

apps.update(shortcuts)

def handle_command(command):

    if system_control(command):
        return "Executing system command"

    if "time" in command:
        t = datetime.datetime.now().strftime("%H:%M")
        speak(t)
        return t

   

    elif "search" in command:
        q = command.replace("search", "")
        webbrowser.open(f"https://google.com/search?q={q}")
        return f"Searching {q}"

    elif "open" in command:
        app_input = command.replace("open", "").strip().lower()
        if app_input in apps:
            exe = apps[app_input]
            os.system(f"start {exe}")
        else:
            os.system(f"start {app_input}")
        speak(f"Opening {app_input}")
        return f"Opening {app_input}"

    elif "close" in command:
        app_input = command.replace("close", "").strip().lower()
        if app_input in apps:
            exe = apps[app_input]
            if exe.startswith('"') and exe.endswith('.lnk"'):
                speak("Cannot close shortcut")
                return "Cannot close shortcut"
            os.system(f"taskkill /f /im {exe}")
        else:
            os.system(f"taskkill /f /im {app_input}.exe")
        speak(f"Closing {app_input}")
        return f"Closing {app_input}"

    elif "chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"
    
    elif "google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    return "Command not found"
