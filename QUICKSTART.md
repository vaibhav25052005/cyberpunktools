# 🚀 Quick Start Guide

## ⚡ Get Started in 3 Minutes

### Step 1: Install Dependencies
```bash
pip install scapy requests colorama reportlab scikit-learn pandas numpy
```

### Step 2: Choose Your Interface

---

## 📱 Option 1: Terminal (CLI)
**Best for:** Quick checks, scripting

```bash
python main.py
```

**Features:**
- ✅ Password checking
- ✅ URL phishing detection
- ✅ WiFi scanning
- ✅ Colorful output

---

## 🖥️ Option 2: Desktop GUI
**Best for:** Visual interface, professional use

```bash
python gui_dashboard.py
```

**Features:**
- ✅ Modern tabbed interface
- ✅ Password visibility toggle
- ✅ AI-powered URL detection
- ✅ One-click PDF reports
- ✅ Full security scan

---

## 📊 Option 3: See All Features Demo
**Best for:** Hackathon presentation

```bash
python demo_all_features.py
```

**What it shows:**
- ✅ Password analysis examples
- ✅ URL detection (both methods)
- ✅ AI phishing detection
- ✅ Risk assessment
- ✅ PDF report generation

---

## 🤖 Option 4: AI Model Only
**Best for:** Testing ML capabilities

```bash
python ai_phishing_detector.py
```

---

## 📄 Option 5: PDF Report Generator
**Best for:** Generating sample report

```bash
python pdf_report_generator.py
```

---

## 📱 Option 6: Mobile App (Desktop Testing)
**Best for:** Testing mobile interface

```bash
pip install kivy
python mobile_app.py
```

### Build for Android:
```bash
pip install buildozer
buildozer init
buildozer android debug
```

---

## 🎯 Quick Test Commands

### Test Password Strength
```python
from password_checker import check_password
strength, score, feedback = check_password("YourPassword123!")
print(f"{strength} - Risk: {score}/100")
```

### Test URL Safety
```python
from phishing_detector import check_url
status, score, feedback = check_url("http://suspicious-site.com")
print(f"{status} - Risk: {score}/100")
```

### Test AI Detection
```python
from ai_phishing_detector import AIPhishingDetector
detector = AIPhishingDetector()
status, score, confidence = detector.predict("http://phishing-site.com")
print(f"{status} - Confidence: {confidence}%")
```

---

## 🎓 Hackathon Demo Script (5 Minutes)

### Minute 1: Introduction
- Open README.md
- Show project structure
- Explain the problem

### Minute 2: CLI Demo
```bash
python main.py
```
- Enter: `password123` → Show "Medium" weakness
- Enter: `http://login-verify-bank.com` → Show "Dangerous"
- Show WiFi scan results

### Minute 3: GUI Demo
```bash
python gui_dashboard.py
```
- Show tabbed interface
- Toggle password visibility
- Run AI phishing detection
- Demonstrate real-time scanning

### Minute 4: PDF Report
- Click "Generate PDF Report"
- Open the generated PDF
- Show professional formatting

### Minute 5: Mobile App & Close
```bash
python mobile_app.py
```
- Show mobile interface
- Explain Android build process
- Deliver pitch line

---

## 🏆 Winning Pitch Line

> "This system provides real-time, multi-layered cyber threat detection for everyday users without requiring technical knowledge."

---

## 📋 Checklist for Submission

- [ ] All dependencies installed
- [ ] CLI version tested
- [ ] GUI version tested
- [ ] PDF report generated
- [ ] AI model working
- [ ] Demo script runs successfully
- [ ] README reviewed
- [ ] Pitch line memorized

---

## 🆘 Troubleshooting

### Issue: Module not found
**Solution:** Run `pip install -r requirements.txt`

### Issue: GUI doesn't open
**Solution:** Make sure tkinter is installed (comes with Python)

### Issue: AI model not training
**Solution:** Check if scikit-learn is installed: `pip install scikit-learn`

### Issue: WiFi scan fails
**Solution:** Make sure WiFi is enabled and you have permissions

---

## 📞 Need Help?

Check the full README.md for detailed documentation.

**Good luck with your hackathon! 🚀**
