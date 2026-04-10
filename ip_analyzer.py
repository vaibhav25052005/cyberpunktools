import requests
import json
from datetime import datetime

class IPAnalyzer:
    """
    Advanced IP Address Analysis Module
    Fetches IP metadata and performs risk assessment
    """
    
    def __init__(self):
        self.api_url = "http://ip-api.com/json/"
        self.public_ip_api = "https://api.ipify.org?format=json"
        
    def get_public_ip(self):
        """Get current public IP address"""
        try:
            response = requests.get(self.public_ip_api, timeout=5)
            return response.json().get("ip", "Unknown")
        except Exception as e:
            return f"Error: {e}"
    
    def check_ip(self, ip):
        """
        Analyze IP address for security risks
        Returns: dict with IP details and risk assessment
        """
        try:
            # Fetch IP data from API
            url = f"{self.api_url}{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if data.get("status") == "fail":
                return {
                    "IP": ip,
                    "Status": "Failed",
                    "Error": data.get("message", "Unknown error"),
                    "Risk": "UNKNOWN"
                }
            
            # Extract data
            country = data.get("country", "Unknown")
            city = data.get("city", "Unknown")
            region = data.get("regionName", "Unknown")
            zipcode = data.get("zip", "Unknown")
            lat = data.get("lat", 0)
            lon = data.get("lon", 0)
            timezone = data.get("timezone", "Unknown")
            isp = data.get("isp", "Unknown")
            org = data.get("org", "Unknown")
            asn = data.get("as", "Unknown")
            
            # Perform risk analysis
            risk_level, risk_score, warnings = self.analyze_risk(data)
            
            # Check blacklist
            blacklist_status = self.check_blacklist(ip)
            
            return {
                "IP": ip,
                "Status": "Success",
                "Country": country,
                "Country Code": data.get("countryCode", "Unknown"),
                "Region": region,
                "City": city,
                "Zipcode": zipcode,
                "Coordinates": f"{lat}, {lon}",
                "Timezone": timezone,
                "ISP": isp,
                "Organization": org,
                "ASN": asn,
                "Risk Level": risk_level,
                "Risk Score": risk_score,
                "Blacklisted": blacklist_status,
                "Warnings": warnings,
                "Checked At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
        except requests.exceptions.Timeout:
            return {
                "IP": ip,
                "Status": "Error",
                "Error": "Request timeout",
                "Risk": "UNKNOWN"
            }
        except requests.exceptions.RequestException as e:
            return {
                "IP": ip,
                "Status": "Error",
                "Error": str(e),
                "Risk": "UNKNOWN"
            }
    
    def analyze_risk(self, ip_data):
        """
        Analyze IP risk based on multiple factors
        Returns: (risk_level, risk_score, warnings)
        """
        risk_score = 0
        warnings = []
        isp = ip_data.get("isp", "").lower()
        org = ip_data.get("org", "").lower()
        country = ip_data.get("country", "")
        country_code = ip_data.get("countryCode", "")
        
        # Check 1: VPN/Proxy Detection
        vpn_keywords = ["vpn", "proxy", "hosting", "datacenter", "cloud", "tor"]
        if any(keyword in isp or keyword in org for keyword in vpn_keywords):
            risk_score += 40
            warnings.append("⚠️ VPN/Proxy/Datacenter detected")
        
        # Check 2: Foreign country (example: not from India)
        # You can customize this based on your location
        trusted_countries = ["IN", "US", "GB", "CA", "AU", "DE", "FR"]
        if country_code and country_code not in trusted_countries:
            risk_score += 25
            warnings.append(f"⚠️ Access from foreign country: {country}")
        
        # Check 3: Suspicious ISP
        suspicious_isps = ["anonymous", "private", "secure"]
        if any(keyword in isp for keyword in suspicious_isps):
            risk_score += 30
            warnings.append("⚠️ Suspicious ISP detected")
        
        # Check 4: Known hosting providers (often used for attacks)
        hosting_providers = ["amazon", "digitalocean", "linode", "ovh", "hetzner"]
        if any(provider in isp or provider in org for provider in hosting_providers):
            risk_score += 15
            warnings.append("ℹ️ Hosting provider IP (may be legitimate)")
        
        # Determine risk level
        if risk_score >= 60:
            risk_level = "HIGH"
        elif risk_score >= 30:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        
        return risk_level, risk_score, warnings
    
    def check_blacklist(self, ip):
        """
        Check if IP is in common blacklists
        Note: This is a simplified check. For production, use services like:
        - Spamhaus
        - AbuseIPDB
        - VirusTotal
        """
        # Simplified blacklist check
        # In production, integrate with AbuseIPDB API or similar
        suspicious_ranges = [
            "185.220.",  # Known Tor exit nodes
            "104.244.",  # Suspicious hosting
        ]
        
        for range_prefix in suspicious_ranges:
            if ip.startswith(range_prefix):
                return "Yes - Suspicious Range"
        
        return "No"
    
    def get_current_network_info(self):
        """Get current network IP and basic info"""
        try:
            public_ip = self.get_public_ip()
            if public_ip and not public_ip.startswith("Error"):
                return self.check_ip(public_ip)
            return {"Error": "Could not fetch public IP"}
        except Exception as e:
            return {"Error": str(e)}


# Quick test
if __name__ == "__main__":
    from colorama import init, Fore, Style
    init(autoreset=True)
    
    analyzer = IPAnalyzer()
    
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    print(Fore.CYAN + Style.BRIGHT + "🌐 IP ADDRESS ANALYZER")
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    
    # Test with sample IPs
    test_ips = [
        "8.8.8.8",           # Google DNS
        "1.1.1.1",           # Cloudflare DNS
        "208.67.222.222",    # OpenDNS
    ]
    
    for ip in test_ips:
        print(Fore.MAGENTA + f"\n📌 Analyzing: {ip}")
        print("-"*60)
        
        result = analyzer.check_ip(ip)
        
        if result.get("Status") == "Success":
            print(Fore.GREEN + f"✅ Country: {result['Country']}")
            print(Fore.GREEN + f"✅ City: {result['City']}")
            print(Fore.GREEN + f"✅ ISP: {result['ISP']}")
            print(Fore.GREEN + f"✅ Organization: {result['Organization']}")
            
            risk = result['Risk Level']
            risk_color = Fore.RED if risk == "HIGH" else Fore.YELLOW if risk == "MEDIUM" else Fore.GREEN
            print(Fore.GREEN + f"✅ Risk Level: {risk_color}{Style.BRIGHT}{risk}")
            print(Fore.GREEN + f"✅ Risk Score: {result['Risk Score']}/100")
            
            if result['Warnings']:
                print(Fore.YELLOW + "\n⚠️ Warnings:")
                for warning in result['Warnings']:
                    print(f"  {warning}")
        else:
            print(Fore.RED + f"❌ Error: {result.get('Error', 'Unknown')}")
    
    # Get current public IP
    print(Fore.MAGENTA + f"\n📌 Your Current Public IP:")
    print("-"*60)
    current_ip = analyzer.get_public_ip()
    print(Fore.CYAN + f"Public IP: {current_ip}")
