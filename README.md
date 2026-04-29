# 🔐 Cyber Lab Simulator
A cybersecurity simulator using Python to generate system logs, mimic brute-force attacks and raise the alarm based on rules.

# Objective
- Generates realistic system logs (login success/fail, file access)
- Simulates brute-force attacks from multiple IPs
- Detects suspicious behavior using pattern analysis
- Flags threats using severity levels (LOW / MEDIUM / HIGH)
- Outputs a security summary report


# Tech Stack
- Python

# How It Works
1. Log generator creates fake system activity
2. Attack simulator mimics brute-force attempts
3. Detection engine analyzes logs
4. System outputs security alerts + summary report

# Example Output
text
- LOW ALERT: Suspicious activity from 192.168.1.10 (3 fails)
- MEDIUM ALERT: Possible brute force from 10.0.0.5 (5 fails)
- HIGH ALERT: ACTIVE ATTACK DETECTED from 172.16.0.2 (7 fails)

# Purpose
Built to demonstrate foundational skills in:
- SOC analysis thinking
- Log parsing
- Threat detection logic
- Basic cybersecurity automation

# Author
Built by Mirianta — aspiring cybersecurity analyst

# Sample Detection Output
- text
HIGH ALERT: ACTIVE ATTACK DETECTED from 192.168.1.10

# Purpose
Built to demonstrate foundational SOC analyst and threat detection skills.
