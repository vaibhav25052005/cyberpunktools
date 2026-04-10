import subprocess
import re
import platform
import socket
from datetime import datetime

class NetworkDeviceScanner:
    """
    Scans local network to find all connected devices
    Shows IP addresses, MAC addresses, and device info
    """
    
    def __init__(self):
        self.connected_devices = []
        
    def get_local_ip(self):
        """Get local IP address of current machine"""
        try:
            # Create socket connection to get local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception as e:
            return f"Error: {e}"
    
    def get_network_range(self):
        """Get network range (subnet) from local IP"""
        local_ip = self.get_local_ip()
        if local_ip.startswith("Error"):
            return None, None
        
        # Extract first 3 octets (e.g., 192.168.1)
        parts = local_ip.split('.')
        network_prefix = '.'.join(parts[:3])
        return local_ip, network_prefix
    
    def scan_network_arp(self):
        """
        Scan network using ARP table (Windows/Linux/Mac)
        Returns list of connected devices
        """
        devices = []
        system = platform.system()
        
        try:
            if system == "Windows":
                # Windows: Use arp -a command
                result = subprocess.check_output(["arp", "-a"], stderr=subprocess.STDOUT)
                output = result.decode('utf-8', errors='ignore')
                
                # Parse ARP table
                # Format: 192.168.1.1         00-11-22-33-44-55     dynamic
                pattern = r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F-]{17})\s+(dynamic|static)'
                matches = re.findall(pattern, output)
                
                for ip, mac, type_ in matches:
                    if ip != "255.255.255.255":  # Skip broadcast
                        devices.append({
                            'IP': ip,
                            'MAC': mac.replace('-', ':'),
                            'Type': type_.capitalize(),
                            'Status': 'Active'
                        })
            
            elif system == "Linux":
                # Linux: Use arp -n or ip neigh
                try:
                    result = subprocess.check_output(["ip", "neigh"], stderr=subprocess.STDOUT)
                    output = result.decode('utf-8', errors='ignore')
                    
                    # Format: 192.168.1.1 dev wlan0 lladdr 00:11:22:33:44:55 REACHABLE
                    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+.*\s+lladdr\s+([0-9a-f:]{17})\s+(\w+)'
                    matches = re.findall(pattern, output)
                    
                    for ip, mac, status in matches:
                        devices.append({
                            'IP': ip,
                            'MAC': mac,
                            'Type': 'Dynamic',
                            'Status': status.upper()
                        })
                except:
                    # Fallback to arp -n
                    result = subprocess.check_output(["arp", "-n"], stderr=subprocess.STDOUT)
                    output = result.decode('utf-8', errors='ignore')
                    
                    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+.*\s+([0-9a-f:]{17})'
                    matches = re.findall(pattern, output)
                    
                    for ip, mac in matches:
                        devices.append({
                            'IP': ip,
                            'MAC': mac,
                            'Type': 'Dynamic',
                            'Status': 'Active'
                        })
            
            elif system == "Darwin":  # macOS
                result = subprocess.check_output(["arp", "-a"], stderr=subprocess.STDOUT)
                output = result.decode('utf-8', errors='ignore')
                
                # Format: ? (192.168.1.1) at 0:11:22:33:44:55 on en0
                pattern = r'\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+([0-9a-f:]{17})'
                matches = re.findall(pattern, output)
                
                for ip, mac in matches:
                    devices.append({
                        'IP': ip,
                        'MAC': mac,
                        'Type': 'Dynamic',
                        'Status': 'Active'
                    })
            
            self.connected_devices = devices
            return devices
            
        except subprocess.CalledProcessError as e:
            return [{'Error': f"Scan failed: {e.output.decode('utf-8', errors='ignore')}"}]
        except Exception as e:
            return [{'Error': f"Error: {str(e)}"}]
    
    def ping_scan(self, ip_range=None):
        """
        Active ping scan to discover devices
        More thorough but slower
        """
        if ip_range is None:
            _, ip_range = self.get_network_range()
        
        if ip_range is None:
            return []
        
        devices = []
        system = platform.system()
        
        print(f"Scanning {ip_range}.1 to {ip_range}.254...")
        
        # Scan common IPs first (router, DNS, etc.)
        common_ips = [1, 2, 10, 50, 100, 150, 200, 254]
        
        for last_octet in common_ips:
            ip = f"{ip_range}.{last_octet}"
            try:
                if system == "Windows":
                    cmd = ["ping", "-n", "1", "-w", "100", ip]
                else:
                    cmd = ["ping", "-c", "1", "-W", "1", ip]
                
                result = subprocess.run(cmd, capture_output=True, timeout=2)
                
                if result.returncode == 0:
                    devices.append({
                        'IP': ip,
                        'MAC': 'Unknown',
                        'Type': 'Ping',
                        'Status': 'Online'
                    })
            except:
                pass
        
        return devices
    
    def get_device_info(self, ip):
        """Get additional info about a device"""
        info = {}
        
        try:
            # Reverse DNS lookup
            hostname = socket.gethostbyaddr(ip)[0]
            info['Hostname'] = hostname
        except:
            info['Hostname'] = 'Unknown'
        
        # Check if it's a common device type
        common_devices = {
            'router': ['192.168.1.1', '192.168.0.1', '10.0.0.1'],
            'dns': ['8.8.8.8', '8.8.4.4', '1.1.1.1'],
        }
        
        for device_type, ips in common_devices.items():
            if ip in ips:
                info['Device Type'] = device_type.upper()
                break
        else:
            info['Device Type'] = 'Unknown'
        
        return info
    
    def scan_all_devices(self):
        """
        Complete network scan
        Returns all connected devices with details
        """
        print("Starting network scan...")
        scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get local network info
        local_ip = self.get_local_ip()
        _, network_range = self.get_network_range()
        
        print(f"Local IP: {local_ip}")
        print(f"Network: {network_range}.0/24\n")
        
        # Scan ARP table
        devices = self.scan_network_arp()
        
        # Add scan metadata
        scan_result = {
            'Scan Time': scan_time,
            'Local IP': local_ip,
            'Network Range': f"{network_range}.0/24" if network_range else "Unknown",
            'Total Devices': len(devices),
            'Devices': devices
        }
        
        return scan_result
    
    def format_results(self, scan_result):
        """Format scan results for display"""
        output = []
        output.append("="*70)
        output.append("NETWORK DEVICE SCAN RESULTS")
        output.append("="*70)
        output.append(f"Scan Time: {scan_result.get('Scan Time', 'Unknown')}")
        output.append(f"Local IP: {scan_result.get('Local IP', 'Unknown')}")
        output.append(f"Network: {scan_result.get('Network Range', 'Unknown')}")
        output.append(f"Total Devices Found: {scan_result.get('Total Devices', 0)}")
        output.append("="*70)
        output.append("")
        
        devices = scan_result.get('Devices', [])
        
        if not devices:
            output.append("No devices found or scan failed.")
            return '\n'.join(output)
        
        output.append(f"{'No.':<5} {'IP Address':<20} {'MAC Address':<20} {'Status':<12} {'Type':<10}")
        output.append("-"*70)
        
        for i, device in enumerate(devices, 1):
            if 'Error' in device:
                output.append(f"Error: {device['Error']}")
                break
            
            ip = device.get('IP', 'Unknown')
            mac = device.get('MAC', 'Unknown')
            status = device.get('Status', 'Unknown')
            type_ = device.get('Type', 'Unknown')
            
            output.append(f"{i:<5} {ip:<20} {mac:<20} {status:<12} {type_:<10}")
        
        output.append("")
        output.append("="*70)
        
        return '\n'.join(output)


# Quick test
if __name__ == "__main__":
    from colorama import init, Fore, Style
    init(autoreset=True)
    
    scanner = NetworkDeviceScanner()
    
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "📡 NETWORK DEVICE SCANNER")
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    
    # Get local IP
    local_ip = scanner.get_local_ip()
    print(Fore.GREEN + f"\nYour Local IP: {local_ip}")
    
    # Scan network
    print(Fore.MAGENTA + "\n🔍 Scanning network for connected devices...\n")
    
    result = scanner.scan_all_devices()
    
    # Display results
    formatted = scanner.format_results(result)
    print(Fore.WHITE + formatted)
    
    if result.get('Devices'):
        print(Fore.GREEN + f"\n✅ Found {result['Total Devices']} device(s) on your network!")
    else:
        print(Fore.YELLOW + "\n⚠️ No devices found. Try running as administrator.")
