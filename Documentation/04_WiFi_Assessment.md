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


# Environment Assessment

## Wireless Adapter Status

The Kali Linux virtual machine was inspected for wireless network interfaces using the following commands:

- iw dev
- iw list
- nmcli device wifi list

### Observation

No wireless interfaces were detected.

### Reason

The Kali Linux virtual machine is running inside Oracle VirtualBox using a virtual network adapter. VirtualBox does not expose the host's physical Wi-Fi adapter as a native wireless interface to the guest operating system.

### Impact

Live WPA2/WPA3 wireless packet analysis could not be performed directly inside the virtual machine.

### Recommendation

Use a compatible external USB wireless adapter supporting monitor mode and packet injection (e.g., Alfa AWUS036ACH or AWUS036NHA) for full wireless security assessments.