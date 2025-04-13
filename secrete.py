import os
import sys
from tkinter import Tk, Label
from cryptography.fernet import Fernet

# --- Try Decrypting ---
try:
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    with open("secret.enc", "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = cipher.decrypt(encrypted).decode()
    print("Decrypted successfully.")
except Exception as e:
    print("❌ ERROR:", e)
    input("Press Enter to exit...")
    exit()

# --- GUI Setup ---
root = Tk()
root.title("🕵️ Secret Message")
root.configure(bg="#1e1e1e")

# --- Calculate window size dynamically ---
chars_per_line = 50
line_height = 30
num_lines = (len(decrypted) // chars_per_line) + 2

window_width = 500
window_height = num_lines * line_height + 100

# --- Center window ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cord = int((screen_width / 2) - (window_width / 2))
y_cord = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cord}+{y_cord}")

# --- Show message ---
label = Label(
    root,
    text=decrypted,
    wraplength=window_width - 40,
    font=("Consolas", 14),
    padx=20,
    pady=10,
    bg="#1e1e1e",
    fg="#00FF88"
)
label.pack()

# --- Large countdown label ---
countdown_label = Label(
    root,
    text="",
    font=("Consolas", 16, "bold"),
    bg="#1e1e1e",
    fg="#FF4444"
)
countdown_label.pack(pady=10)

# --- Destroy files and script itself ---
def destroy_popup():
    root.destroy()
    try:
        # Deleting encrypted files
        os.remove("secret.enc")
        os.remove("secret.key")
        print("💥 Secret files destroyed.")
        
        # Deleting the script (self-destruct)
        script_path = sys.argv[0]  # Get the path of the running script
        os.remove(script_path)  # Deletes the running script file
        print(f"💥 Script {script_path} destroyed.")
        
    except Exception as e:
        print("Error deleting files:", e)
    print("💥 All evidence destroyed.")

def update_countdown(seconds):
    if seconds > 0:
        countdown_label.config(text=f"💣 Self-destructs in {seconds} seconds...")
        root.after(1000, update_countdown, seconds - 1)
    else:
        destroy_popup()

# --- Set your custom countdown time here ---
update_countdown(10)

root.mainloop()
