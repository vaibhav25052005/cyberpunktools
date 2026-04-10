import subprocess
import platform

def scan_wifi():
    """
    Scan for available WiFi networks.
    Works on Windows and Linux.
    Returns: (networks_list, error_message)
    """
    system = platform.system()
    
    try:
        if system == "Windows":
            result = subprocess.check_output(
                ["netsh", "wlan", "show", "networks", "mode=bssid"],
                stderr=subprocess.STDOUT
            )
            return result.decode("utf-8", errors="ignore"), None
        
        elif system == "Linux":
            # For Linux, you can integrate with iwlist or nmcli
            result = subprocess.check_output(
                ["nmcli", "-t", "-f", "SSID,SIGNAL,SECURITY", "dev", "wifi"],
                stderr=subprocess.STDOUT
            )
            return result.decode("utf-8", errors="ignore"), None
        
        else:
            return None, f"Unsupported operating system: {system}"
            
    except subprocess.CalledProcessError as e:
        return None, f"Error scanning WiFi: {e.output.decode('utf-8', errors='ignore')}"
    except FileNotFoundError:
        return None, "WiFi scanning tool not found. Make sure WiFi is enabled."
