## 13 July 2026

### Completed
- Created project folder structure.
- Initialized Git repository.
- Created GitHub repository.
- Installed Snort.
- Installed Suricata.
- Verified Wireshark and Aircrack-ng.
- Performed initial Kali cleanup.

### Challenges
- Kali VM had only 397 MB free disk space.
- Recovered approximately 900 MB using apt autoremove and apt clean.

### Next Session
- Capture remaining setup screenshots.
- Verify Bluetooth.
- Continue disk cleanup if needed.
- Begin Wireless Network Architecture Review.

## 19 July 2026

## Snort IDS - Custom ICMP Detection

# objecive #
Configure Snort 3 to detect ICMP traffic using a custom rule.

**Activities Performed**
- Configured Kali VM with Bridged Networking.
- Verified network connectivity.
- Modified `snort.lua` to load `local.rules`.
- Created a custom ICMP detection rule.
- Validated the Snort configuration.
- Generated ICMP traffic from the Windows host.
- Observed successful IDS alerts.

**Evidence**
- 01_Network_Verification.png
- 02_Snort_Configuration_Validation.png
- 03_Custom_ICMP_Rule.png
- 04_Live_ICMP_Alert.png
- 05_Windows_Ping_Test.png

**Result**
Successfully detected ICMP echo request and reply traffic using a custom Snort rule.

**Lessons Learned**
An IDS detects and reports suspicious or defined traffic patterns but does not block them. Alert analysis requires validating the source, destination, protocol, timestamp, and determining whether the activity is expected or suspicious.
## Day X – Snort IDS Alert Logging

### Objective
Configure Snort IDS to detect ICMP traffic and log alerts for SIEM integration.

### Tasks Completed
- Enabled file logging using the alert_fast logger.
- Validated Snort configuration successfully.
- Started Snort in IDS mode on interface eth0.
- Generated ICMP traffic using ping.
- Verified custom ICMP detection rule execution.
- Confirmed alerts were written to /home/kali/alert_fast.txt.

### Evidence Collected
- Snort configuration screenshot
- Configuration validation screenshot
- Snort IDS running
- alert_fast.txt location
- ICMP alert logs
- Alert file verification

### Outcome
Snort is successfully generating alerts that are ready to be ingested into Splunk Enterprise through the Splunk Universal Forwarder.

## Day X – WireGuard VPN Server and Client Configuration

### Objectives
- Configure a secure WireGuard VPN between a Kali Linux server and a Windows 11 client.
- Verify encrypted communication over the VPN tunnel.

### Activities Completed
- Installed WireGuard and WireGuard tools on Kali Linux.
- Installed the official WireGuard client on Windows 11.
- Generated public/private key pairs for both server and client.
- Configured the WireGuard server (`wg0`) with a dedicated VPN subnet (`10.10.10.0/24`).
- Configured the Windows client and established a secure VPN tunnel.
- Added the Windows client as a trusted peer on the Kali server.
- Resolved an `AllowedIPs` configuration issue that initially prevented ICMP traffic.
- Successfully verified bidirectional communication using ICMP over the VPN.

### Results
- Secure WireGuard tunnel established.
- Successful handshake and encrypted data transfer observed.
- Windows client successfully reached the Kali VPN endpoint.
- Kali server successfully communicated with the Windows client over the VPN.

### Evidence
- WireGuard server configuration
- Windows WireGuard client
- Successful VPN handshake
- Successful ping tests
- VPN interface configuration