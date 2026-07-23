## End-to-End Encrypted Communication

### Objective

Demonstrate secure application-layer communication using symmetric encryption over a TCP connection.

### Technologies

- Python
- Socket Programming
- Cryptography (Fernet)
- Kali Linux
- Windows 11
- Wireshark

### Workflow

```
Windows Client
        │
        ▼
Encrypt Plaintext (Fernet)
        │
        ▼
TCP Port 5000
        │
        ▼
Kali Linux Server
        │
        ▼
Decrypt Ciphertext
        │
        ▼
Display Original Message
```

### Features

- Interactive client application
- Symmetric key encryption
- Secure TCP communication
- Automatic decryption
- Continuous server operation
- Network packet verification using Wireshark

### Validation

Wireshark captures confirmed that only encrypted Fernet ciphertext (`gAAAAAB...`) traversed the network. The original plaintext remained confidential throughout transmission and was only recovered by the server after successful decryption.
