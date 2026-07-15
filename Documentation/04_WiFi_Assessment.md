# Wireless Network Vulnerability Assessment

## Objective

Assess the security posture of the enterprise wireless network and identify potential vulnerabilities affecting confidentiality, integrity, and availability.

---

## Scope

- Employee Wi-Fi
- Guest Wi-Fi
- Wireless Access Points
- VPN Access
- Bluetooth Devices

---

## Assessment Methodology

The assessment was performed using:

- Wireshark
- Aircrack-ng
- Kali Linux
- Snort
- Suricata

---

## Identified Threats

| Threat | Description | Severity |
|---------|-------------|----------|
| Rogue Access Point | Unauthorized AP impersonating corporate network | High |
| Evil Twin Attack | Fake AP used to steal credentials | High |
| Weak WPA2 Password | Susceptible to offline cracking | High |
| Wireless Packet Sniffing | Interception of unencrypted traffic | Medium |
| Guest Network Abuse | Unauthorized access attempts | Medium |
| VPN Credential Theft | Compromised remote user credentials | High |

---

## Initial Observation

The proposed enterprise architecture incorporates multiple security layers including firewall protection, VPN access, VLAN segmentation, WPA3-Enterprise, and IDS/IPS monitoring.

However, wireless environments remain susceptible to rogue access points, credential theft, Bluetooth attacks, and wireless eavesdropping if security controls are not continuously monitored.