"""
Mobile App Version - Cyber Security Assistant
Built with Kivy Framework
Can be exported to Android using Buildozer
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import platform

# Import security modules
from password_checker import check_password
from phishing_detector import check_url
from ai_phishing_detector import AIPhishingDetector
from ip_analyzer import IPAnalyzer
from risk_engine import calculate_risk

# Set window size for desktop testing
Window.size = (400, 700)


class HomeScreen(Screen):
    """Home screen of the mobile app"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text='🔐 Cyber Security\nAssistant',
            font_size=28,
            bold=True,
            size_hint=(1, 0.3),
            color=(0.1, 0.45, 0.91, 1)
        )
        layout.add_widget(title)
        
        # Subtitle
        subtitle = Label(
            text='Protecting your digital world',
            font_size=14,
            size_hint=(1, 0.1),
            color=(0.37, 0.39, 0.41, 1)
        )
        layout.add_widget(subtitle)
        
        # Navigation buttons
        btn_password = Button(
            text='🔑 Check Password',
            size_hint=(1, 0.12),
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=16
        )
        btn_password.bind(on_press=self.go_to_password)
        layout.add_widget(btn_password)
        
        btn_url = Button(
            text='🔗 Check URL',
            size_hint=(1, 0.12),
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=16
        )
        btn_url.bind(on_press=self.go_to_url)
        layout.add_widget(btn_url)
        
        btn_ip = Button(
            text='🌐 IP Analysis',
            size_hint=(1, 0.12),
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=16
        )
        btn_ip.bind(on_press=self.go_to_ip)
        layout.add_widget(btn_ip)
        
        btn_risk = Button(
            text='📊 Risk Assessment',
            size_hint=(1, 0.12),
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=16
        )
        btn_risk.bind(on_press=self.go_to_risk)
        layout.add_widget(btn_risk)
        
        self.add_widget(layout)
    
    def go_to_password(self, instance):
        self.manager.current = 'password'
    
    def go_to_url(self, instance):
        self.manager.current = 'url'
    
    def go_to_ip(self, instance):
        self.manager.current = 'ip'
    
    def go_to_risk(self, instance):
        self.manager.current = 'risk'


class PasswordScreen(Screen):
    """Password strength check screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Back button
        btn_back = Button(
            text='← Back',
            size_hint=(1, 0.08),
            background_color=(0.37, 0.39, 0.41, 1),
            font_size=14
        )
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        # Title
        title = Label(
            text='🔑 Password Strength Check',
            font_size=20,
            bold=True,
            size_hint=(1, 0.1),
            color=(0.1, 0.45, 0.91, 1)
        )
        layout.add_widget(title)
        
        # Input
        self.password_input = TextInput(
            hint_text='Enter password...',
            multiline=False,
            password=True,
            size_hint=(1, 0.1),
            font_size=16
        )
        layout.add_widget(self.password_input)
        
        # Check button
        btn_check = Button(
            text='✓ Check Strength',
            size_hint=(1, 0.1),
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=16
        )
        btn_check.bind(on_press=self.check_password)
        layout.add_widget(btn_check)
        
        # Result
        self.result_label = Label(
            text='Result will appear here...',
            font_size=14,
            size_hint=(1, 0.4),
            color=(0.37, 0.39, 0.41, 1)
        )
        layout.add_widget(self.result_label)
        
        self.add_widget(layout)
    
    def check_password(self, instance):
        password = self.password_input.text
        if not password:
            self.result_label.text = '⚠️ Please enter a password'
            return
        
        strength, score, feedback = check_password(password)
        
        result_text = f"Strength: {strength}\nRisk Score: {score}/100\n\n"
        if feedback:
            result_text += "Suggestions:\n" + "\n".join([f"• {f}" for f in feedback])
        
        self.result_label.text = result_text
    
    def go_back(self, instance):
        self.manager.current = 'home'


class URLScreen(Screen):
    """URL phishing detection screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Back button
        btn_back = Button(
            text='← Back',
            size_hint=(1, 0.08),
            background_color=(0.37, 0.39, 0.41, 1),
            font_size=14
        )
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        # Title
        title = Label(
            text='🔗 URL Phishing Detection',
            font_size=20,
            bold=True,
            size_hint=(1, 0.1),
            color=(0.1, 0.45, 0.91, 1)
        )
        layout.add_widget(title)
        
        # Input
        self.url_input = TextInput(
            hint_text='Enter URL to check...',
            multiline=False,
            size_hint=(1, 0.1),
            font_size=14
        )
        layout.add_widget(self.url_input)
        
        # Buttons
        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.1))
        
        btn_rule = Button(
            text='Rule-Based',
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=14
        )
        btn_rule.bind(on_press=self.check_url_rule)
        btn_layout.add_widget(btn_rule)
        
        btn_ai = Button(
            text='AI Model',
            background_color=(0, 0.8, 0.2, 1),
            font_size=14
        )
        btn_ai.bind(on_press=self.check_url_ai)
        btn_layout.add_widget(btn_ai)
        
        layout.add_widget(btn_layout)
        
        # Result
        self.result_label = Label(
            text='Result will appear here...',
            font_size=14,
            size_hint=(1, 0.4),
            color=(0.37, 0.39, 0.41, 1)
        )
        layout.add_widget(self.result_label)
        
        # AI detector
        self.ai_detector = AIPhishingDetector()
        
        self.add_widget(layout)
    
    def check_url_rule(self, instance):
        url = self.url_input.text
        if not url:
            self.result_label.text = '⚠️ Please enter a URL'
            return
        
        status, score, feedback = check_url(url)
        
        result_text = f"Status: {status}\nRisk Score: {score}/100\nMethod: Rule-Based\n\n"
        if feedback:
            result_text += "Warnings:\n" + "\n".join([f"• {f}" for f in feedback])
        
        self.result_label.text = result_text
    
    def check_url_ai(self, instance):
        url = self.url_input.text
        if not url:
            self.result_label.text = '⚠️ Please enter a URL'
            return
        
        try:
            status, score, confidence = self.ai_detector.predict(url)
            self.result_label.text = f"Status: {status}\nRisk Score: {score}/100\nConfidence: {confidence:.1f}%\nMethod: AI-Powered"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"
    
    def go_back(self, instance):
        self.manager.current = 'home'


class IPScreen(Screen):
    """IP Address Analysis screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Back button
        btn_back = Button(
            text='← Back',
            size_hint=(1, 0.08),
            background_color=(0.37, 0.39, 0.41, 1),
            font_size=14
        )
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        # Title
        title = Label(
            text='🌐 IP Address Analysis',
            font_size=20,
            bold=True,
            size_hint=(1, 0.1),
            color=(0.1, 0.45, 0.91, 1)
        )
        layout.add_widget(title)
        
        # Input
        self.ip_input = TextInput(
            hint_text='Enter IP address...',
            multiline=False,
            size_hint=(1, 0.1),
            font_size=14
        )
        layout.add_widget(self.ip_input)
        
        # Buttons
        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.1))
        
        btn_analyze = Button(
            text='🔍 Analyze',
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=14
        )
        btn_analyze.bind(on_press=self.analyze_ip)
        btn_layout.add_widget(btn_analyze)
        
        btn_myip = Button(
            text='📡 My IP',
            background_color=(0, 0.8, 0.2, 1),
            font_size=14
        )
        btn_myip.bind(on_press=self.get_my_ip)
        btn_layout.add_widget(btn_myip)
        
        layout.add_widget(btn_layout)
        
        # Result
        self.result_label = Label(
            text='Result will appear here...',
            font_size=13,
            size_hint=(1, 0.45),
            color=(0.37, 0.39, 0.41, 1)
        )
        layout.add_widget(self.result_label)
        
        # IP analyzer
        self.ip_analyzer = IPAnalyzer()
        
        self.add_widget(layout)
    
    def analyze_ip(self, instance):
        ip = self.ip_input.text
        if not ip:
            self.result_label.text = '⚠️ Please enter an IP address'
            return
        
        try:
            self.result_label.text = 'Analyzing...'
            result = self.ip_analyzer.check_ip(ip)
            
            if result.get("Status") == "Success":
                result_text = f"IP: {result['IP']}\n"
                result_text += f"Country: {result['Country']}\n"
                result_text += f"City: {result['City']}\n"
                result_text += f"ISP: {result['ISP']}\n"
                result_text += f"Risk: {result['Risk Level']}\n"
                result_text += f"Score: {result['Risk Score']}/100\n"
                
                if result.get("Warnings"):
                    result_text += "\nWarnings:\n" + "\n".join([f"• {w}" for w in result["Warnings"]])
                
                self.result_label.text = result_text
            else:
                self.result_label.text = f"Error: {result.get('Error', 'Unknown')}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"
    
    def get_my_ip(self, instance):
        try:
            self.result_label.text = 'Fetching your IP...'
            public_ip = self.ip_analyzer.get_public_ip()
            self.ip_input.text = public_ip
            
            result = self.ip_analyzer.check_ip(public_ip)
            
            if result.get("Status") == "Success":
                result_text = f"Your IP: {result['IP']}\n"
                result_text += f"Country: {result['Country']}\n"
                result_text += f"ISP: {result['ISP']}\n"
                result_text += f"Risk: {result['Risk Level']}\n"
                result_text += f"Score: {result['Risk Score']}/100"
                
                self.result_label.text = result_text
            else:
                self.result_label.text = f"Error: {result.get('Error', 'Unknown')}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"
    
    def go_back(self, instance):
        self.manager.current = 'home'


class RiskScreen(Screen):
    """Risk assessment screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Back button
        btn_back = Button(
            text='← Back',
            size_hint=(1, 0.08),
            background_color=(0.37, 0.39, 0.41, 1),
            font_size=14
        )
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        # Title
        title = Label(
            text='📊 Risk Assessment',
            font_size=20,
            bold=True,
            size_hint=(1, 0.1),
            color=(0.1, 0.45, 0.91, 1)
        )
        layout.add_widget(title)
        
        # Instructions
        instruction = Label(
            text='Enter scores to calculate overall risk:',
            font_size=14,
            size_hint=(1, 0.08),
            color=(0.37, 0.39, 0.41, 1)
        )
        layout.add_widget(instruction)
        
        # Input fields
        self.password_score = TextInput(
            hint_text='Password Risk Score (0-100)',
            multiline=False,
            size_hint=(1, 0.08),
            font_size=14
        )
        layout.add_widget(self.password_score)
        
        self.url_score = TextInput(
            hint_text='URL Risk Score (0-100)',
            multiline=False,
            size_hint=(1, 0.08),
            font_size=14
        )
        layout.add_widget(self.url_score)
        
        # Calculate button
        btn_calc = Button(
            text='🧮 Calculate Risk',
            size_hint=(1, 0.1),
            background_color=(0.1, 0.45, 0.91, 1),
            font_size=16
        )
        btn_calc.bind(on_press=self.calculate_risk)
        layout.add_widget(btn_calc)
        
        # Result
        self.result_label = Label(
            text='Risk assessment will appear here...',
            font_size=14,
            size_hint=(1, 0.35),
            color=(0.37, 0.39, 0.41, 1)
        )
        layout.add_widget(self.result_label)
        
        self.add_widget(layout)
    
    def calculate_risk(self, instance):
        try:
            pwd_score = int(self.password_score.text)
            url_score = int(self.url_score.text)
            
            risk_level, recommendations = calculate_risk([pwd_score, url_score])
            
            result_text = f"Overall Risk: {risk_level}\n\nRecommendations:\n"
            result_text += "\n".join([f"{i}. {r}" for i, r in enumerate(recommendations, 1)])
            
            self.result_label.text = result_text
        except ValueError:
            self.result_label.text = '⚠️ Please enter valid numbers (0-100)'
    
    def go_back(self, instance):
        self.manager.current = 'home'


class CyberSecurityApp(App):
    """Main application class"""
    
    def build(self):
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(PasswordScreen(name='password'))
        sm.add_widget(URLScreen(name='url'))
        sm.add_widget(IPScreen(name='ip'))
        sm.add_widget(RiskScreen(name='risk'))
        
        return sm


if __name__ == '__main__':
    CyberSecurityApp().run()
