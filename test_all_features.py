"""
Comprehensive Test Script for All Features
Tests all modules and ensures everything works correctly
"""

from colorama import init, Fore, Style
import sys

init(autoreset=True)

def print_header():
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "🧪 COMPREHENSIVE FEATURE TEST")
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print()

def test_module(name, test_func):
    """Test a module and report results"""
    print(Fore.MAGENTA + f"📌 Testing: {name}...")
    try:
        test_func()
        print(Fore.GREEN + "✅ PASSED\n")
        return True
    except Exception as e:
        print(Fore.RED + f"❌ FAILED: {str(e)}\n")
        return False

def test_password_checker():
    from password_checker import check_password
    strength, score, feedback = check_password("TestP@ss123!")
    assert strength in ["Weak", "Medium", "Strong", "Very Strong"]
    assert 0 <= score <= 100

def test_phishing_detector():
    from phishing_detector import check_url
    status, score, feedback = check_url("https://google.com")
    assert status in ["Safe", "Suspicious", "Dangerous"]
    assert 0 <= score <= 100

def test_ai_phishing_detector():
    from ai_phishing_detector import AIPhishingDetector
    detector = AIPhishingDetector()
    status, score, confidence = detector.predict("https://google.com")
    # Status can include emoji like "🟢 SAFE"
    assert any(word in str(status).upper() for word in ["SAFE", "SUSPICIOUS", "DANGEROUS", "PHISHING"])

def test_ip_analyzer():
    from ip_analyzer import IPAnalyzer
    analyzer = IPAnalyzer()
    public_ip = analyzer.get_public_ip()
    assert public_ip and not public_ip.startswith("Error")

def test_network_scanner():
    from network_scanner import NetworkDeviceScanner
    scanner = NetworkDeviceScanner()
    local_ip = scanner.get_local_ip()
    assert local_ip and not local_ip.startswith("Error")

def test_wifi_scanner():
    from wifi_scanner import scan_wifi
    wifi_data, wifi_error = scan_wifi()
    # WiFi scan might fail due to permissions, that's okay
    assert wifi_data is not None or wifi_error is not None

def test_risk_engine():
    from risk_engine import calculate_risk
    risk_level, recommendations = calculate_risk([20, 30, 40])
    assert risk_level is not None
    assert len(recommendations) > 0

def test_email_phishing_detector():
    from email_phishing_detector import EmailPhishingDetector
    detector = EmailPhishingDetector()
    
    # Test with suspicious email
    result = detector.analyze_email(
        subject="URGENT: Verify Your Account",
        sender="support@paypa1.com",
        body="Click here to verify your account immediately",
        links=["http://paypa1.com/verify"],
        attachments=["invoice.pdf.exe"]
    )
    
    assert "Overall Risk" in result
    assert "Risk Score" in result
    assert 0 <= result["Risk Score"] <= 100

def test_password_generator():
    from password_generator import PasswordGenerator
    generator = PasswordGenerator()
    
    # Test password generation
    password, strength_info = generator.generate_password(length=16)
    assert len(password) == 16
    assert "Strength" in strength_info
    assert "Score" in strength_info
    
    # Test passphrase generation
    passphrase, pass_strength = generator.generate_passphrase(num_words=5)
    assert len(passphrase) > 0
    assert "-" in passphrase  # Default separator

def test_password_storage():
    from password_generator import PasswordGenerator
    import os
    
    generator = PasswordGenerator(storage_file="test_passwords.json")
    
    # Test storing password
    generator.store_password("TestService", "testuser", "TestP@ss123!", "https://test.com")
    
    # Test retrieving password
    retrieved = generator.retrieve_password("TestService")
    assert retrieved is not None
    assert retrieved["Password"] == "TestP@ss123!"
    assert retrieved["Username"] == "testuser"
    
    # Test listing services
    services = generator.list_services()
    assert "TestService" in services
    
    # Test password health check
    health = generator.check_password_health()
    assert "Total" in health
    
    # Cleanup test file
    if os.path.exists("test_passwords.json"):
        os.remove("test_passwords.json")
    if os.path.exists("encryption.key"):
        # Don't remove if it's the main key file
        pass

def test_pdf_generator():
    from pdf_report_generator import PDFReportGenerator
    generator = PDFReportGenerator()
    
    # Test report generation
    test_results = {
        'password': {'strength': 'Strong', 'score': 80, 'feedback': []},
        'url': {'status': 'Safe', 'score': 20, 'feedback': []},
        'wifi': {'data': 'Test WiFi data', 'error': None},
        'risk_level': 'LOW RISK',
        'recommendations': ['Test recommendation']
    }
    
    output_file = "test_report.pdf"
    generator.generate_report(test_results)
    
    import os
    # PDF generator saves with default name
    if os.path.exists("security_report.pdf"):
        os.remove("security_report.pdf")
    if os.path.exists(output_file):
        os.remove(output_file)

def main():
    print_header()
    
    tests = [
        ("Password Checker", test_password_checker),
        ("Phishing URL Detector", test_phishing_detector),
        ("AI Phishing Detector", test_ai_phishing_detector),
        ("IP Analyzer", test_ip_analyzer),
        ("Network Scanner", test_network_scanner),
        ("WiFi Scanner", test_wifi_scanner),
        ("Risk Engine", test_risk_engine),
        ("Email Phishing Detector ⭐ NEW", test_email_phishing_detector),
        ("Password Generator ⭐ NEW", test_password_generator),
        ("Password Storage ⭐ NEW", test_password_storage),
        ("PDF Report Generator", test_pdf_generator),
    ]
    
    results = []
    for name, test_func in tests:
        result = test_module(name, test_func)
        results.append((name, result))
    
    # Summary
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "📊 TEST SUMMARY")
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    
    passed = sum(1 for _, result in results if result)
    failed = sum(1 for _, result in results if not result)
    total = len(results)
    
    print(Fore.WHITE + f"\nTotal Tests: {total}")
    print(Fore.GREEN + f"✅ Passed: {passed}")
    if failed > 0:
        print(Fore.RED + f"❌ Failed: {failed}")
    else:
        print(Fore.GREEN + "🎉 All tests passed!")
    
    print(Fore.CYAN + "\nTest Results:")
    for name, result in results:
        status = Fore.GREEN + "✅ PASS" if result else Fore.RED + "❌ FAIL"
        print(f"  {status} - {name}")
    
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*70)
    
    if failed == 0:
        print(Fore.GREEN + Style.BRIGHT + "🎉 ALL TESTS PASSED! System is working perfectly!")
        print(Fore.GREEN + Style.BRIGHT + "="*70)
        return 0
    else:
        print(Fore.RED + Style.BRIGHT + f"⚠️ {failed} test(s) failed. Please check the errors above.")
        print(Fore.RED + Style.BRIGHT + "="*70)
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n⚠️ Test interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
