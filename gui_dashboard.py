import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import filedialog
import threading
from datetime import datetime

from password_checker import check_password
from phishing_detector import check_url
from ai_phishing_detector import AIPhishingDetector
from wifi_scanner import scan_wifi
from ip_analyzer import IPAnalyzer
from network_scanner import NetworkDeviceScanner
from connected_devices import ConnectedDevicesScanner
from enhanced_ip_scanner import EnhancedIPScanner
from risk_engine import calculate_risk
from pdf_report_generator import PDFReportGenerator
from password_recovery_guide import PasswordRecoveryGuide
from ethical_cybersecurity_framework import EthicalCybersecurityFramework
from email_phishing_detector import EmailPhishingDetector
from password_generator import PasswordGenerator

class CyberSecurityDashboard:
    """Modern GUI Dashboard for Cyber Security Assistant"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Personal Cyber Security Assistant")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Configure style
        self.setup_style()
        
        # Initialize AI detector
        self.ai_detector = AIPhishingDetector()
        
        # Initialize IP analyzer
        self.ip_analyzer = IPAnalyzer()
        
        # Initialize network scanner
        self.network_scanner = NetworkDeviceScanner()
        
        # Initialize connected devices scanner
        self.connected_scanner = ConnectedDevicesScanner()
        
        # Initialize enhanced IP scanner
        self.enhanced_scanner = EnhancedIPScanner()
        
        # Initialize email phishing detector
        self.email_detector = EmailPhishingDetector()
        
        # Initialize password generator
        self.password_generator = PasswordGenerator()
        
        # Store results
        self.results = {
            'password': {},
            'url': {},
            'wifi': {},
            'ip': {},
            'email': {},
            'risk_level': '',
            'recommendations': []
        }
        
        # Build UI
        self.create_widgets()
        
    def setup_style(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', font=('Segoe UI', 24, 'bold'), foreground='#1a73e8')
        style.configure('Subtitle.TLabel', font=('Segoe UI', 11), foreground='#5f6368')
        style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'), foreground='#202124')
        style.configure('Result.TLabel', font=('Segoe UI', 11), foreground='#202124')
        style.configure('Success.TLabel', foreground='#00C851')
        style.configure('Warning.TLabel', foreground='#ffbb33')
        style.configure('Danger.TLabel', foreground='#ff4444')
        
        style.configure('TButton', font=('Segoe UI', 10), padding=10)
        style.configure('Primary.TButton', font=('Segoe UI', 10, 'bold'), padding=10)
        
    def create_widgets(self):
        """Create all UI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Title
        title_frame = ttk.Frame(main_frame)
        title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(title_frame, text="🔐 Cyber Security Assistant", 
                 style='Title.TLabel').pack()
        ttk.Label(title_frame, text="Protecting your digital world, one scan at a time!", 
                 style='Subtitle.TLabel').pack()
        
        # Tab control
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        main_frame.rowconfigure(1, weight=1)
        
        # Create tabs
        self.create_password_tab()
        self.create_url_tab()
        self.create_ip_tab()
        self.create_network_tab()
        self.create_wifi_tab()
        self.create_email_phishing_tab()
        self.create_password_generator_tab()
        self.create_recovery_tab()
        self.create_ethics_tab()
        self.create_results_tab()
        
        # Action buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=20)
        
        ttk.Button(button_frame, text="🚀 Run Full Security Scan", 
                  command=self.run_full_scan, style='Primary.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="📊 Generate PDF Report", 
                  command=self.generate_pdf_report).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🔄 Clear All", 
                  command=self.clear_all).pack(side=tk.LEFT, padx=5)
        
    def create_password_tab(self):
        """Password strength check tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="🔑 Password Check")
        
        ttk.Label(tab, text="Password Strength Analyzer", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        # Input frame
        input_frame = ttk.Frame(tab)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="Enter Password:").pack(side=tk.LEFT, padx=(0, 10))
        self.password_entry = ttk.Entry(input_frame, width=40, show="*")
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(input_frame, text="👁️ Show", 
                  command=self.toggle_password).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(input_frame, text="✓ Check", 
                  command=self.check_password).pack(side=tk.LEFT, padx=(5, 0))
        
        # Result frame
        self.password_result_frame = ttk.LabelFrame(tab, text="Analysis Result", padding="10")
        self.password_result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.password_result_text = scrolledtext.ScrolledText(
            self.password_result_frame, height=15, font=('Consolas', 10)
        )
        self.password_result_text.pack(fill=tk.BOTH, expand=True)
        
    def create_url_tab(self):
        """URL phishing detection tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="🔗 URL Check")
        
        ttk.Label(tab, text="AI-Powered Phishing Detection", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        # Input frame
        input_frame = ttk.Frame(tab)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="Enter URL:").pack(side=tk.LEFT, padx=(0, 10))
        self.url_entry = ttk.Entry(input_frame, width=50)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(input_frame, text="🔍 Check (Rule-Based)", 
                  command=self.check_url_rule).pack(side=tk.LEFT, padx=5)
        ttk.Button(input_frame, text="🧠 Check (AI)", 
                  command=self.check_url_ai).pack(side=tk.LEFT, padx=5)
        
        # Result frame
        self.url_result_frame = ttk.LabelFrame(tab, text="Analysis Result", padding="10")
        self.url_result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.url_result_text = scrolledtext.ScrolledText(
            self.url_result_frame, height=15, font=('Consolas', 10)
        )
        self.url_result_text.pack(fill=tk.BOTH, expand=True)
    
    def create_ip_tab(self):
        """IP Address Analysis tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="🌐 IP Analysis")
        
        ttk.Label(tab, text="IP Address Security Analysis", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        # Input frame
        input_frame = ttk.Frame(tab)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="Enter IP:").pack(side=tk.LEFT, padx=(0, 10))
        self.ip_entry = ttk.Entry(input_frame, width=30)
        self.ip_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(input_frame, text="🔍 Analyze IP", 
                  command=self.analyze_ip).pack(side=tk.LEFT, padx=5)
        ttk.Button(input_frame, text="📡 Get My IP", 
                  command=self.get_my_ip).pack(side=tk.LEFT, padx=5)
        
        # Result frame
        self.ip_result_frame = ttk.LabelFrame(tab, text="Analysis Result", padding="10")
        self.ip_result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.ip_result_text = scrolledtext.ScrolledText(
            self.ip_result_frame, height=18, font=('Consolas', 10)
        )
        self.ip_result_text.pack(fill=tk.BOTH, expand=True)
    
    def create_network_tab(self):
        """Network Device Scanner tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="🔍 Network Scan")
        
        ttk.Label(tab, text="Connected Devices Scanner", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        # Info frame
        info_frame = ttk.Frame(tab)
        info_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(info_frame, text="Scan your network to find all connected devices",
                 style='Subtitle.TLabel').pack()
        
        # Button frame
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="🔍 Find All IPs", 
                  command=self.find_all_ips).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📱 Find My Devices", 
                  command=self.find_connected_devices).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🔍 Scan Network", 
                  command=self.scan_network).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📊 Quick Scan", 
                  command=self.quick_scan).pack(side=tk.LEFT, padx=5)
        
        # Result frame
        self.network_result_frame = ttk.LabelFrame(tab, text="Scan Results", padding="10")
        self.network_result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.network_result_text = scrolledtext.ScrolledText(
            self.network_result_frame, height=22, font=('Consolas', 10)
        )
        self.network_result_text.pack(fill=tk.BOTH, expand=True)
        
    def create_wifi_tab(self):
        """WiFi scanner tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="📡 WiFi Scanner")
        
        ttk.Label(tab, text="Available WiFi Networks", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        # Button frame
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="📡 Scan Networks", 
                  command=self.scan_wifi_networks).pack(side=tk.LEFT)
        
        # Result frame
        self.wifi_result_frame = ttk.LabelFrame(tab, text="Scan Results", padding="10")
        self.wifi_result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.wifi_result_text = scrolledtext.ScrolledText(
            self.wifi_result_frame, height=20, font=('Consolas', 10)
        )
        self.wifi_result_text.pack(fill=tk.BOTH, expand=True)
    
    def create_email_phishing_tab(self):
        """Email phishing detection tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="📧 Email Phishing")
        
        ttk.Label(tab, text="Email Phishing Detection", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        # Input frame
        input_frame = ttk.LabelFrame(tab, text="Email Details", padding="10")
        input_frame.pack(fill=tk.X, pady=10)
        
        # Subject
        ttk.Label(input_frame, text="Subject:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.email_subject_entry = ttk.Entry(input_frame, width=60)
        self.email_subject_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Sender
        ttk.Label(input_frame, text="Sender:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.email_sender_entry = ttk.Entry(input_frame, width=60)
        self.email_sender_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Body
        ttk.Label(input_frame, text="Body:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.email_body_text = scrolledtext.ScrolledText(input_frame, height=6, width=60)
        self.email_body_text.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Links
        ttk.Label(input_frame, text="Links (comma-separated):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.email_links_entry = ttk.Entry(input_frame, width=60)
        self.email_links_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Attachments
        ttk.Label(input_frame, text="Attachments (comma-separated):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.email_attachments_entry = ttk.Entry(input_frame, width=60)
        self.email_attachments_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        input_frame.columnconfigure(1, weight=1)
        
        # Button frame
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="🔍 Analyze Email", 
                  command=self.analyze_email).pack(side=tk.LEFT)
        
        # Result frame
        self.email_result_frame = ttk.LabelFrame(tab, text="Analysis Results", padding="10")
        self.email_result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.email_result_text = scrolledtext.ScrolledText(
            self.email_result_frame, height=15, font=('Consolas', 10)
        )
        self.email_result_text.pack(fill=tk.BOTH, expand=True)
    
    def create_password_generator_tab(self):
        """Password generator tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="🔐 Password Gen")
        
        ttk.Label(tab, text="Secure Password Generator & Manager", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        # Options frame
        options_frame = ttk.LabelFrame(tab, text="Password Options", padding="10")
        options_frame.pack(fill=tk.X, pady=10)
        
        # Length
        length_frame = ttk.Frame(options_frame)
        length_frame.pack(fill=tk.X, pady=5)
        ttk.Label(length_frame, text="Length:").pack(side=tk.LEFT, padx=(0, 10))
        self.pwd_length_var = tk.StringVar(value="16")
        ttk.Spinbox(length_frame, from_=8, to=64, textvariable=self.pwd_length_var, width=10).pack(side=tk.LEFT)
        
        # Character options
        char_frame = ttk.Frame(options_frame)
        char_frame.pack(fill=tk.X, pady=5)
        
        self.pwd_upper_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(char_frame, text="Uppercase (A-Z)", variable=self.pwd_upper_var).pack(side=tk.LEFT, padx=5)
        
        self.pwd_lower_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(char_frame, text="Lowercase (a-z)", variable=self.pwd_lower_var).pack(side=tk.LEFT, padx=5)
        
        self.pwd_digits_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(char_frame, text="Digits (0-9)", variable=self.pwd_digits_var).pack(side=tk.LEFT, padx=5)
        
        self.pwd_symbols_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(char_frame, text="Symbols (!@#$)", variable=self.pwd_symbols_var).pack(side=tk.LEFT, padx=5)
        
        # Generate button
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="🔑 Generate Password", 
                  command=self.generate_password).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📝 Generate Passphrase", 
                  command=self.generate_passphrase).pack(side=tk.LEFT, padx=5)
        
        # Generated password display
        pwd_display_frame = ttk.LabelFrame(tab, text="Generated Password", padding="10")
        pwd_display_frame.pack(fill=tk.X, pady=10)
        
        self.generated_pwd_text = tk.Text(pwd_display_frame, height=3, font=('Consolas', 14), wrap=tk.WORD)
        self.generated_pwd_text.pack(fill=tk.X, pady=5)
        
        # Strength info
        self.pwd_strength_label = ttk.Label(pwd_display_frame, text="", style='Result.TLabel')
        self.pwd_strength_label.pack(anchor=tk.W, pady=5)
        
        # Store password frame
        store_frame = ttk.LabelFrame(tab, text="Store Password (Encrypted)", padding="10")
        store_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(store_frame, text="Service:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.store_service_entry = ttk.Entry(store_frame, width=30)
        self.store_service_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(store_frame, text="Username:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.store_username_entry = ttk.Entry(store_frame, width=30)
        self.store_username_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(store_frame, text="URL (optional):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.store_url_entry = ttk.Entry(store_frame, width=30)
        self.store_url_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Button(store_frame, text="💾 Store Password", 
                  command=self.store_generated_password).grid(row=3, column=1, sticky=tk.W, pady=10)
        
        # Password health check
        health_frame = ttk.LabelFrame(tab, text="Password Health", padding="10")
        health_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        ttk.Button(health_frame, text="📊 Check Password Health", 
                  command=self.check_password_health).pack(pady=5)
        
        self.pwd_health_text = scrolledtext.ScrolledText(
            health_frame, height=10, font=('Consolas', 10)
        )
        self.pwd_health_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
    def analyze_email(self):
        """Analyze email for phishing"""
        subject = self.email_subject_entry.get()
        sender = self.email_sender_entry.get()
        body = self.email_body_text.get(1.0, tk.END).strip()
        
        links_input = self.email_links_entry.get()
        links = [link.strip() for link in links_input.split(',')] if links_input else []
        
        attachments_input = self.email_attachments_entry.get()
        attachments = [att.strip() for att in attachments_input.split(',')] if attachments_input else []
        
        if not subject and not sender and not body:
            messagebox.showwarning("Warning", "Please enter at least subject, sender, or body")
            return
        
        # Run analysis in thread to avoid freezing UI
        def analyze_thread():
            result = self.email_detector.analyze_email(
                subject=subject,
                sender=sender,
                body=body,
                links=links,
                attachments=attachments
            )
            
            self.results['email'] = result
            
            # Update UI
            self.root.after(0, lambda: self.display_email_result(result))
        
        threading.Thread(target=analyze_thread, daemon=True).start()
    
    def display_email_result(self, result):
        """Display email analysis result"""
        self.email_result_text.delete(1.0, tk.END)
        
        risk = result.get('Overall Risk', 'UNKNOWN')
        score = result.get('Risk Score', 0)
        
        self.email_result_text.insert(tk.END, f"Overall Risk: {risk}\n")
        self.email_result_text.insert(tk.END, f"Risk Score: {score}/100\n")
        self.email_result_text.insert(tk.END, f"Timestamp: {result.get('Timestamp', '')}\n\n")
        
        warnings = result.get('Warnings', [])
        if warnings:
            self.email_result_text.insert(tk.END, "⚠️ WARNINGS:\n")
            for warning in warnings:
                self.email_result_text.insert(tk.END, f"  • {warning}\n")
        else:
            self.email_result_text.insert(tk.END, "✅ No warnings detected\n")
    
    def generate_password(self):
        """Generate secure password"""
        try:
            length = int(self.pwd_length_var.get())
            if length < 8 or length > 64:
                messagebox.showwarning("Warning", "Password length must be between 8 and 64")
                return
            
            password, strength_info = self.password_generator.generate_password(
                length=length,
                use_uppercase=self.pwd_upper_var.get(),
                use_lowercase=self.pwd_lower_var.get(),
                use_digits=self.pwd_digits_var.get(),
                use_symbols=self.pwd_symbols_var.get()
            )
            
            # Display password
            self.generated_pwd_text.delete(1.0, tk.END)
            self.generated_pwd_text.insert(1.0, password)
            
            # Display strength
            strength_text = f"Strength: {strength_info['Strength']} | Score: {strength_info['Score']}/100 | Crack Time: {strength_info['Crack Time']}"
            self.pwd_strength_label.config(text=strength_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate password: {str(e)}")
    
    def generate_passphrase(self):
        """Generate memorable passphrase"""
        try:
            passphrase, strength_info = self.password_generator.generate_passphrase(
                num_words=6,
                capitalize=True,
                add_number=True
            )
            
            # Display passphrase
            self.generated_pwd_text.delete(1.0, tk.END)
            self.generated_pwd_text.insert(1.0, passphrase)
            
            # Display strength
            strength_text = f"Strength: {strength_info['Strength']} | Score: {strength_info['Score']}/100 | Crack Time: {strength_info['Crack Time']}"
            self.pwd_strength_label.config(text=strength_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate passphrase: {str(e)}")
    
    def store_generated_password(self):
        """Store generated password"""
        password = self.generated_pwd_text.get(1.0, tk.END).strip()
        service = self.store_service_entry.get()
        username = self.store_username_entry.get()
        url = self.store_url_entry.get()
        
        if not password:
            messagebox.showwarning("Warning", "Please generate a password first")
            return
        
        if not service or not username:
            messagebox.showwarning("Warning", "Please enter service name and username")
            return
        
        try:
            self.password_generator.store_password(service, username, password, url)
            messagebox.showinfo("Success", "Password stored securely!")
            
            # Clear fields
            self.store_service_entry.delete(0, tk.END)
            self.store_username_entry.delete(0, tk.END)
            self.store_url_entry.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to store password: {str(e)}")
    
    def check_password_health(self):
        """Check health of stored passwords"""
        try:
            health_report = self.password_generator.check_password_health()
            
            self.pwd_health_text.delete(1.0, tk.END)
            
            if 'Status' in health_report:
                self.pwd_health_text.insert(tk.END, f"Status: {health_report['Status']}\n")
                return
            
            self.pwd_health_text.insert(tk.END, f"Total Passwords: {health_report['Total']}\n")
            self.pwd_health_text.insert(tk.END, f"Strong: {health_report['Strong']}\n")
            self.pwd_health_text.insert(tk.END, f"Moderate: {health_report['Moderate']}\n")
            self.pwd_health_text.insert(tk.END, f"Weak: {health_report['Weak']}\n")
            self.pwd_health_text.insert(tk.END, f"Duplicates: {health_report['Duplicate Passwords']}\n")
            self.pwd_health_text.insert(tk.END, f"Short Passwords: {health_report['Short Passwords']}\n\n")
            
            if health_report.get('Recommendations'):
                self.pwd_health_text.insert(tk.END, "Recommendations:\n")
                for rec in health_report['Recommendations']:
                    self.pwd_health_text.insert(tk.END, f"  • {rec}\n")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to check password health: {str(e)}")
        
    def create_results_tab(self):
        """Overall results tab"""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="📊 Results")
        
        ttk.Label(tab, text="Security Assessment Summary", 
                 style='Header.TLabel').pack(anchor=tk.W, pady=(0, 10))
        
        self.overall_result_text = scrolledtext.ScrolledText(
            tab, height=30, font=('Consolas', 10)
        )
        self.overall_result_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
    def toggle_password(self):
        """Toggle password visibility"""
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
    
    def check_password(self):
        """Check password strength"""
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password")
            return
        
        strength, score, feedback = check_password(password)
        
        self.results['password'] = {
            'strength': strength,
            'score': score,
            'feedback': feedback
        }
        
        # Display results
        self.password_result_text.delete(1.0, tk.END)
        self.password_result_text.insert(tk.END, f"Password Strength: {strength}\n")
        self.password_result_text.insert(tk.END, f"Risk Score: {score}/100\n\n")
        
        if feedback:
            self.password_result_text.insert(tk.END, "Suggestions:\n")
            for item in feedback:
                self.password_result_text.insert(tk.END, f"  • {item}\n")
        
    def check_url_rule(self):
        """Check URL using rule-based method"""
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL")
            return
        
        status, score, feedback = check_url(url)
        
        self.results['url'] = {
            'status': status,
            'score': score,
            'feedback': feedback,
            'method': 'Rule-Based'
        }
        
        # Display results
        self.url_result_text.delete(1.0, tk.END)
        self.url_result_text.insert(tk.END, f"URL Status: {status}\n")
        self.url_result_text.insert(tk.END, f"Risk Score: {score}/100\n")
        self.url_result_text.insert(tk.END, f"Method: Rule-Based\n\n")
        
        if feedback:
            self.url_result_text.insert(tk.END, "Warnings:\n")
            for item in feedback:
                self.url_result_text.insert(tk.END, f"  • {item}\n")
    
    def check_url_ai(self):
        """Check URL using AI model"""
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL")
            return
        
        # Run in thread to avoid freezing UI
        def ai_check():
            status, score, confidence = self.ai_detector.predict(url)
            
            self.results['url'] = {
                'status': status,
                'score': score,
                'feedback': [f"AI Confidence: {confidence:.1f}%"],
                'method': 'AI-Powered'
            }
            
            # Update UI
            self.url_result_text.delete(1.0, tk.END)
            self.url_result_text.insert(tk.END, f"URL Status: {status}\n")
            self.url_result_text.insert(tk.END, f"Risk Score: {score}/100\n")
            self.url_result_text.insert(tk.END, f"Method: AI-Powered (Random Forest)\n")
            self.url_result_text.insert(tk.END, f"Confidence: {confidence:.1f}%\n\n")
        
        thread = threading.Thread(target=ai_check, daemon=True)
        thread.start()
    
    def scan_wifi_networks(self):
        """Scan WiFi networks"""
        self.wifi_result_text.delete(1.0, tk.END)
        self.wifi_result_text.insert(tk.END, "Scanning WiFi networks...\n")
        
        def scan():
            wifi_data, error = scan_wifi()
            
            if error:
                self.wifi_result_text.delete(1.0, tk.END)
                self.wifi_result_text.insert(tk.END, f"Error: {error}\n")
                self.results['wifi'] = {'data': '', 'error': error}
            else:
                self.wifi_result_text.delete(1.0, tk.END)
                self.wifi_result_text.insert(tk.END, wifi_data)
                self.results['wifi'] = {'data': wifi_data, 'error': None}
        
        thread = threading.Thread(target=scan, daemon=True)
        thread.start()
    
    def analyze_ip(self):
        """Analyze IP address"""
        ip = self.ip_entry.get()
        if not ip:
            messagebox.showwarning("Warning", "Please enter an IP address")
            return
        
        self.ip_result_text.delete(1.0, tk.END)
        self.ip_result_text.insert(tk.END, f"Analyzing IP: {ip}...\n")
        
        def analyze():
            result = self.ip_analyzer.check_ip(ip)
            
            self.results['ip'] = result
            
            # Display results
            self.ip_result_text.delete(1.0, tk.END)
            
            if result.get("Status") == "Success":
                self.ip_result_text.insert(tk.END, f"IP Address: {result['IP']}\n")
                self.ip_result_text.insert(tk.END, f"Country: {result['Country']}\n")
                self.ip_result_text.insert(tk.END, f"City: {result['City']}\n")
                self.ip_result_text.insert(tk.END, f"Region: {result['Region']}\n")
                self.ip_result_text.insert(tk.END, f"ISP: {result['ISP']}\n")
                self.ip_result_text.insert(tk.END, f"Organization: {result['Organization']}\n")
                self.ip_result_text.insert(tk.END, f"Coordinates: {result['Coordinates']}\n")
                self.ip_result_text.insert(tk.END, f"Timezone: {result['Timezone']}\n\n")
                self.ip_result_text.insert(tk.END, f"Risk Level: {result['Risk Level']}\n")
                self.ip_result_text.insert(tk.END, f"Risk Score: {result['Risk Score']}/100\n")
                self.ip_result_text.insert(tk.END, f"Blacklisted: {result['Blacklisted']}\n\n")
                
                if result.get("Warnings"):
                    self.ip_result_text.insert(tk.END, "Warnings:\n")
                    for warning in result["Warnings"]:
                        self.ip_result_text.insert(tk.END, f"  • {warning}\n")
            else:
                self.ip_result_text.insert(tk.END, f"Error: {result.get('Error', 'Unknown')}\n")
        
        thread = threading.Thread(target=analyze, daemon=True)
        thread.start()
    
    def get_my_ip(self):
        """Get and analyze current public IP"""
        self.ip_result_text.delete(1.0, tk.END)
        self.ip_result_text.insert(tk.END, "Fetching your public IP...\n")
        
        def fetch_and_analyze():
            public_ip = self.ip_analyzer.get_public_ip()
            self.ip_entry.delete(0, tk.END)
            self.ip_entry.insert(0, public_ip)
            
            self.ip_result_text.delete(1.0, tk.END)
            self.ip_result_text.insert(tk.END, f"Your Public IP: {public_ip}\n\n")
            self.ip_result_text.insert(tk.END, "Analyzing...\n")
            
            result = self.ip_analyzer.check_ip(public_ip)
            self.results['ip'] = result
            
            if result.get("Status") == "Success":
                self.ip_result_text.insert(tk.END, f"Country: {result['Country']}\n")
                self.ip_result_text.insert(tk.END, f"City: {result['City']}\n")
                self.ip_result_text.insert(tk.END, f"ISP: {result['ISP']}\n")
                self.ip_result_text.insert(tk.END, f"Risk Level: {result['Risk Level']}\n")
                self.ip_result_text.insert(tk.END, f"Risk Score: {result['Risk Score']}/100\n")
                
                if result.get("Warnings"):
                    self.ip_result_text.insert(tk.END, "\nWarnings:\n")
                    for warning in result["Warnings"]:
                        self.ip_result_text.insert(tk.END, f"  • {warning}\n")
            else:
                self.ip_result_text.insert(tk.END, f"Error: {result.get('Error', 'Unknown')}\n")
        
        thread = threading.Thread(target=fetch_and_analyze, daemon=True)
        thread.start()
    
    def scan_network(self):
        """Full network scan for connected devices"""
        self.network_result_text.delete(1.0, tk.END)
        self.network_result_text.insert(tk.END, "🔍 Starting full network scan...\n")
        self.network_result_text.insert(tk.END, "This may take a few seconds...\n\n")
        
        def scan():
            result = self.network_scanner.scan_all_devices()
            formatted = self.network_scanner.format_results(result)
            
            self.results['network'] = result
            
            self.network_result_text.delete(1.0, tk.END)
            self.network_result_text.insert(tk.END, formatted)
            
            if result.get('Devices'):
                self.network_result_text.insert(tk.END, f"\n\n✅ Found {result['Total Devices']} device(s)!")
        
        thread = threading.Thread(target=scan, daemon=True)
        thread.start()
    
    def find_connected_devices(self):
        """Find ONLY real devices connected to your network"""
        self.network_result_text.delete(1.0, tk.END)
        self.network_result_text.insert(tk.END, "📱 Finding devices connected to YOUR network...\n")
        self.network_result_text.insert(tk.END, "Filtering out system addresses...\n\n")
        
        def find():
            devices = self.connected_scanner.scan_connected_devices()
            
            if devices:
                formatted = self.connected_scanner.format_devices_table(devices)
                self.network_result_text.delete(1.0, tk.END)
                self.network_result_text.insert(tk.END, formatted)
                self.network_result_text.insert(tk.END, f"\n\n✅ Found {len(devices)} real device(s)!")
                self.network_result_text.insert(tk.END, "\n💡 These are actual devices like phones, laptops, smart TVs, etc.")
            else:
                self.network_result_text.delete(1.0, tk.END)
                self.network_result_text.insert(tk.END, "⚠️ No devices found.\n\n")
                self.network_result_text.insert(tk.END, "Tips:\n")
                self.network_result_text.insert(tk.END, "• Make sure other devices are connected to your WiFi\n")
                self.network_result_text.insert(tk.END, "• Try running as administrator\n")
                self.network_result_text.insert(tk.END, "• Other devices need to be active on the network\n")
        
        thread = threading.Thread(target=find, daemon=True)
        thread.start()
    
    def find_all_ips(self):
        """Enhanced scan to find ALL IP addresses on network"""
        self.network_result_text.delete(1.0, tk.END)
        self.network_result_text.insert(tk.END, "🔍 Enhanced IP Discovery Mode\n")
        self.network_result_text.insert(tk.END, "Scanning all 254 addresses in your network...\n")
        self.network_result_text.insert(tk.END, "This will take 30-60 seconds...\n\n")
        
        def scan():
            devices = self.enhanced_scanner.scan_network_complete()
            
            if devices:
                your_ip = self.enhanced_scanner.get_local_ip()
                formatted = self.enhanced_scanner.format_results(devices, your_ip)
                self.network_result_text.delete(1.0, tk.END)
                self.network_result_text.insert(tk.END, formatted)
                self.network_result_text.insert(tk.END, f"\n\n✅ Successfully found {len(devices)} device(s)!")
                self.network_result_text.insert(tk.END, "\n💡 This scan actively pinged all IP addresses in your network range")
            else:
                self.network_result_text.delete(1.0, tk.END)
                self.network_result_text.insert(tk.END, "⚠️ No devices found. Try running as administrator.")
        
        thread = threading.Thread(target=scan, daemon=True)
        thread.start()
    
    def quick_scan(self):
        """Quick ping scan for common devices"""
        self.network_result_text.delete(1.0, tk.END)
        self.network_result_text.insert(tk.END, "📊 Quick scan for common devices...\n\n")
        
        def quick():
            local_ip = self.network_scanner.get_local_ip()
            _, network_range = self.network_scanner.get_network_range()
            
            self.network_result_text.insert(tk.END, f"Local IP: {local_ip}\n")
            self.network_result_text.insert(tk.END, f"Network: {network_range}.0/24\n\n")
            self.network_result_text.insert(tk.END, "Pinging common IPs...\n\n")
            
            devices = self.network_scanner.ping_scan(network_range)
            
            self.network_result_text.insert(tk.END, f"{'IP Address':<20} {'Status':<12}\n")
            self.network_result_text.insert(tk.END, "-"*40 + "\n")
            
            for device in devices:
                self.network_result_text.insert(tk.END, f"{device['IP']:<20} {device['Status']:<12}\n")
            
            self.network_result_text.insert(tk.END, f"\n✅ Found {len(devices)} online device(s)!")
        
        thread = threading.Thread(target=quick, daemon=True)
        thread.start()
    
    def run_full_scan(self):
        """Run complete security scan"""
        self.check_password()
        if self.url_entry.get():
            self.check_url_ai()
        if self.ip_entry.get():
            self.analyze_ip()
        self.scan_wifi_networks()
        
        # Calculate overall risk
        scores = []
        if self.results['password'].get('score'):
            scores.append(self.results['password']['score'])
        if self.results['url'].get('score'):
            scores.append(self.results['url']['score'])
        if self.results.get('ip', {}).get('Risk Score'):
            scores.append(self.results['ip']['Risk Score'])
        
        if scores:
            risk_level, recommendations = calculate_risk(scores)
            self.results['risk_level'] = risk_level
            self.results['recommendations'] = recommendations
            
            # Display overall results
            self.overall_result_text.delete(1.0, tk.END)
            self.overall_result_text.insert(tk.END, "="*60 + "\n")
            self.overall_result_text.insert(tk.END, "OVERALL SECURITY ASSESSMENT\n")
            self.overall_result_text.insert(tk.END, "="*60 + "\n\n")
            self.overall_result_text.insert(tk.END, f"Risk Level: {risk_level}\n\n")
            self.overall_result_text.insert(tk.END, "Recommendations:\n")
            for i, rec in enumerate(recommendations, 1):
                self.overall_result_text.insert(tk.END, f"  {i}. {rec}\n")
            
            messagebox.showinfo("Scan Complete", "Full security scan completed!")
    
    def generate_pdf_report(self):
        """Generate PDF report"""
        if not self.results.get('password') and not self.results.get('url'):
            messagebox.showwarning("Warning", "Please run at least one security check first")
            return
        
        # Ask for save location
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )
        
        if filename:
            try:
                generator = PDFReportGenerator(filename)
                generator.generate_report(self.results)
                messagebox.showinfo("Success", f"PDF report saved to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate report:\n{str(e)}")
    
    def create_recovery_tab(self):
        """Create Password Recovery tab"""
        recovery_frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(recovery_frame, text='🔐 Recovery')
        
        # Title
        title = tk.Label(
            recovery_frame,
            text="🔐 Legal Password Recovery Guide",
            font=('Segoe UI', 16, 'bold')
        )
        title.pack(pady=(0, 10))
        
        # Disclaimer
        disclaimer = tk.Label(
            recovery_frame,
            text="⚠️ Only use these methods on devices YOU legally own",
            font=('Segoe UI', 10),
            fg='red'
        )
        disclaimer.pack(pady=(0, 10))
        
        # Device selection
        device_frame = tk.LabelFrame(recovery_frame, text="Select Your Device", font=('Segoe UI', 11, 'bold'))
        device_frame.pack(fill=tk.X, pady=10, padx=15)
        
        # Buttons for each device type
        button_frame = tk.Frame(device_frame)
        button_frame.pack(fill=tk.X)
        
        tk.Button(button_frame, text="🤖 Android", command=self.show_android_recovery, 
                 bg='#FF9800', fg='white', font=('Segoe UI', 10, 'bold'), width=15).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="🍎 iPhone", command=self.show_iphone_recovery, 
                 bg='#9C27B0', fg='white', font=('Segoe UI', 10, 'bold'), width=15).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="💻 Windows", command=self.show_windows_recovery, 
                 bg='#2196F3', fg='white', font=('Segoe UI', 10, 'bold'), width=15).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="📋 General Tips", command=self.show_general_tips, 
                 bg='#4CAF50', fg='white', font=('Segoe UI', 10, 'bold'), width=15).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Result area
        self.recovery_result_text = scrolledtext.ScrolledText(
            recovery_frame,
            height=20,
            font=('Consolas', 10),
            wrap=tk.WORD
        )
        self.recovery_result_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Initialize recovery guide
        self.recovery_guide = PasswordRecoveryGuide()
    
    def show_android_recovery(self):
        """Show Android recovery methods"""
        self.recovery_result_text.delete(1.0, tk.END)
        self.recovery_result_text.insert(tk.END, "🤖 ANDROID PASSWORD RECOVERY (LEGAL METHODS)\n")
        self.recovery_result_text.insert(tk.END, "="*70 + "\n\n")
        
        methods = [
            ("Method 1: Google Find My Device",
             "Data Loss: ⚠️ YES | Difficulty: Easy\n\n"
             "Steps:\n"
             "1. Visit: google.com/android/find\n"
             "2. Sign in with your Google account\n"
             "3. Select your locked device\n"
             "4. Click 'Erase Device'\n"
             "5. Device will be reset to factory settings\n"
             "6. Set up device again with new password\n"
             "7. Restore data from Google backup if available\n\n"
             "Requirements:\n"
             "• Device must be connected to internet\n"
             "• Location services enabled\n"
             "• Signed into Google account\n"
             "• Find My Device was enabled\n"),
            ("Method 2: Samsung Find My Mobile",
             "Data Loss: ✅ NO | Difficulty: Easy\n\n"
             "Steps:\n"
             "1. Visit: smartthingsfind.samsung.com\n"
             "2. Sign in with Samsung account\n"
             "3. Select your device\n"
             "4. Click 'Unlock'\n"
             "5. Enter Samsung account password\n"
             "6. Device will be unlocked WITHOUT data loss\n\n"
             "Requirements:\n"
             "• Samsung device only\n"
             "• Samsung account signed in\n"
             "• Remote unlock enabled\n"
             "• Internet connection active\n"),
            ("Method 3: Recovery Mode (Factory Reset)",
             "Data Loss: ⚠️ YES | Difficulty: Medium\n\n"
             "Steps:\n"
             "1. Power off the device completely\n"
             "2. Boot into Recovery Mode:\n"
             "   - Most phones: Volume Up + Power button\n"
             "   - Samsung: Volume Up + Bixby + Power\n"
             "3. Navigate to 'Wipe data/factory reset'\n"
             "4. Confirm with power button\n"
             "5. Select 'Reboot system now'\n"
             "6. Set up as new device\n"
             "7. Restore from backup if available\n\n"
             "Requirements:\n"
             "• Physical access to device\n"
             "• Will erase ALL data\n"
             "• Google account credentials (after reset)\n"),
        ]
        
        for title, content in methods:
            self.recovery_result_text.insert(tk.END, f"{title}\n")
            self.recovery_result_text.insert(tk.END, "-"*70 + "\n")
            self.recovery_result_text.insert(tk.END, content + "\n")
    
    def show_iphone_recovery(self):
        """Show iPhone recovery methods"""
        self.recovery_result_text.delete(1.0, tk.END)
        self.recovery_result_text.insert(tk.END, "🍎 iPHONE/IPAD PASSWORD RECOVERY (LEGAL METHODS)\n")
        self.recovery_result_text.insert(tk.END, "="*70 + "\n\n")
        
        methods = [
            ("Method 1: iCloud Find My iPhone",
             "Data Loss: ⚠️ YES | Difficulty: Easy\n\n"
             "Steps:\n"
             "1. Visit: icloud.com/find\n"
             "2. Sign in with Apple ID\n"
             "3. Select your device from 'All Devices'\n"
             "4. Click 'Erase iPhone/iPad'\n"
             "5. Enter Apple ID password to confirm\n"
             "6. Device will be erased and reset\n"
             "7. Set up device again\n"
             "8. Restore from iCloud backup during setup\n\n"
             "Requirements:\n"
             "• Find My iPhone was enabled\n"
             "• Device connected to internet\n"
             "• Apple ID and password\n"
             "• iCloud backup (to restore data)\n"),
            ("Method 2: Recovery Mode with iTunes/Finder",
             "Data Loss: ⚠️ YES | Difficulty: Medium\n\n"
             "Steps:\n"
             "1. Connect iPhone to computer with USB\n"
             "2. Force restart into Recovery Mode:\n"
             "   - iPhone 8+: Volume Up, Volume Down, hold Power\n"
             "   - iPhone 7: Volume Down + Power\n"
             "   - iPhone 6s: Home + Power\n"
             "3. iTunes/Finder will detect recovery mode\n"
             "4. Click 'Restore' (NOT 'Update')\n"
             "5. Wait for restore to complete\n"
             "6. Set up device again\n"
             "7. Restore from backup if available\n\n"
             "Requirements:\n"
             "• Computer with iTunes (Windows) or Finder (Mac)\n"
             "• USB cable\n"
             "• Apple ID password (after restore)\n"),
        ]
        
        for title, content in methods:
            self.recovery_result_text.insert(tk.END, f"{title}\n")
            self.recovery_result_text.insert(tk.END, "-"*70 + "\n")
            self.recovery_result_text.insert(tk.END, content + "\n")
    
    def show_windows_recovery(self):
        """Show Windows recovery methods"""
        self.recovery_result_text.delete(1.0, tk.END)
        self.recovery_result_text.insert(tk.END, "💻 WINDOWS PASSWORD RECOVERY (LEGAL METHODS)\n")
        self.recovery_result_text.insert(tk.END, "="*70 + "\n\n")
        
        methods = [
            ("Method 1: Microsoft Account Reset",
             "Data Loss: ✅ NO | Difficulty: Easy\n\n"
             "Steps:\n"
             "1. Visit: account.live.com/password/reset\n"
             "2. Enter your Microsoft email\n"
             "3. Verify identity (email/phone code)\n"
             "4. Create new password\n"
             "5. Connect PC to internet\n"
             "6. Sign in with new password\n\n"
             "Requirements:\n"
             "• Using Microsoft account (not local)\n"
             "• Access to recovery email/phone\n"
             "• Internet connection\n"),
            ("Method 2: Password Reset Disk",
             "Data Loss: ✅ NO | Difficulty: Easy\n\n"
             "Steps:\n"
             "1. Insert password reset USB drive\n"
             "2. Click 'Reset password' on login screen\n"
             "3. Follow Password Reset Wizard\n"
             "4. Create new password\n"
             "5. Sign in with new password\n\n"
             "Requirements:\n"
             "• Reset disk must be created BEFORE forgetting password\n"
             "• USB drive with reset disk\n"),
        ]
        
        for title, content in methods:
            self.recovery_result_text.insert(tk.END, f"{title}\n")
            self.recovery_result_text.insert(tk.END, "-"*70 + "\n")
            self.recovery_result_text.insert(tk.END, content + "\n")
    
    def show_general_tips(self):
        """Show general recovery tips"""
        self.recovery_result_text.delete(1.0, tk.END)
        self.recovery_result_text.insert(tk.END, "📋 GENERAL PASSWORD RECOVERY TIPS\n")
        self.recovery_result_text.insert(tk.END, "="*70 + "\n\n")
        
        tips = """Recovery Tips:
----------------------------------------------------------------------
  💡 Try common passwords you use
  💡 Check if Caps Lock is on
  💡 Try password variations (add numbers, symbols)
  💡 Check for saved passwords in browser
  💡 Try biometric login (fingerprint, face)
  💡 Contact manufacturer support with proof of purchase

⚠️  Important Reminders:
----------------------------------------------------------------------
  Only recover devices YOU legally own
  Unauthorized access is ILLEGAL
  Factory reset erases ALL data
  Always backup important data regularly
  Keep proof of purchase for devices

📚 Prevention for Future:
----------------------------------------------------------------------
  ✅ Use a password manager (LastPass, Bitwarden, 1Password)
  ✅ Enable biometric authentication
  ✅ Set up recovery email/phone
  ✅ Backup data regularly to cloud
  ✅ Write down passwords in secure location
  ✅ Enable Find My Device features
"""
        self.recovery_result_text.insert(tk.END, tips)
    
    def create_ethics_tab(self):
        """Create Ethical Cybersecurity Framework tab"""
        ethics_frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(ethics_frame, text='🛡️ Ethics')
        
        # Title
        title = tk.Label(
            ethics_frame,
            text="🛡️ Ethical Cybersecurity Framework",
            font=('Segoe UI', 16, 'bold')
        )
        title.pack(pady=(0, 10))
        
        # Topic selection
        topic_frame = tk.LabelFrame(ethics_frame, text="Choose a Topic", font=('Segoe UI', 11, 'bold'))
        topic_frame.pack(fill=tk.X, pady=10, padx=15)
        
        # Buttons for each topic
        button_frame = tk.Frame(topic_frame)
        button_frame.pack(fill=tk.X)
        
        tk.Button(button_frame, text="🚫 Illegal Practices", command=self.show_illegal_practices, 
                 bg='#F44336', fg='white', font=('Segoe UI', 10, 'bold'), width=18).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="✅ Legal Practices", command=self.show_legal_practices, 
                 bg='#4CAF50', fg='white', font=('Segoe UI', 10, 'bold'), width=18).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="📊 Comparison", command=self.show_comparison, 
                 bg='#FF9800', fg='white', font=('Segoe UI', 10, 'bold'), width=18).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="🎓 Career Path", command=self.show_career_path, 
                 bg='#2196F3', fg='white', font=('Segoe UI', 10, 'bold'), width=18).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Result area
        self.ethics_result_text = scrolledtext.ScrolledText(
            ethics_frame,
            height=20,
            font=('Consolas', 10),
            wrap=tk.WORD
        )
        self.ethics_result_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Initialize ethics framework
        self.ethics_framework = EthicalCybersecurityFramework()
    
    def show_illegal_practices(self):
        """Show illegal practices"""
        self.ethics_result_text.delete(1.0, tk.END)
        self.ethics_result_text.insert(tk.END, "🚫 ILLEGAL CYBERSECURITY PRACTICES (NEVER DO THESE)\n")
        self.ethics_result_text.insert(tk.END, "="*80 + "\n\n")
        
        content = """Category: 🚫 Unauthorized Access
----------------------------------------------------------------------
❌ Illegal Practices:
  • Cracking passwords on devices you don't own
  • Bypassing security without authorization
  • Accessing others' devices without permission
  • Hacking into accounts that aren't yours
  • Unauthorized network access

⚖️ Laws Violated:
  • Computer Fraud and Abuse Act (CFAA)
  • Cybercrime Prevention Act
  • Unauthorized Access laws
  • Privacy violations

💀 Consequences:
  • Criminal charges (felony)
  • Heavy fines ($100,000+)
  • Imprisonment (1-20 years)
  • Permanent criminal record


Category: 🚫 Illegal Exploitation
----------------------------------------------------------------------
❌ Illegal Practices:
  • Exploiting vulnerabilities without permission
  • Using exploits for malicious purposes
  • Creating/distributing malware
  • Ransomware attacks
  • Data theft and selling

💀 Consequences:
  • Federal prosecution
  • Decades in prison
  • Millions in fines
  • International warrants


Category: 🚫 Privacy Violations
----------------------------------------------------------------------
❌ Illegal Practices:
  • Spying on others without consent
  • Installing keyloggers on others' devices
  • Intercepting communications illegally
  • Unauthorized surveillance

💀 Consequences:
  • Privacy violation charges
  • Civil damages
  • Regulatory fines
  • Criminal prosecution


Category: 🚫 Encryption Breaking
----------------------------------------------------------------------
❌ Illegal Practices:
  • Breaking encryption without authorization
  • Decrypting others' protected data
  • Bypassing DRM illegally
  • Circumventing security measures

⚖️ Laws Violated:
  • Digital Millennium Copyright Act (DMCA)
  • Copyright infringement
  • Trade secret theft
"""
        self.ethics_result_text.insert(tk.END, content)
    
    def show_legal_practices(self):
        """Show legal practices"""
        self.ethics_result_text.delete(1.0, tk.END)
        self.ethics_result_text.insert(tk.END, "✅ LEGAL & ETHICAL CYBERSECURITY PRACTICES\n")
        self.ethics_result_text.insert(tk.END, "="*80 + "\n\n")
        
        content = """Category: ✅ Authorized Security Testing
----------------------------------------------------------------------
✅ Legal Practices:
  • Penetration testing WITH written permission
  • Bug bounty programs (authorized)
  • Security audits for clients
  • Vulnerability research (responsible disclosure)
  • Red team exercises (contracted)

📋 Requirements:
  • Written authorization/contract
  • Clearly defined scope
  • Rules of engagement document
  • Legal agreement signed

🎓 Recommended Certifications:
  • CEH (Certified Ethical Hacker)
  • OSCP (Offensive Security Certified Professional)
  • GPEN (GIAC Penetration Tester)
  • CompTIA PenTest+


Category: ✅ Defensive Security
----------------------------------------------------------------------
✅ Legal Practices:
  • Network monitoring and defense
  • Incident response
  • Security awareness training
  • Vulnerability assessment
  • Security architecture design

🎓 Recommended Certifications:
  • CompTIA Security+
  • CISSP (Certified Information Systems Security Professional)
  • CISM (Certified Information Security Manager)
  • GCIH (GIAC Certified Incident Handler)


Category: ✅ Educational & Research
----------------------------------------------------------------------
✅ Legal Practices:
  • Learning cybersecurity in controlled labs
  • CTF (Capture The Flag) competitions
  • Home lab experiments
  • Academic research
  • Security tool development

💻 Legal Practice Platforms:
  • HackTheBox (legal platform)
  • TryHackMe (educational)
  • CTF competitions
  • Home virtual labs
  • Bug bounty programs
"""
        self.ethics_result_text.insert(tk.END, content)
    
    def show_comparison(self):
        """Show illegal vs legal comparison"""
        self.ethics_result_text.delete(1.0, tk.END)
        self.ethics_result_text.insert(tk.END, "📊 ILLEGAL vs LEGAL: QUICK COMPARISON\n")
        self.ethics_result_text.insert(tk.END, "="*80 + "\n\n")
        
        content = """Scenario: Testing Network Security
----------------------------------------------------------------------
  ❌ ILLEGAL: Scanning networks you don't own without permission
  ✅ LEGAL:  Scanning your own network or with written authorization

Scenario: Password Testing
----------------------------------------------------------------------
  ❌ ILLEGAL: Cracking passwords on others' accounts/devices
  ✅ LEGAL:  Testing password strength on your own systems

Scenario: Vulnerability Discovery
----------------------------------------------------------------------
  ❌ ILLEGAL: Exploiting found vulnerabilities for personal gain
  ✅ LEGAL:  Responsible disclosure to vendor/bug bounty

Scenario: Device Access
----------------------------------------------------------------------
  ❌ ILLEGAL: Bypassing security on devices you don't own
  ✅ LEGAL:  Recovering your own device with proof of ownership

Scenario: Data Access
----------------------------------------------------------------------
  ❌ ILLEGAL: Accessing others' private data without consent
  ✅ LEGAL:  Accessing data you own or have authorization for

Scenario: Tool Development
----------------------------------------------------------------------
  ❌ ILLEGAL: Creating malware or hacking tools for attacks
  ✅ LEGAL:  Building defensive tools and educational resources
"""
        self.ethics_result_text.insert(tk.END, content)
    
    def show_career_path(self):
        """Show career path"""
        self.ethics_result_text.delete(1.0, tk.END)
        self.ethics_result_text.insert(tk.END, "🎓 LEGAL CYBERSECURITY CAREER PATH\n")
        self.ethics_result_text.insert(tk.END, "="*80 + "\n\n")
        
        content = """💼 Penetration Tester
----------------------------------------------------------------------
  💰 Salary: $70,000 - $120,000/year
  📝 Description: Legally test security with authorization
  📋 Requirements:
    • CEH or OSCP certification
    • Written contracts
    • Legal authorization

💼 Security Analyst
----------------------------------------------------------------------
  💰 Salary: $60,000 - $100,000/year
  📝 Description: Monitor and defend against cyber threats
  📋 Requirements:
    • Security+ certification
    • Analytical skills
    • Incident response

💼 Security Consultant
----------------------------------------------------------------------
  💰 Salary: $80,000 - $150,000/year
  📝 Description: Advise organizations on security
  📋 Requirements:
    • CISSP certification
    • Experience
    • Client trust

💼 Bug Bounty Hunter
----------------------------------------------------------------------
  💰 Salary: $10,000 - $500,000+/year
  📝 Description: Find vulnerabilities legally for rewards
  📋 Requirements:
    • Technical skills
    • Platforms: HackerOne, Bugcrowd
    • Responsible disclosure

💼 Security Researcher
----------------------------------------------------------------------
  💰 Salary: $70,000 - $130,000/year
  📝 Description: Research new security threats
  📋 Requirements:
    • Advanced degree
    • Publications
    • Ethical guidelines
"""
        self.ethics_result_text.insert(tk.END, content)
    
    def clear_all(self):
        """Clear all results"""
        self.password_entry.delete(0, tk.END)
        self.url_entry.delete(0, tk.END)
        self.password_result_text.delete(1.0, tk.END)
        self.url_result_text.delete(1.0, tk.END)
        self.wifi_result_text.delete(1.0, tk.END)
        self.overall_result_text.delete(1.0, tk.END)
        
        self.results = {
            'password': {},
            'url': {},
            'wifi': {},
            'risk_level': '',
            'recommendations': []
        }


def main():
    root = tk.Tk()
    app = CyberSecurityDashboard(root)
    root.mainloop()


if __name__ == "__main__":
    main()
