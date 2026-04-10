from colorama import init, Fore, Back, Style
from password_checker import check_password
from phishing_detector import check_url
from wifi_scanner import scan_wifi
from ip_analyzer import IPAnalyzer
from network_scanner import NetworkDeviceScanner
from risk_engine import calculate_risk
from email_phishing_detector import EmailPhishingDetector
from password_generator import PasswordGenerator

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

    # ─── Email Phishing Detection ───
    print_section("EMAIL PHISHING DETECTION")
    email_choice = input(Fore.YELLOW + "Analyze email for phishing? (yes/no): " + Style.RESET_ALL).lower()
    
    email_detector = EmailPhishingDetector()
    email_result = None
    email_score = 0
    
    if email_choice == 'yes':
        print(Fore.CYAN + "\n📧 Enter email details for analysis:")
        subject = input(Fore.YELLOW + "Email Subject: " + Style.RESET_ALL)
        sender = input(Fore.YELLOW + "Sender Email: " + Style.RESET_ALL)
        
        print(Fore.CYAN + "Email Body (press Enter twice to finish):")
        body_lines = []
        while True:
            line = input()
            if not line:
                break
            body_lines.append(line)
        body = '\n'.join(body_lines)
        
        links_input = input(Fore.YELLOW + "Links in email (comma-separated): " + Style.RESET_ALL)
        links = [link.strip() for link in links_input.split(',')] if links_input else []
        
        attachments_input = input(Fore.YELLOW + "Attachments (comma-separated, e.g., file.pdf): " + Style.RESET_ALL)
        attachments = [att.strip() for att in attachments_input.split(',')] if attachments_input else []
        
        print(Fore.CYAN + "\n🔍 Analyzing email...\n")
        email_result = email_detector.analyze_email(
            subject=subject,
            sender=sender,
            body=body,
            links=links,
            attachments=attachments
        )
        
        formatted_email = email_detector.format_results(email_result)
        print(Fore.WHITE + formatted_email)
        
        email_score = email_result.get("Risk Score", 0)
    else:
        print(Fore.CYAN + "Skipped email analysis")

    # ─── Password Generator ───
    print_section("PASSWORD GENERATOR & MANAGER")
    pwd_gen_choice = input(Fore.YELLOW + "Generate secure password? (yes/no): " + Style.RESET_ALL).lower()
    
    pwd_generator = PasswordGenerator()
    generated_pwd = None
    
    if pwd_gen_choice == 'yes':
        print(Fore.CYAN + "\n🔐 Password Generator Options:")
        length = int(input(Fore.YELLOW + "Password length (default 16): " + Style.RESET_ALL) or "16")
        
        use_upper = input(Fore.YELLOW + "Include uppercase? (yes/no, default yes): " + Style.RESET_ALL).lower() != 'no'
        use_lower = input(Fore.YELLOW + "Include lowercase? (yes/no, default yes): " + Style.RESET_ALL).lower() != 'no'
        use_digits = input(Fore.YELLOW + "Include digits? (yes/no, default yes): " + Style.RESET_ALL).lower() != 'no'
        use_symbols = input(Fore.YELLOW + "Include symbols? (yes/no, default yes): " + Style.RESET_ALL).lower() != 'no'
        
        print(Fore.CYAN + "\nGenerating password...\n")
        generated_pwd, strength_info = pwd_generator.generate_password(
            length=length,
            use_uppercase=use_upper,
            use_lowercase=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols
        )
        
        formatted_pwd = pwd_generator.format_password_info(generated_pwd, strength_info)
        print(Fore.WHITE + formatted_pwd)
        
        # Option to store password
        store_choice = input(Fore.YELLOW + "\nStore this password securely? (yes/no): " + Style.RESET_ALL).lower()
        if store_choice == 'yes':
            service = input(Fore.YELLOW + "Service name: " + Style.RESET_ALL)
            username = input(Fore.YELLOW + "Username: " + Style.RESET_ALL)
            url = input(Fore.YELLOW + "URL (optional): " + Style.RESET_ALL)
            
            pwd_generator.store_password(service, username, generated_pwd, url)
            print(Fore.GREEN + "✅ Password stored securely!")
    else:
        print(Fore.CYAN + "Skipped password generation")

    # ─── Risk Calculation ───
    print_section("OVERALL SECURITY ASSESSMENT")
    
    # Add IP score to calculation if available
    if ip_score > 0:
        scores.append(ip_score)
    
    # Add email score to calculation if available
    if email_score > 0:
        scores.append(email_score)
    
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
