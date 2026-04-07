import tkinter as tk
from threading import Thread
from datetime import datetime
from utils.speak import speak
from utils.listen import listen
from commands.basic_commands import handle_command

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS AI")
        self.root.geometry("700x700")
        self.root.configure(bg="#020617")

        self.is_running = False

        title = tk.Label(root, text="JARVIS", font=("Arial", 28, "bold"),
                         fg="#22d3ee", bg="#020617")
        title.pack(pady=10)

        self.clock = tk.Label(root, font=("Arial", 12), fg="white", bg="#020617")
        self.clock.pack()
        self.update_clock()

        self.chat_box = tk.Text(root, bg="#020617", fg="#e2e8f0",
                                font=("Consolas", 12), wrap=tk.WORD, bd=0)
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.status = tk.Label(root, text="Idle", fg="#94a3b8", bg="#020617")
        self.status.pack(pady=5)

        btn_frame = tk.Frame(root, bg="#020617")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start", command=self.start, bg="#22c55e", width=12).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Stop", command=self.stop, bg="#ef4444", width=12).grid(row=0, column=1, padx=10)

    def update_clock(self):
        self.clock.config(text=datetime.now().strftime("%H:%M:%S"))
        self.root.after(1000, self.update_clock)

    def log(self, msg):
        self.chat_box.insert(tk.END, msg + "\n")
        self.chat_box.see(tk.END)

    def start(self):
        if not self.is_running:
            self.is_running = True
            Thread(target=self.run).start()

    def stop(self):
        self.is_running = False
        self.status.config(text="Stopped")

    def run(self):
        speak("Advanced Jarvis with automation activated")
        self.log("Jarvis: Activated")

        while self.is_running:
            self.status.config(text="Listening...")
            cmd = listen()

            if cmd:
                self.log("You: " + cmd)

                if "exit" in cmd:
                    speak("Goodbye")
                    self.log("Jarvis: Goodbye")
                    self.is_running = False
                    break

                res = handle_command(cmd)
                if res:
                    self.log("Jarvis: " + res)

            self.status.config(text="Idle")

def start_app():
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()
