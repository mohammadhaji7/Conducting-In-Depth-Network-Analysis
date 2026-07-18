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