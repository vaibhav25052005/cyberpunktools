from colorama import init, Fore, Back, Style
from password_checker import check_password
from phishing_detector import check_url
from wifi_scanner import scan_wifi
from ip_analyzer import IPAnalyzer
from network_scanner import NetworkDeviceScanner
from risk_engine import calculate_risk

# Initialize colorama
init(autoreset=True)

def print_header():
    """Print application header"""
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + "🔐 PERSONAL CYBER SECURITY ASSISTANT")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.YELLOW + "Protecting your digital world, one scan at a time!")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60 + "\n")

def print_section(title):
    """Print section header"""
    print(Fore.MAGENTA + Style.BRIGHT + f"\n{'─' * 60}")
    print(Fore.MAGENTA + Style.BRIGHT + f"📌 {title}")
    print(Fore.MAGENTA + Style.BRIGHT + f"{'─' * 60}")

def print_result(label, value, color=Fore.WHITE):
    """Print formatted result"""
    print(f"{Fore.CYAN}{label}: {color}{value}{Style.RESET_ALL}")

def main():
    print_header()

    scores = []

    # ─── Password Check ───
    print_section("PASSWORD STRENGTH ANALYSIS")
    pwd = input(Fore.YELLOW + "Enter password to check: " + Style.RESET_ALL)
    pwd_strength, pwd_score, pwd_feedback = check_password(pwd)

    print_result("Password Strength", pwd_strength, 
                Fore.RED if pwd_strength == "Weak" else 
                Fore.YELLOW if pwd_strength == "Medium" else 
                Fore.GREEN)
    print_result("Risk Score", f"{pwd_score}/100")

    if pwd_feedback:
        print(Fore.YELLOW + "\nSuggestions:")
        for fb in pwd_feedback:
            print(f"  {fb}")
    
    scores.append(pwd_score)

    # ─── URL Check ───
    print_section("PHISHING URL DETECTION")
    url = input(Fore.YELLOW + "Enter URL to check: " + Style.RESET_ALL)
    url_status, url_score, url_feedback = check_url(url)

    print_result("URL Status", url_status,
                Fore.RED if url_status == "Dangerous" else
                Fore.YELLOW if url_status in ["Suspicious", "Risky"] else
                Fore.GREEN)
    print_result("Risk Score", f"{url_score}/100")

    if url_feedback:
        print(Fore.YELLOW + "\nWarnings:")
        for fb in url_feedback:
            print(f"  {fb}")
    
    scores.append(url_score)

    # ─── WiFi Scan ───
    print_section("WIFI NETWORK SCAN")
    print(Fore.CYAN + "Scanning for available WiFi networks...\n")
    wifi_data, wifi_error = scan_wifi()

    if wifi_error:
        print(Fore.RED + f"⚠️ {wifi_error}")
    else:
        print(Fore.GREEN + "✅ WiFi scan complete!")
        print(Fore.WHITE + wifi_data)

    # ─── IP Analysis ───
    print_section("IP ADDRESS ANALYSIS")
    ip_choice = input(Fore.YELLOW + "Analyze your current IP? (yes/no): " + Style.RESET_ALL).lower()
    
    ip_analyzer = IPAnalyzer()
    ip_result = None
    ip_score = 0
    
    if ip_choice == 'yes':
        print(Fore.CYAN + "Fetching your public IP...")
        public_ip = ip_analyzer.get_public_ip()
        print(Fore.GREEN + f"Your Public IP: {public_ip}\n")
        
        analyze_more = input(Fore.YELLOW + "Analyze this IP in detail? (yes/no): " + Style.RESET_ALL).lower()
        
        if analyze_more == 'yes':
            ip_result = ip_analyzer.check_ip(public_ip)
            
            if ip_result.get("Status") == "Success":
                print_result("Country", ip_result.get("Country", "Unknown"))
                print_result("City", ip_result.get("City", "Unknown"))
                print_result("ISP", ip_result.get("ISP", "Unknown"))
                print_result("Organization", ip_result.get("Organization", "Unknown"))
                
                risk = ip_result.get("Risk Level", "UNKNOWN")
                risk_color = Fore.RED if risk == "HIGH" else Fore.YELLOW if risk == "MEDIUM" else Fore.GREEN
                print_result("Risk Level", risk, risk_color)
                print_result("Risk Score", f"{ip_result.get('Risk Score', 0)}/100")
                
                if ip_result.get("Warnings"):
                    print(Fore.YELLOW + "\n⚠️ Warnings:")
                    for warning in ip_result["Warnings"]:
                        print(f"  {warning}")
                
                ip_score = ip_result.get("Risk Score", 0)
            else:
                print(Fore.RED + f"❌ Error: {ip_result.get('Error', 'Unknown')}")
                ip_score = 50
        else:
            ip_score = 0
    else:
        print(Fore.CYAN + "Skipped IP analysis")
        ip_score = 0

    # ─── Network Device Scan ───
    print_section("NETWORK DEVICE SCAN")
    network_choice = input(Fore.YELLOW + "Scan for connected devices? (yes/no): " + Style.RESET_ALL).lower()
    
    network_scanner = NetworkDeviceScanner()
    network_result = None
    
    if network_choice == 'yes':
        print(Fore.CYAN + "\n🔍 Scanning network for connected devices...\n")
        network_result = network_scanner.scan_all_devices()
        formatted = network_scanner.format_results(network_result)
        print(Fore.WHITE + formatted)
        
        if network_result.get('Devices'):
            print(Fore.GREEN + f"\n✅ Found {network_result['Total Devices']} device(s) on your network!")
        else:
            print(Fore.YELLOW + "\n⚠️ No devices found. Try running as administrator.")
    else:
        print(Fore.CYAN + "Skipped network scan")

    # ─── Risk Calculation ───
    print_section("OVERALL SECURITY ASSESSMENT")
    
    # Add IP score to calculation if available
    if ip_score > 0:
        scores.append(ip_score)
    
    risk_level, recommendations = calculate_risk(scores)

    print(Fore.CYAN + f"Overall Risk Level: {Style.BRIGHT}{risk_level}")
    
    print(Fore.YELLOW + f"\n📋 Security Recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")

    # ─── Footer ───
    print(Fore.CYAN + Style.BRIGHT + f"\n{'=' * 60}")
    print(Fore.GREEN + Style.BRIGHT + "✅ Scan Complete!")
    print(Fore.CYAN + Style.BRIGHT + f"{'=' * 60}")
    print(Fore.YELLOW + "\n💡 Stay safe online! Regular security checks help protect your digital life.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n⚠️ Scan interrupted by user.")
    except Exception as e:
        print(Fore.RED + f"\n\n❌ An error occurred: {e}")
