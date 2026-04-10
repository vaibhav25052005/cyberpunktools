"""
Quick Demo Script - Test All Features
Run this to see all capabilities in action!
"""

from colorama import init, Fore, Style
from password_checker import check_password
from phishing_detector import check_url
from ai_phishing_detector import AIPhishingDetector
from ip_analyzer import IPAnalyzer
from risk_engine import calculate_risk
from pdf_report_generator import PDFReportGenerator

init(autoreset=True)

def demo():
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "🔐 CYBER SECURITY ASSISTANT - FEATURE DEMO")
    print(Fore.CYAN + Style.BRIGHT + "="*70 + "\n")
    
    # Demo 1: Password Checking
    print(Fore.MAGENTA + Style.BRIGHT + "📌 DEMO 1: Password Strength Analysis")
    print("-"*70)
    
    test_passwords = [
        "password123",
        "MyP@ssw0rd!",
        "Tr0ub4dor&3"
    ]
    
    for pwd in test_passwords:
        strength, score, feedback = check_password(pwd)
        color = Fore.RED if strength == "Weak" else Fore.YELLOW if strength == "Medium" else Fore.GREEN
        print(f"\nPassword: {pwd}")
        print(f"Strength: {color}{Style.BRIGHT}{strength}")
        print(f"Risk Score: {score}/100")
    
    # Demo 2: URL Detection (Rule-Based)
    print("\n\n" + Fore.MAGENTA + Style.BRIGHT + "📌 DEMO 2: Rule-Based URL Detection")
    print("-"*70)
    
    test_urls = [
        "https://www.google.com",
        "http://login-verify-bank.com",
        "https://github.com/user/repo"
    ]
    
    for url in test_urls:
        status, score, feedback = check_url(url)
        color = Fore.GREEN if status == "Safe" else Fore.YELLOW if status in ["Risky", "Suspicious"] else Fore.RED
        print(f"\nURL: {url}")
        print(f"Status: {color}{Style.BRIGHT}{status}")
        print(f"Risk Score: {score}/100")
    
    # Demo 3: AI Phishing Detection
    print("\n\n" + Fore.MAGENTA + Style.BRIGHT + "📌 DEMO 3: AI-Powered Phishing Detection")
    print("-"*70)
    
    detector = AIPhishingDetector()
    
    ai_urls = [
        "https://www.google.com/search?q=test",
        "http://secure-login-verify-account.com/update",
        "https://amazon.com/orders"
    ]
    
    for url in ai_urls:
        status, score, confidence = detector.predict(url)
        color = Fore.GREEN if "SAFE" in status else Fore.RED
        print(f"\nURL: {url}")
        print(f"AI Prediction: {color}{Style.BRIGHT}{status}")
        print(f"Risk Score: {score}/100")
        print(f"Confidence: {confidence:.1f}%")
    
    # Demo 4: Risk Assessment
    print("\n\n" + Fore.MAGENTA + Style.BRIGHT + "📌 DEMO 4: Risk Assessment Engine")
    print("-"*70)
    
    test_cases = [
        [75, 70],  # High risk
        [40, 50],  # Medium risk
        [10, 20],  # Low risk
    ]
    
    for i, scores in enumerate(test_cases, 1):
        risk_level, recommendations = calculate_risk(scores)
        print(f"\nTest Case {i}:")
        print(f"Password Score: {scores[0]}, URL Score: {scores[1]}")
        print(f"Overall Risk: {Style.BRIGHT}{risk_level}")
        print(f"Top Recommendation: {recommendations[0]}")
    
    # Demo 5: IP Address Analysis
    print("\n\n" + Fore.MAGENTA + Style.BRIGHT + "📌 DEMO 5: IP Address Analysis")
    print("-"*70)
    
    analyzer = IPAnalyzer()
    test_ips = ["8.8.8.8", "1.1.1.1"]
    
    for ip in test_ips:
        result = analyzer.check_ip(ip)
        if result.get("Status") == "Success":
            print(f"\nIP: {ip}")
            print(f"Country: {result['Country']}")
            print(f"City: {result['City']}")
            print(f"ISP: {result['ISP']}")
            print(f"Risk Level: {result['Risk Level']}")
            print(f"Risk Score: {result['Risk Score']}/100")
    
    # Demo 6: PDF Report
    print("\n\n" + Fore.MAGENTA + Style.BRIGHT + "📌 DEMO 6: PDF Report Generation")
    print("-"*70)
    
    sample_data = {
        'risk_level': '🟡 MEDIUM RISK',
        'recommendations': [
            'Strengthen your passwords',
            'Be cautious with unknown links',
            'Use VPN on public networks'
        ],
        'password': {
            'strength': 'Medium',
            'score': 40,
            'feedback': ['Add special characters', 'Use longer password']
        },
        'url': {
            'status': 'Suspicious',
            'score': 60,
            'feedback': ['Missing HTTPS', 'Suspicious keywords']
        },
        'wifi': {
            'data': 'Network scan completed successfully',
            'error': None
        }
    }
    
    try:
        generator = PDFReportGenerator("demo_report.pdf")
        generator.generate_report(sample_data)
        print(Fore.GREEN + "\n✅ PDF Report generated: demo_report.pdf")
    except Exception as e:
        print(Fore.RED + f"\n❌ Error generating PDF: {e}")
    
    # Summary
    print("\n\n" + Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.GREEN + Style.BRIGHT + "✅ ALL FEATURES DEMONSTRATED SUCCESSFULLY!")
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print("\n📚 Next Steps:")
    print("  1. Run 'python main.py' for interactive CLI")
    print("  2. Run 'python gui_dashboard.py' for GUI")
    print("  3. Run 'python mobile_app.py' for mobile app")
    print("  4. Check 'demo_report.pdf' for sample report\n")


if __name__ == "__main__":
    demo()
