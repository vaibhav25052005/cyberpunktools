"""
Quick IP Address Finder
Finds ALL IP addresses connected to your network
Simple and fast!
"""

import subprocess
import socket
import platform
from datetime import datetime

def get_local_ip():
    """Get your local IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "Unknown"

def ping_ip(ip, timeout=1):
    """Ping single IP, return True if active"""
    try:
        if platform.system() == "Windows":
            cmd = ["ping", "-n", "1", "-w", str(timeout * 1000), ip]
        else:
            cmd = ["ping", "-c", "1", "-W", str(timeout), ip]
        
        result = subprocess.run(cmd, capture_output=True, timeout=timeout + 1)
        return result.returncode == 0
    except:
        return False

def get_mac(ip):
    """Get MAC address for IP"""
    try:
        # Ping first to ensure in ARP table
        subprocess.run(["ping", "-n", "1", "-w", "100", ip], 
                      capture_output=True, timeout=2)
        
        # Get ARP table
        result = subprocess.check_output(["arp", "-a"], stderr=subprocess.STDOUT)
        output = result.decode('utf-8', errors='ignore')
        
        # Find IP in output
        import re
        pattern = rf'{re.escape(ip)}\s+([0-9a-fA-F-]{{17}})'
        match = re.search(pattern, output)
        
        if match:
            return match.group(1).replace('-', ':')
    except:
        pass
    
    return "Unknown"

def scan_network():
    """Scan entire network for all IPs"""
    print("="*70)
    print("🔍 FINDING ALL IP ADDRESSES ON YOUR NETWORK")
    print("="*70)
    print()
    
    # Get your IP
    your_ip = get_local_ip()
    network = '.'.join(your_ip.split('.')[:3])
    
    print(f"Your IP: {your_ip}")
    print(f"Network: {network}.0/24")
    print(f"Scanning: {network}.1 to {network}.254")
    print()
    print("⏳ Scanning... (this takes 30-60 seconds)")
    print()
    
    # Find active IPs
    active_ips = []
    
    for i in range(1, 255):
        ip = f"{network}.{i}"
        
        # Show progress
        if i % 25 == 0:
            print(f"  Scanned {i}/254 addresses...")
        
        if ping_ip(ip, timeout=1):
            mac = get_mac(ip)
            active_ips.append({
                'IP': ip,
                'MAC': mac,
                'Is You': ip == your_ip
            })
    
    # Display results
    print()
    print("="*70)
    print(f"✅ FOUND {len(active_ips)} DEVICES ON YOUR NETWORK")
    print("="*70)
    print()
    print(f"{'No.':<5} {'IP Address':<18} {'MAC Address':<20} {'Status':<10}")
    print("-"*70)
    
    for i, device in enumerate(active_ips, 1):
        marker = " ← THIS IS YOU" if device['Is You'] else ""
        print(f"{i:<5} {device['IP']:<18} {device['MAC']:<20} {'Online':<10}{marker}")
    
    print()
    print("="*70)
    print()
    
    # Summary
    print("📊 SUMMARY:")
    print(f"  Total devices found: {len(active_ips)}")
    print(f"  Your IP: {your_ip}")
    print(f"  Network: {network}.0/24")
    print()
    
    # List just IPs
    print("📝 ALL IP ADDRESSES:")
    print("-"*70)
    for i, device in enumerate(active_ips, 1):
        marker = " (You)" if device['Is You'] else ""
        print(f"  {i}. {device['IP']}{marker}")
    
    print()
    print("="*70)
    print("✅ Scan Complete!")
    print("="*70)

if __name__ == "__main__":
    scan_network()
