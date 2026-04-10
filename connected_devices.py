import subprocess
import re
import platform
import socket
from datetime import datetime

class ConnectedDevicesScanner:
    """
    Scans and displays ONLY real devices connected to your network
    Filters out multicast, broadcast, and system addresses
    Shows devices like: phones, laptops, tablets, smart TVs, etc.
    """
    
    def __init__(self):
        self.devices = []
        
    def get_local_ip(self):
        """Get your local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception as e:
            return f"Error: {e}"
    
    def get_network_range(self):
        """Get your network subnet"""
        local_ip = self.get_local_ip()
        if local_ip.startswith("Error"):
            return None
        
        parts = local_ip.split('.')
        network_prefix = '.'.join(parts[:3])
        return network_prefix
    
    def is_real_device(self, ip, mac):
        """
        Filter out non-device addresses
        Returns True if it's likely a real device
        """
        # Filter out broadcast addresses
        if ip.endswith('.255') or ip == '255.255.255.255':
            return False
        
        # Filter out multicast addresses (224.0.0.0 - 239.255.255.255)
        if ip.startswith('224.') or ip.startswith('239.'):
            return False
        
        # Filter out loopback
        if ip.startswith('127.'):
            return False
        
        # Filter out multicast MAC addresses
        if mac.startswith('01:00:5e') or mac.startswith('01-00-5e'):
            return False
        
        # Filter out broadcast MAC
        if mac == 'ff:ff:ff:ff:ff:ff' or mac == 'FF-FF-FF-FF-FF-FF':
            return False
        
        return True
    
    def detect_device_type(self, ip, mac, hostname='Unknown'):
        """
        Try to detect what type of device it is
        Returns: device type string
        """
        mac_prefix = mac[:8].lower()
        
        # Common router IPs
        if ip.endswith('.1') or ip.endswith('.254'):
            return '🌐 Router/Gateway'
        
        # Known DNS servers
        if ip in ['8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1']:
            return '🔍 DNS Server'
        
        # Check MAC vendor prefixes (common manufacturers)
        apple_prefixes = ['00:1b:63', '00:1c:b3', '00:1d:4f', '00:23:6c', '00:25:00',
                         '00:26:08', '00:26:b0', '3c:07:54', '3c:15:c2', '40:6c:8f',
                         '44:d8:84', '4c:32:75', '50:ea:d6', '5c:59:48', '60:03:08',
                         '60:c5:47', '68:5b:35', '68:64:4b', '68:a8:6d', '68:ab:cd',
                         '70:cd:60', '74:e2:f5', '78:ca:39', '7c:11:be', '80:60:b7',
                         '84:38:35', '88:66:a5', '8c:85:90', '90:27:e4', '90:84:0d',
                         '98:01:a7', '98:5a:eb', '9c:3d:cf', 'a4:5e:60', 'ac:87:a3',
                         'b8:17:c2', 'b8:53:ac', 'bc:52:b7', 'c0:9f:42', 'c0:ce:cd',
                         'c8:2a:14', 'c8:69:cd', 'cc:29:f5', 'd0:25:98', 'd4:85:64',
                         'd8:a0:1d', 'dc:2b:61', 'e0:55:3d', 'e4:ce:8f', 'f0:18:98',
                         'f4:0f:24', 'f8:1e:df', 'fc:1f:c3']
        
        samsung_prefixes = ['00:12:47', '00:16:32', '00:18:af', '00:1c:62', '00:1e:7d',
                           '00:21:4c', '00:23:39', '00:24:54', '00:26:37', '00:27:1c']
        
        if any(mac_prefix.startswith(prefix) for prefix in apple_prefixes):
            return '🍎 Apple Device'
        
        if any(mac_prefix.startswith(prefix) for prefix in samsung_prefixes):
            return '📱 Samsung Device'
        
        # Try reverse DNS lookup for hostname clues
        if hostname != 'Unknown':
            hostname_lower = hostname.lower()
            if 'iphone' in hostname_lower or 'ipad' in hostname_lower:
                return '🍎 Apple Device'
            elif 'samsung' in hostname_lower or 'android' in hostname_lower:
                return '📱 Android Device'
            elif 'laptop' in hostname_lower or 'pc' in hostname_lower:
                return '💻 Computer'
            elif 'tv' in hostname_lower or 'smarttv' in hostname_lower:
                return '📺 Smart TV'
            elif 'printer' in hostname_lower:
                return '🖨️ Printer'
        
        # Default: assume it's a connected device
        return '📡 Connected Device'
    
    def get_hostname(self, ip):
        """Try to get device hostname"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return 'Unknown'
    
    def scan_connected_devices(self):
        """
        Scan network and return ONLY real connected devices
        """
        print("🔍 Scanning for connected devices on your network...\n")
        
        local_ip = self.get_local_ip()
        network_range = self.get_network_range()
        
        print(f"Your IP: {local_ip}")
        print(f"Network: {network_range}.0/24\n")
        
        devices = []
        system = platform.system()
        
        try:
            if system == "Windows":
                # Get ARP table
                result = subprocess.check_output(["arp", "-a"], stderr=subprocess.STDOUT)
                output = result.decode('utf-8', errors='ignore')
                
                # Parse ARP table
                pattern = r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F-]{17})\s+(dynamic|static)'
                matches = re.findall(pattern, output)
                
                for ip, mac, type_ in matches:
                    mac_formatted = mac.replace('-', ':')
                    
                    # Filter to show only real devices
                    if self.is_real_device(ip, mac_formatted):
                        # Try to get hostname
                        hostname = self.get_hostname(ip)
                        
                        # Detect device type
                        device_type = self.detect_device_type(ip, mac_formatted, hostname)
                        
                        devices.append({
                            'IP': ip,
                            'MAC': mac_formatted,
                            'Hostname': hostname,
                            'Type': device_type,
                            'Status': 'Connected',
                            'Connection Type': type_.capitalize()
                        })
            
            elif system == "Linux":
                # Linux: Use ip neigh
                try:
                    result = subprocess.check_output(["ip", "neigh"], stderr=subprocess.STDOUT)
                    output = result.decode('utf-8', errors='ignore')
                    
                    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+.*\s+lladdr\s+([0-9a-f:]{17})\s+(\w+)'
                    matches = re.findall(pattern, output)
                    
                    for ip, mac, status in matches:
                        if self.is_real_device(ip, mac):
                            hostname = self.get_hostname(ip)
                            device_type = self.detect_device_type(ip, mac, hostname)
                            
                            devices.append({
                                'IP': ip,
                                'MAC': mac,
                                'Hostname': hostname,
                                'Type': device_type,
                                'Status': status.upper(),
                                'Connection Type': 'Dynamic'
                            })
                except:
                    # Fallback to arp -n
                    result = subprocess.check_output(["arp", "-n"], stderr=subprocess.STDOUT)
                    output = result.decode('utf-8', errors='ignore')
                    
                    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+.*\s+([0-9a-f:]{17})'
                    matches = re.findall(pattern, output)
                    
                    for ip, mac in matches:
                        if self.is_real_device(ip, mac):
                            hostname = self.get_hostname(ip)
                            device_type = self.detect_device_type(ip, mac, hostname)
                            
                            devices.append({
                                'IP': ip,
                                'MAC': mac,
                                'Hostname': hostname,
                                'Type': device_type,
                                'Status': 'Connected',
                                'Connection Type': 'Dynamic'
                            })
            
            elif system == "Darwin":  # macOS
                result = subprocess.check_output(["arp", "-a"], stderr=subprocess.STDOUT)
                output = result.decode('utf-8', errors='ignore')
                
                pattern = r'\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+([0-9a-f:]{17})'
                matches = re.findall(pattern, output)
                
                for ip, mac in matches:
                    if self.is_real_device(ip, mac):
                        hostname = self.get_hostname(ip)
                        device_type = self.detect_device_type(ip, mac, hostname)
                        
                        devices.append({
                            'IP': ip,
                            'MAC': mac,
                            'Hostname': hostname,
                            'Type': device_type,
                            'Status': 'Connected',
                            'Connection Type': 'Dynamic'
                        })
            
            self.devices = devices
            return devices
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
    
    def format_devices_table(self, devices):
        """Format devices into a clean table"""
        if not devices:
            return "No devices found or scan failed."
        
        output = []
        output.append("="*90)
        output.append("📱 DEVICES CONNECTED TO YOUR NETWORK")
        output.append("="*90)
        output.append(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output.append(f"Total Devices Found: {len(devices)}")
        output.append("="*90)
        output.append("")
        
        # Table header
        output.append(f"{'No.':<5} {'IP Address':<18} {'MAC Address':<20} {'Device Type':<25}")
        output.append("-"*90)
        
        for i, device in enumerate(devices, 1):
            output.append(
                f"{i:<5} {device['IP']:<18} {device['MAC']:<20} {device['Type']:<25}"
            )
        
        output.append("")
        output.append("="*90)
        
        # Device summary
        output.append("\n📊 DEVICE SUMMARY:")
        output.append("-"*90)
        
        # Count device types
        type_counts = {}
        for device in devices:
            device_type = device['Type']
            type_counts[device_type] = type_counts.get(device_type, 0) + 1
        
        for device_type, count in type_counts.items():
            output.append(f"  {device_type}: {count}")
        
        output.append("")
        output.append("="*90)
        
        return '\n'.join(output)
    
    def get_simple_list(self):
        """Get simple list of connected device IPs"""
        return [device['IP'] for device in self.devices]


# Quick test
if __name__ == "__main__":
    from colorama import init, Fore, Style
    init(autoreset=True)
    
    scanner = ConnectedDevicesScanner()
    
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "📱 CONNECTED DEVICES SCANNER")
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print()
    
    # Scan for devices
    devices = scanner.scan_connected_devices()
    
    if devices:
        # Display formatted table
        table = scanner.format_devices_table(devices)
        print(Fore.WHITE + table)
        
        print(Fore.GREEN + f"\n✅ Found {len(devices)} real device(s) connected to your network!")
        print(Fore.YELLOW + "\n💡 These are actual devices like phones, laptops, smart TVs, etc.")
    else:
        print(Fore.YELLOW + "\n⚠️ No devices found. Try running as administrator.")
        print(Fore.CYAN + "Tip: Make sure other devices are connected to your WiFi.")
