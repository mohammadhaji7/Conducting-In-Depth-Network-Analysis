import socket
from cryptography.fernet import Fernet

# ===============================
# Load Encryption Key
# ===============================
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# ===============================
# Server Details
# ===============================
SERVER_IP = "192.168.0.15"
PORT = 5000

print("=" * 60)
print("        Secure Communication Client")
print("=" * 60)

message = input("Enter Secure Message: ")

encrypted_message = cipher.encrypt(message.encode())

print("\nEncrypting message...")
print("Encryption successful.")

print(f"\nConnecting to {SERVER_IP}:{PORT}...")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

client.send(encrypted_message)

print("\nEncrypted message sent successfully!")

client.close()

print("\nConnection closed.")
print("=" * 60)