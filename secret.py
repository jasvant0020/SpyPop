import tkinter as tk
from cryptography.fernet import Fernet
import os
import sys
import tempfile

def decrypt_and_show():
    # Load encryption key and message
    with open("secret.key", "rb") as kf:
        key = kf.read()
    with open("secret.enc", "rb") as ef:
        encrypted = ef.read()

    fernet = Fernet(key)
    decrypted_msg = fernet.decrypt(encrypted).decode()

    # 🪟 Create popup window
    root = tk.Tk()
    root.title("💬 Secret Message")
    root.configure(bg="#2e2e2e")  # smooth dark background
    root.attributes("-topmost", True)
    root.resizable(False, False)

    # Dynamic sizing
    wrap_len = 500 if len(decrypted_msg) > 100 else 300
    font_size = 14 if len(decrypted_msg) < 100 else 12

    # 📜 Message display
    msg_label = tk.Label(
        root,
        text=decrypted_msg,
        font=("Segoe UI", font_size),
        fg="white",
        bg="#2e2e2e",
        wraplength=wrap_len,
        justify="center",
        padx=40,
        pady=15
    )
    msg_label.pack()

    # ⏳ Countdown with extra padding
    countdown = tk.Label(
        root,
        font=("Segoe UI", 24, "bold"),
        fg="#ff4d4d",
        bg="#2e2e2e",
        pady=20,   # 👈 extra padding for visual comfort
        padx=10
    )
    countdown.pack()

    def start_timer(seconds):
        def tick():
            nonlocal seconds
            if seconds > 0:
                countdown.config(text=f"⚠️Warning Self-destroy in {seconds} seconds...")
                seconds -= 1
                root.after(1000, tick)
            else:
                root.destroy()
                self_destruct()
        tick()

    start_timer(5)
    root.mainloop()

def self_destruct():
    files_to_delete = [
        "secret.enc", "secret.key", "secret.py", "secret.pyc", "secret.spec"
    ]
    for file in files_to_delete:
        if os.path.exists(file):
            try:
                os.remove(file)
            except:
                pass

    folders_to_delete = ["build", "dist", "__pycache__"]
    for folder in folders_to_delete:
        if os.path.exists(folder):
            try:
                os.system(f'rmdir /s /q "{folder}"')
            except:
                pass

    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
        bat_path = os.path.join(tempfile.gettempdir(), "killme.bat")

        with open(bat_path, "w") as bat_file:
            bat_file.write(f"""@echo off
timeout /t 2 >nul
del "{exe_path}" >nul
del "%~f0" >nul
""")
        os.startfile(bat_path)
    else:
        try:
            os.remove(__file__)
        except:
            pass

# 🚀 Entry point
if __name__ == "__main__":
    decrypt_and_show()
