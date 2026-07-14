# Wireless Network Architecture Review

## Objective

To analyze the wireless network architecture of a financial services organization and identify potential security risks associated with Wi-Fi and Bluetooth communications.

---

## Lab Environment

- Host OS: Windows 11 Home
- Virtualization: Oracle VirtualBox
- Guest OS: Kali Linux 2026.2
- Tools:
  - Wireshark
  - Aircrack-ng
  - Snort
  - Suricata
  - Bluetooth Utilities
  - Git
  - GitHub

---

## Proposed Enterprise Architecture

The organization uses separate wireless networks for employees and guests.

Critical financial systems are isolated from wireless users through VLAN segmentation and firewall policies.

Wireless communications are protected using WPA3-Enterprise wherever possible.

Remote users connect through a VPN gateway before accessing internal resources.

Bluetooth-enabled corporate devices use secure pairing mechanisms and restricted access policies.

---

## Trust Zones

| Zone | Trust Level |
|------|-------------|
| Internet | Untrusted |
| Corporate Firewall | Security Boundary |
| VPN Gateway | Trusted Entry |
| Employee Wi-Fi | Trusted |
| Guest Wi-Fi | Semi-Trusted |
| Bluetooth Devices | Limited Trust |
| Finance Servers | Highly Trusted |

---

## Initial Attack Surface

- Rogue Access Points
- Evil Twin Attacks
- Weak Wi-Fi Authentication
- Bluetooth Device Spoofing
- Unauthorized Pairing
- VPN Credential Theft
- Guest Wi-Fi Abuse
- Wireless Eavesdropping

---

## Initial Observation

The proposed architecture separates critical financial assets from public wireless networks while enforcing layered security controls.

Further assessment will evaluate encryption mechanisms, authentication, VPN protection, intrusion detection, and network segmentation.