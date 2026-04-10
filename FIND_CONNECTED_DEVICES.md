# 📱 FIND DEVICES CONNECTED TO YOUR NETWORK

## ✅ What This Does

This feature finds **ONLY real devices** connected to YOUR WiFi/network:
- ✅ Phones (iPhone, Android)
- ✅ Laptops & Computers
- ✅ Tablets (iPad, Android tablets)
- ✅ Smart TVs
- ✅ Gaming consoles
- ✅ Smart home devices
- ✅ Routers

**Filters out:**
- ❌ System addresses
- ❌ Broadcast addresses
- ❌ Multicast addresses
- ❌ Virtual addresses

---

## 🚀 How to Use

### **Method 1: Quick Command** ⭐ EASIEST
```bash
python connected_devices.py
```

**Output:**
```
📱 DEVICES CONNECTED TO YOUR NETWORK
==========================================================
Scan Time: 2026-04-10 16:11:40
Total Devices Found: 1
==========================================================

No.   IP Address         MAC Address          Device Type
----------------------------------------------------------
1     172.32.255.254     b8:85:7b:e5:0c:9b    🌐 Router/Gateway

==========================================================

📊 DEVICE SUMMARY:
----------------------------------------------------------
  🌐 Router/Gateway: 1

✅ Found 1 real device(s) connected to your network!
💡 These are actual devices like phones, laptops, smart TVs, etc.
```

---

### **Method 2: GUI Dashboard** ⭐ BEST VISUAL
```bash
python gui_dashboard.py
```

**Steps:**
1. Click **"🔍 Network Scan"** tab
2. Click **"📱 Find My Devices"** button
3. See all connected devices in a clean table

---

### **Method 3: Full CLI Program**
```bash
python main.py
```

When asked: "Scan for connected devices? (yes/no)"
Type: `yes`

---

## 🎯 What You'll See

### **Device Information:**
- **IP Address** - Network address (e.g., 192.168.1.5)
- **MAC Address** - Physical hardware ID (unique per device)
- **Device Type** - Auto-detected (Phone, Laptop, Router, etc.)
- **Status** - Connected/Active

### **Device Types Detected:**
- 🌐 Router/Gateway
- 🍎 Apple Device (iPhone, iPad, Mac)
- 📱 Samsung Device
- 💻 Computer
- 📺 Smart TV
- 🖨️ Printer
- 📡 Connected Device (generic)

---

## 🔍 Example Scenarios

### **Scenario 1: Check Who's Using Your WiFi**
```bash
python connected_devices.py
```
**Result:** Shows 5 devices
- Your laptop
- Your phone
- Your tablet
- Roommate's phone
- Router

**If you see unknown devices** → Someone might be stealing your WiFi!

---

### **Scenario 2: Network Security Audit**
```bash
python connected_devices.py
```
**Look for:**
- Unknown MAC addresses
- Unexpected device count
- Devices you don't recognize

**Action:** Change WiFi password if you see strangers

---

### **Scenario 3: IoT Device Inventory**
```bash
python connected_devices.py
```
**Finds:**
- Smart speakers (Alexa, Google Home)
- Smart bulbs
- Security cameras
- Smart thermostat
- Connected appliances

---

## 💡 Tips for Better Results

### **1. Make Sure Devices Are Active**
- Devices need to be powered on
- Connected to same WiFi network
- Recently used (within last few minutes)

### **2. Run as Administrator** (Windows)
Right-click Command Prompt → "Run as administrator"
```bash
python connected_devices.py
```

### **3. Refresh ARP Cache**
If results seem outdated:
```bash
# Windows
arp -d
python connected_devices.py

# Linux/Mac
sudo ip neigh flush all
python connected_devices.py
```

### **4. Ping Devices First**
Make devices active by pinging:
```bash
# Windows
ping 192.168.1.1
python connected_devices.py
```

---

## 🎓 How It Works

### **Step 1: Get Your Network Info**
```python
Your IP: 172.32.4.204
Network: 172.32.4.0/24
```

### **Step 2: Read ARP Table**
Your computer keeps a cache of all devices it has communicated with:
```
IP Address       MAC Address        Type
172.32.255.254   b8:85:7b:e5:0c:9b  dynamic
```

### **Step 3: Filter Real Devices**
Removes:
- Broadcast (255.255.255.255)
- Multicast (224.x.x.x, 239.x.x.x)
- System addresses
- Virtual addresses

### **Step 4: Detect Device Type**
- Analyzes MAC address prefix
- Checks hostname
- Identifies manufacturer
- Classifies device type

### **Step 5: Display Results**
Clean table with only real, connected devices!

---

## 🔧 Technical Details

### **ARP Table Commands:**
```
Windows: arp -a
Linux:   ip neigh or arp -n
Mac:     arp -a
```

### **MAC Address Lookup:**
```python
# Apple devices start with:
00:1b:63, 3c:07:54, 40:6c:8f, etc.

# Samsung devices start with:
00:12:47, 00:16:32, 00:18:af, etc.
```

### **Filtering Logic:**
```python
# Remove multicast
if ip.startswith('224.') or ip.startswith('239.'):
    return False

# Remove broadcast
if ip.endswith('.255'):
    return False

# Remove multicast MAC
if mac.startswith('01:00:5e'):
    return False
```

---

## 🎬 Demo Script (For Hackathon)

### **Quick Demo (1 minute):**
```bash
# Run scanner
python connected_devices.py

# Say: "I just scanned my network and found X devices"
# Show the clean table
# Explain: "This filters out system addresses to show only real devices"
# Mention: "You can detect unauthorized WiFi users"
```

### **Full Demo (3 minutes):**
```bash
# 1. Show GUI
python gui_dashboard.py

# 2. Click "Network Scan" tab

# 3. Click "Find My Devices"

# 4. Explain the results:
#    - "Found X devices on my network"
#    - "Each has unique IP and MAC address"
#    - "Device type is auto-detected"
#    - "Helps identify unauthorized access"

# 5. Show device summary:
#    - "X routers"
#    - "Y phones"
#    - "Z laptops"
```

---

## 🎓 Viva Answers

### **Q: How does it find connected devices?**
**A:** "It reads the ARP (Address Resolution Protocol) table from the operating system. This table contains IP-to-MAC address mappings for all devices your computer has recently communicated with on the local network."

### **Q: How do you filter only real devices?**
**A:** "We filter out multicast addresses (224.x.x.x and 239.x.x.x), broadcast addresses (ending in .255), and multicast MAC addresses (starting with 01:00:5e). This leaves only actual physical devices like phones, laptops, and routers."

### **Q: Can you detect what type of device it is?**
**A:** "Yes! We analyze the MAC address prefix to identify the manufacturer. For example, Apple devices have specific MAC prefixes, as do Samsung devices. We also check hostnames for clues like 'iPhone' or 'Android'."

### **Q: Why is this useful for cybersecurity?**
**A:** "It helps detect unauthorized access to your network. If you see unknown devices, someone might be using your WiFi without permission. It's essential for network security audits and monitoring."

---

## 📊 Your Results Explained

**Example Output:**
```
Found 1 real device(s) connected to your network!

Device: 172.32.255.254
Type: 🌐 Router/Gateway
MAC: b8:85:7b:e5:0c:9b
```

**This means:**
- 1 device found (your router)
- Other devices may not be active yet
- Try browsing on other devices, then scan again

---

## 🔥 Pro Tips

### **To Find More Devices:**
1. Make sure other devices are connected to WiFi
2. Use those devices (browse, stream, etc.)
3. Run the scanner immediately after
4. Devices will appear in ARP cache

### **For Best Demo:**
1. Connect 2-3 phones/laptops to your WiFi
2. Browse on them for 1 minute
3. Run: `python connected_devices.py`
4. Show all devices in the table
5. Say: "I can see every device on my network!"

---

## 📁 Files Created

- ✅ `connected_devices.py` - Standalone scanner
- ✅ Updated `gui_dashboard.py` - Added "Find My Devices" button
- ✅ Updated `main.py` - Integrated into CLI

---

## 🚀 Quick Commands

### **Fastest Way:**
```bash
python connected_devices.py
```

### **GUI Way:**
```bash
python gui_dashboard.py
# Click "🔍 Network Scan" → "📱 Find My Devices"
```

### **Full System:**
```bash
python main.py
# Answer "yes" to network scan
```

---

## ✅ Summary

**What it does:**
- ✅ Finds ALL devices on your WiFi
- ✅ Shows IP and MAC addresses
- ✅ Detects device types
- ✅ Filters out system addresses
- ✅ Clean, readable output

**Why it's useful:**
- ✅ Detect unauthorized WiFi users
- ✅ Network security monitoring
- ✅ Device inventory
- ✅ IT troubleshooting

**Perfect for:**
- ✅ Home network monitoring
- ✅ Office security
- ✅ Hackathon demos
- ✅ Cybersecurity projects

---

**🏆 Now you can see EXACTLY what's connected to your network!**
