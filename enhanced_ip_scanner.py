import subprocess
import re
import platform
import socket
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

class EnhancedIPScanner:
    """
    Advanced IP Address Discovery System
    Actively scans entire network range to find ALL connected devices
    Uses multiple methods: ARP, Ping Sweep, Port Scanning
    """
    
    def __init__(self):
        self.devices = {}
        self.scan_progress = 0
        
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
        """Get network subnet range"""
        local_ip = self.get_local_ip()
        if local_ip.startswith("Error"):
            return None, None
        
        parts = local_ip.split('.')
        network_prefix = '.'.join(parts[:3])
        your_ip = local_ip
        return network_prefix, your_ip
    
    def ping_host(self, ip, timeout=1):
        """
        Ping a single IP address
        Returns True if host is up
        """
        try:
            system = platform.system()
            if system == "Windows":
                cmd = ["ping", "-n", "1", "-w", str(timeout * 1000), ip]
            else:
                cmd = ["ping", "-c", "1", "-W", str(timeout), ip]
            
            result = subprocess.run(cmd, capture_output=True, timeout=timeout + 1)
            return result.returncode == 0
        except:
            return False
    
    def get_mac_from_arp(self, ip):
        """Get MAC address from ARP table for a specific IP"""
        try:
            system = platform.system()
            
            if system == "Windows":
                # First ping the IP to ensure it's in ARP table
                subprocess.run(["ping", "-n", "1", "-w", "100", ip], 
                             capture_output=True, timeout=2)
                
                # Then read ARP table
                result = subprocess.check_output(["arp", "-a"], stderr=subprocess.STDOUT)
                output = result.decode('utf-8', errors='ignore')
                
                # Find specific IP
                pattern = rf'{re.escape(ip)}\s+([0-9a-fA-F-]{{17}})'
                match = re.search(pattern, output)
                
                if match:
                    return match.group(1).replace('-', ':')
            
            elif system == "Linux":
                subprocess.run(["ping", "-c", "1", "-W", "1", ip], 
                             capture_output=True, timeout=2)
                
                result = subprocess.check_output(["ip", "neigh"], stderr=subprocess.STDOUT)
                output = result.decode('utf-8', errors='ignore')
                
                pattern = rf'{re.escape(ip)}\s+.*\s+lladdr\s+([0-9a-f:]{{17}})'
                match = re.search(pattern, output)
                
                if match:
                    return match.group(1)
            
            elif system == "Darwin":
                subprocess.run(["ping", "-c", "1", "-W", "1", ip], 
                             capture_output=True, timeout=2)
                
                result = subprocess.check_output(["arp", "-a"], stderr=subprocess.STDOUT)
                output = result.decode('utf-8', errors='ignore')
                
                pattern = rf'\({re.escape(ip)}\)\s+at\s+([0-9a-f:]{{17}})'
                match = re.search(pattern, output)
                
                if match:
                    return match.group(1)
                    
        except:
            pass
        
        return "Unknown"
    
    def get_hostname(self, ip):
        """Get hostname for IP address"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return "Unknown"
    
    def detect_device_type(self, ip, mac, hostname):
        """Detect what type of device it is"""
        # Router/Gateway
        if ip.endswith('.1') or ip.endswith('.254'):
            return '🌐 Router/Gateway'
        
        # Known DNS
        if ip in ['8.8.8.8', '8.8.4.4', '1.1.1.1']:
            return '🔍 DNS Server'
        
        # Check MAC vendor
        mac_prefix = mac[:8].lower() if mac != "Unknown" else ""
        
        apple_prefixes = ['00:1b:63', '00:1c:b3', '3c:07:54', '40:6c:8f', 
                         'ac:87:a3', 'b8:53:ac', 'c8:69:cd']
        
        if any(mac_prefix.startswith(p) for p in apple_prefixes):
            return '🍎 Apple Device'
        
        # Check hostname clues
        if hostname != "Unknown":
            h = hostname.lower()
            if 'iphone' in h or 'ipad' in h:
                return '🍎 Apple Device'
            elif 'android' in h or 'samsung' in h:
                return '📱 Android Device'
            elif 'laptop' in h or 'pc' in h or 'desktop' in h:
                return '💻 Computer'
            elif 'tv' in h:
                return '📺 Smart TV'
            elif 'printer' in h:
                return '🖨️ Printer'
        
        return '📡 Connected Device'
    
    def ping_sweep(self, network_prefix, start=1, end=254, max_threads=50):
        """
        Ping sweep entire network range to find active devices
        Uses multi-threading for speed
        """
        active_hosts = []
        total = end - start + 1
        completed = 0
        
        def ping_single(ip):
            if self.ping_host(ip, timeout=1):
                return ip
            return None
        
        # Create IP list
        ip_list = [f"{network_prefix}.{i}" for i in range(start, end + 1)]
        
        # Multi-threaded ping
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            future_to_ip = {executor.submit(ping_single, ip): ip for ip in ip_list}
            
            for future in as_completed(future_to_ip):
                ip = future_to_ip[future]
                try:
                    result = future.result()
                    if result:
                        active_hosts.append(result)
                except:
                    pass
                
                completed += 1
                self.scan_progress = int((completed / total) * 100)
        
        return sorted(active_hosts)
    
    def scan_network_complete(self, callback=None):
        """
        Complete network scan with detailed device information
        Returns list of all connected devices with IP, MAC, hostname, type
        """
        print("🔍 Starting enhanced network scan...\n")
        
        network_prefix, your_ip = self.get_network_range()
        
        if not network_prefix:
            return []
        
        print(f"Your IP: {your_ip}")
        print(f"Network: {network_prefix}.0/24")
        print("Scanning 254 addresses...\n")
        
        # Step 1: Ping sweep to find active hosts
        if callback:
            callback("Step 1/3: Pinging network range...")
        
        active_ips = self.ping_sweep(network_prefix, start=1, end=254, max_threads=50)
        
        print(f"\n✅ Found {len(active_ips)} active hosts\n")
        
        # Step 2: Get detailed info for each active host
        if callback:
            callback(f"Step 2/3: Found {len(active_ips)} devices, gathering details...")
        
        devices = []
        
        for i, ip in enumerate(active_ips, 1):
            if callback:
                callback(f"Step 3/3: Analyzing device {i}/{len(active_ips)}...")
            
            # Get MAC address
            mac = self.get_mac_from_arp(ip)
            
            # Get hostname
            hostname = self.get_hostname(ip)
            
            # Detect device type
            device_type = self.detect_device_type(ip, mac, hostname)
            
            devices.append({
                'IP': ip,
                'MAC': mac,
                'Hostname': hostname,
                'Type': device_type,
                'Status': 'Online',
                'Your Device': ip == your_ip
            })
            
            print(f"  [{i}/{len(active_ips)}] {ip:18} {device_type:25} {mac}")
        
        self.devices = devices
        return devices
    
    def format_results(self, devices, your_ip):
        """Format scan results into beautiful table"""
        if not devices:
            return "No devices found on your network."
        
        output = []
        output.append("="*100)
        output.append("📱 ALL DEVICES CONNECTED TO YOUR NETWORK")
        output.append("="*100)
        output.append(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output.append(f"Your IP: {your_ip}")
        output.append(f"Network: {your_ip.rsplit('.', 1)[0]}.0/24")
        output.append(f"Total Devices Found: {len(devices)}")
        output.append("="*100)
        output.append("")
        
        # Table header
        output.append(f"{'No.':<5} {'IP Address':<18} {'MAC Address':<20} {'Device Type':<25} {'Status':<10}")
        output.append("-"*100)
        
        for i, device in enumerate(devices, 1):
            marker = " ← YOU" if device['Your Device'] else ""
            output.append(
                f"{i:<5} {device['IP']:<18} {device['MAC']:<20} {device['Type']:<25} {device['Status']:<10}{marker}"
            )
        
        output.append("")
        output.append("="*100)
        
        # Device summary
        output.append("\n📊 DEVICE SUMMARY:")
        output.append("-"*100)
        
        type_counts = {}
        for device in devices:
            device_type = device['Type']
            type_counts[device_type] = type_counts.get(device_type, 0) + 1
        
        for device_type, count in type_counts.items():
            output.append(f"  {device_type}: {count}")
        
        output.append("")
        output.append("="*100)
        
        # Your device
        your_device = next((d for d in devices if d['Your Device']), None)
        if your_device:
            output.append(f"\n✅ Your Device: {your_device['IP']}")
        
        output.append("")
        output.append("="*100)
        
        return '\n'.join(output)
    
    def quick_scan(self):
        """Quick scan - only ping common IPs"""
        network_prefix, your_ip = self.get_network_range()
        
        if not network_prefix:
            return []
        
        # Common IPs to check
        common_ips = [1, 2, 10, 50, 100, 150, 200, 254]
        
        active = []
        for last_octet in common_ips:
            ip = f"{network_prefix}.{last_octet}"
            if self.ping_host(ip, timeout=1):
                active.append(ip)
        
        return active


# Quick test
if __name__ == "__main__":
    from colorama import init, Fore, Style
    init(autoreset=True)
    
    scanner = EnhancedIPScanner()
    
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "🔍 ENHANCED IP ADDRESS DISCOVERY")
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print()
    
    # Scan network
    devices = scanner.scan_network_complete()
    
    if devices:
        your_ip = scanner.get_local_ip()
        formatted = scanner.format_results(devices, your_ip)
        print(Fore.WHITE + "\n" + formatted)
        
        print(Fore.GREEN + f"\n✅ Successfully found {len(devices)} device(s) on your network!")
        print(Fore.YELLOW + "\n💡 This scan pinged all 254 addresses in your network range")
    else:
        print(Fore.YELLOW + "\n⚠️ No devices found. Try running as administrator.")
