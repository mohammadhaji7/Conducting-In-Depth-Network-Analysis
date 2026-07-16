# Wireshark Packet Analysis

## Objective

The objective of this practical exercise was to capture and analyze network traffic generated while accessing secure websites over the internet. The analysis focused on understanding DNS resolution, TCP connection establishment, TLS encryption, and ARP communication.

---

# Test Environment

Operating System:
- Kali Linux

Tool Used:
- Wireshark

Browser:
- Firefox

Websites Visited:
- https://google.com
- https://github.com
- https://openai.com

---

# Protocol Analysis

## DNS

Observation:

- DNS queries and responses were successfully captured.
- Multiple domain names were resolved including Google, GitHub and OpenAI.
- DNS traffic confirmed successful domain resolution before establishing connections.

---

## TCP

Observation:

- TCP three-way handshake was observed.
- SYN
- SYN-ACK
- ACK

Destination port 443 was identified for HTTPS communication.

---

## TLS

Observation:

- Client Hello and Server Hello packets were observed.
- TLS encrypted application traffic successfully.
- Website contents were not visible because the communication was encrypted.

---

## ARP

Observation:

- No ARP packets were observed during this capture.
- The system likely already had the gateway MAC address stored in its ARP cache before packet capture began.

---

# Security Assessment

The captured traffic demonstrated secure communication using HTTPS over TLS. DNS resolution, TCP connection establishment and encrypted application traffic were successfully observed. No plaintext web content was exposed during packet analysis.

---

# Conclusion

Wireshark successfully captured and analyzed network traffic generated during web browsing. The practical demonstrated how DNS, TCP and TLS work together to establish secure communication over the network.