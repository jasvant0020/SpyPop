from cryptography.fernet import Fernet

# Step 1: Get secret message from user
message = input("🔐 Enter your secret message: ").encode()

# Step 2: Generate and save encryption key
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Step 3: Encrypt the message
cipher = Fernet(key)
encrypted_message = cipher.encrypt(message)

# Step 4: Save encrypted message to file
with open("secret.enc", "wb") as enc_file:
    enc_file.write(encrypted_message)

print("\n✅ Secret encrypted and saved to 'secret.enc' with key in 'secret.key'")
