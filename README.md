# 🔐 Personal Cyber Security Assistant - Advanced Edition

> **This system provides real-time, multi-layered cyber threat detection for everyday users without requiring technical knowledge.**

## 🌟 Features

### ✅ Core Security Features
- **Password Strength Analyzer** - Multi-criteria password evaluation
- **Phishing URL Detection** - Rule-based + AI-powered detection
- **WiFi Network Scanner** - Discover nearby networks
- **IP Address Analyzer** - Geolocation, ISP detection, risk assessment ⭐ NEW
- **Risk Assessment Engine** - Overall security scoring

### 🚀 Advanced Features
- **🎨 Modern GUI Dashboard** - Beautiful Tkinter interface with 5 tabs
- **📊 PDF Report Generator** - Professional security reports
- **🧠 AI-Powered Detection** - Machine learning phishing detection
- **📱 Mobile App** - Cross-platform mobile application (Kivy)

---

## 📁 Project Structure

```
CYBERPUNK/
│
├── 📱 MAIN APPLICATIONS
│   ├── main.py                    # Terminal version (CLI)
│   ├── gui_dashboard.py           # Desktop GUI application
│   └── mobile_app.py              # Mobile app (Kivy)
│
├── 🔧 SECURITY MODULES
│   ├── password_checker.py        # Password strength analysis
│   ├── phishing_detector.py       # Rule-based URL checking
│   ├── ai_phishing_detector.py    # AI/ML phishing detection
│   ├── ip_analyzer.py             # IP address analysis ⭐ NEW
│   ├── wifi_scanner.py            # WiFi network scanner
│   └── risk_engine.py             # Risk calculation engine
│
├── 📄 REPORT GENERATOR
│   └── pdf_report_generator.py    # PDF report generation
│
└── 📚 DOCUMENTATION
    └── README.md                  # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install scapy requests colorama reportlab scikit-learn pandas numpy
```

### For Mobile App (Optional)
```bash
pip install kivy
```

---

## 🎯 Usage

### 1️⃣ Terminal Version (CLI)

Quick command-line security checks:

```bash
python main.py
```

**Features:**
- Interactive password checking
- URL phishing detection
- WiFi network scanning
- Colorful terminal output

---

### 2️⃣ Desktop GUI Dashboard

Modern graphical interface:

```bash
python gui_dashboard.py
```

**Features:**
- Tab-based interface
- Password visibility toggle
- Rule-based & AI URL checking
- Real-time WiFi scanning
- PDF report generation
- Full security scan

**Screenshots:**
- 🔑 Password Check Tab
- 🔗 URL Analysis Tab
- 📡 WiFi Scanner Tab
- 📊 Results Dashboard

---

### 3️⃣ IP Address Analysis

Analyze any IP address for security risks:

**Features:**
- ✅ Geolocation (Country, City)
- ✅ ISP and Organization detection
- ✅ VPN/Proxy detection
- ✅ Risk assessment
- ✅ Blacklist checking
- ✅ Current public IP detection

**Test it:**
```bash
python ip_analyzer.py
```

**Sample Output:**
```
IP: 8.8.8.8
Country: United States
City: Ashburn
ISP: Google LLC
Risk Level: LOW
Risk Score: 0/100
```

---

### 4️⃣ AI Phishing Detection

Test the AI model:

```bash
python ai_phishing_detector.py
```

**How it works:**
1. Extracts 12 features from URL
2. Uses Random Forest classifier
3. Provides confidence score
4. Saves model for future use

**Features detected:**
- URL length & domain analysis
- HTTPS presence
- IP address usage
- Suspicious keywords
- Special characters
- Subdomain count

---

### 4️⃣ PDF Report Generator

Generate professional security reports:

```bash
python pdf_report_generator.py
```

**Report includes:**
- Overall risk assessment
- Password analysis results
- URL detection findings
- WiFi scan results
- Security recommendations
- Professional formatting

---

### 5️⃣ Mobile App

Run on desktop (testing):
```bash
python mobile_app.py
```

**Build for Android:**

1. Install Buildozer:
```bash
pip install buildozer
```

2. Initialize:
```bash
buildozer init
```

3. Build APK:
```bash
buildozer android debug
```

4. Install on device:
```bash
adb install bin/YourApp-0.1-armeabi-v7a-debug.apk
```

---

## 🧪 Testing

### Test Password Checker
```python
from password_checker import check_password
strength, score, feedback = check_password("MyP@ssw0rd!")
print(f"Strength: {strength}, Score: {score}")
```

### Test URL Detector
```python
from phishing_detector import check_url
status, score, feedback = check_url("http://login-verify-bank.com")
print(f"Status: {status}, Risk: {score}")
```

### Test AI Detection
```python
from ai_phishing_detector import AIPhishingDetector
detector = AIPhishingDetector()
status, score, confidence = detector.predict("https://suspicious-url.com")
print(f"AI Result: {status}, Confidence: {confidence}%")
```

---

## 🎓 How to Demo (For Hackathons)

### Demo Flow (5 minutes):

1. **Show Terminal Version** (1 min)
   - Enter weak password → Show "Weak" result
   - Enter suspicious URL → Show "Dangerous"

2. **Launch GUI Dashboard** (2 mins)
   - Demonstrate tabbed interface
   - Show password visibility toggle
   - Run AI phishing detection

3. **Generate PDF Report** (1 min)
   - Click "Generate PDF Report"
   - Show professional output

4. **Show Mobile App** (1 min)
   - Run on desktop or Android device
   - Demonstrate touch interface

---

## 🏆 Hackathon Winning Points

### Technical Excellence
- ✅ Multi-layered security analysis
- ✅ AI/ML integration
- ✅ Cross-platform compatibility
- ✅ Professional reporting

### User Experience
- ✅ Beginner-friendly interface
- ✅ Real-time threat detection
- ✅ Actionable recommendations
- ✅ Beautiful visual design

### Innovation
- ✅ Rule-based + AI detection
- ✅ Desktop + Mobile apps
- ✅ Automated report generation
- ✅ Extensible architecture

---

## 📊 System Architecture

```
User Input
    ↓
┌─────────────────────┐
│  Input Validation   │
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Security Modules   │
│  ├─ Password Check  │
│  ├─ URL Analysis    │
│  ├─ IP Analysis     │
│  └─ WiFi Scan       │
└─────────────────────┘
    ↓
┌─────────────────────┐
│  AI Engine (ML)     │
│  └─ Phishing Model  │
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Risk Calculator    │
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Output & Reports   │
│  ├─ CLI Output      │
│  ├─ GUI Dashboard   │
│  └─ PDF Report      │
└─────────────────────┘
```

---

## 🔮 Future Enhancements

- [ ] Real-time website monitoring
- [ ] Browser extension integration
- [ ] Cloud-based threat intelligence
- [ ] Password manager integration
- [ ] Two-factor authentication setup
- [ ] Dark web monitoring
- [ ] Email phishing detection
- [ ] Network traffic analysis

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Developer

Built with ❤️ for cybersecurity awareness

**Technologies Used:**
- Python 3.10+
- Tkinter (GUI)
- Scikit-learn (AI/ML)
- ReportLab (PDF)
- Kivy (Mobile)

---

## 🎤 Pitch Line

> "This system provides real-time, multi-layered cyber threat detection for everyday users without requiring technical knowledge."

---

## 📞 Support

For questions, issues, or feature requests, please open an issue in the repository.

---

**⭐ If you found this helpful, please star the repository!**
