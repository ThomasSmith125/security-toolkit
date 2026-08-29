# Port Scanner V.1

Simple TCP port scanner written in Python.

## ⚠️ Legal warning

This tool is intended strictly for educational purposes and authorized security testing.

Scanning a network, host, or system without explicit written permission from its owner is illegal in most jurisdictions. Unauthorized use can result in criminal prosecution.

**Only use this tool on:**
- Systems you own
- Local/private lab environments (e.g., your own VMs)
- Platforms explicitly designed for this purpose (TryHackMe, Hack The Box, OverTheWire, etc.)

The author assumes no responsibility for misuse of this tool. You are solely responsible for ensuring you have proper authorization before scanning any target.

## Usage
python port_scanner.py <target> -p <ports> [-t <timeout>]

## Examples
python port_scanner.py 127.0.0.1 -p 1-1024
python port_scanner.py 127.0.0.1 -p 80,443,8080 -t 1

## Arguments
- target: IP address or hostname to scan
- -p / --ports: port range (1-1024) or list (22,80,443)
- -t / --timeout: timeout in seconds per port (default: 1.0)

## Limitations (V1)
- Sequential scan only, no threading — can be slow on large ranges
- TCP connect scan only, no SYN/stealth scan
- No service version detection