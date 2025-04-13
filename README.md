# 🕵️‍♂️ SpyPop – Secret Message Popup with Self-Destruct

**SpyPop** is a sleek Python project that encrypts secret messages and reveals them in a dramatic spy-style popup window. After showing the message, the app self-destructs — wiping out all evidence, including itself. 💥

## 📁 Files

- `main.py` – Encrypts a secret message using `cryptography` and stores the result as `secret.enc` and `secret.key`.
- `secret.py` – Decrypts the message and displays it in a GUI popup. After a countdown, it auto-deletes:
  - The encrypted message
  - The encryption key
  - The decryption script itself (`secret.py` or `secret.exe`)

## 🚀 How to Use

### 1. first run main.py and give a secret message as input and it genrate files which are as secret.enc and secret.key.
### 2. send secret.enc + secret.key + secret.exe or you can send  secret.enc + secret.key + secret.py to your friend or any user 

## ⚠️ Warning

### Once secret.py or secret.exe runs, it deletes itself and all related files. Use with caution — this is not reversible.

## Demo

🎥 [Watch the video here](https://drive.google.com/file/d/1cGmY1VHm9Gq3FvolqnIUvA6NN2xUCJU7/view?usp=sharing)


```bash
git clone https://github.com/yourusername/spypop.git
cd spypop
