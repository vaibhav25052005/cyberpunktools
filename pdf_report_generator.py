from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime
import os

class PDFReportGenerator:
    """Generate professional PDF security reports"""
    
    def __init__(self, filename="security_report.pdf"):
        self.filename = filename
        self.doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        self.styles = getSampleStyleSheet()
        self.story = []
        self.setup_styles()
    
    def setup_styles(self):
        """Custom styles for the report"""
        self.styles.add(ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            textColor=HexColor('#1a73e8'),
            spaceAfter=20,
            alignment=TA_CENTER
        ))
        
        self.styles.add(ParagraphStyle(
            'CustomHeading',
            parent=self.styles['Heading1'],
            fontSize=16,
            textColor=HexColor('#202124'),
            spaceBefore=20,
            spaceAfter=10
        ))
        
        self.styles.add(ParagraphStyle(
            'CustomSubHeading',
            parent=self.styles['Heading2'],
            fontSize=13,
            textColor=HexColor('#5f6368'),
            spaceBefore=15,
            spaceAfter=8
        ))
        
        self.styles.add(ParagraphStyle(
            'BodyText2',
            parent=self.styles['BodyText'],
            fontSize=11,
            spaceAfter=6
        ))
    
    def add_header(self):
        """Add report header"""
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(Paragraph("🔐 CYBER SECURITY REPORT", self.styles['CustomTitle']))
        self.story.append(Spacer(1, 0.3*inch))
        
        # Date and time
        now = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        self.story.append(Paragraph(f"Generated: {now}", self.styles['BodyText2']))
        self.story.append(Spacer(1, 0.2*inch))
    
    def add_risk_summary(self, risk_level, recommendations):
        """Add overall risk summary"""
        self.story.append(Paragraph("OVERALL SECURITY ASSESSMENT", self.styles['CustomHeading']))
        
        # Risk level table
        risk_color = {
            "🔴 HIGH RISK": '#ff4444',
            "🟡 MEDIUM RISK": '#ffbb33',
            "🟢 LOW RISK": '#00C851',
            "🔵 VERY LOW RISK": '#33b5e5',
            "UNKNOWN": '#999999'
        }.get(risk_level, '#999999')
        
        risk_data = [
            ['Risk Level', risk_level],
            ['Assessment Date', datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        ]
        
        risk_table = Table(risk_data, colWidths=[2*inch, 4*inch])
        risk_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), HexColor('#f1f3f4')),
            ('BACKGROUND', (1, 0), (1, -1), HexColor(risk_color)),
            ('TEXTCOLOR', (1, 0), (1, -1), white),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, HexColor('#dadce0')),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        self.story.append(risk_table)
        self.story.append(Spacer(1, 0.3*inch))
        
        # Recommendations
        self.story.append(Paragraph("RECOMMENDATIONS", self.styles['CustomSubHeading']))
        for i, rec in enumerate(recommendations, 1):
            self.story.append(Paragraph(f"{i}. {rec}", self.styles['BodyText2']))
    
    def add_password_analysis(self, strength, score, feedback):
        """Add password analysis section"""
        self.story.append(PageBreak())
        self.story.append(Paragraph("PASSWORD STRENGTH ANALYSIS", self.styles['CustomHeading']))
        
        strength_color = {
            "Weak": '#ff4444',
            "Medium": '#ffbb33',
            "Strong": '#00C851',
            "Very Strong": '#007bff'
        }.get(strength, '#999999')
        
        data = [
            ['Parameter', 'Result'],
            ['Strength Level', strength],
            ['Risk Score', f"{score}/100"],
            ['Assessment', 'Needs Improvement' if score > 40 else 'Good']
        ]
        
        table = Table(data, colWidths=[2*inch, 4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1a73e8')),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('BACKGROUND', (0, 1), (0, -1), HexColor('#f1f3f4')),
            ('BACKGROUND', (1, 1), (1, 1), HexColor(strength_color)),
            ('TEXTCOLOR', (1, 1), (1, 1), white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 1, HexColor('#dadce0')),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        self.story.append(table)
        
        if feedback:
            self.story.append(Spacer(1, 0.2*inch))
            self.story.append(Paragraph("Suggestions:", self.styles['CustomSubHeading']))
            for item in feedback:
                self.story.append(Paragraph(f"• {item}", self.styles['BodyText2']))
    
    def add_url_analysis(self, status, score, feedback):
        """Add URL/Phishing analysis section"""
        self.story.append(Spacer(1, 0.3*inch))
        self.story.append(Paragraph("PHISHING URL DETECTION", self.styles['CustomHeading']))
        
        status_color = {
            "Safe": '#00C851',
            "Risky": '#ffbb33',
            "Suspicious": '#ff8800',
            "Dangerous": '#ff4444'
        }.get(status, '#999999')
        
        data = [
            ['Parameter', 'Result'],
            ['URL Status', status],
            ['Risk Score', f"{score}/100"],
            ['Threat Level', 'Low' if score < 40 else 'High']
        ]
        
        table = Table(data, colWidths=[2*inch, 4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1a73e8')),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('BACKGROUND', (0, 1), (0, -1), HexColor('#f1f3f4')),
            ('BACKGROUND', (1, 1), (1, 1), HexColor(status_color)),
            ('TEXTCOLOR', (1, 1), (1, 1), white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 1, HexColor('#dadce0')),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        
        self.story.append(table)
        
        if feedback:
            self.story.append(Spacer(1, 0.2*inch))
            self.story.append(Paragraph("Security Warnings:", self.styles['CustomSubHeading']))
            for item in feedback:
                self.story.append(Paragraph(f"• {item}", self.styles['BodyText2']))
    
    def add_wifi_scan(self, wifi_data, error=None):
        """Add WiFi scan results"""
        self.story.append(PageBreak())
        self.story.append(Paragraph("WIFI NETWORK SCAN", self.styles['CustomHeading']))
        
        if error:
            self.story.append(Paragraph(f"Error: {error}", self.styles['BodyText2']))
        else:
            self.story.append(Paragraph("Scan Results:", self.styles['CustomSubHeading']))
            # Clean and format WiFi data
            clean_data = wifi_data.replace('\r', '').replace('\x00', '')
            self.story.append(Paragraph(clean_data[:2000], self.styles['BodyText2']))
    
    def add_footer(self):
        """Add report footer"""
        self.story.append(PageBreak())
        self.story.append(Spacer(1, 2*inch))
        self.story.append(Paragraph("_" * 70, self.styles['BodyText2']))
        self.story.append(Spacer(1, 0.2*inch))
        self.story.append(Paragraph(
            "This report was generated by Personal Cyber Security Assistant.",
            self.styles['BodyText2']
        ))
        self.story.append(Paragraph(
            "For questions or concerns, consult with a cybersecurity professional.",
            self.styles['BodyText2']
        ))
        self.story.append(Spacer(1, 0.3*inch))
        self.story.append(Paragraph(
            f"Report generated on {datetime.now().strftime('%B %d, %Y')}",
            self.styles['BodyText2']
        ))
    
    def generate_report(self, report_data):
        """Generate complete PDF report"""
        self.add_header()
        
        # Add risk summary
        self.add_risk_summary(
            report_data.get('risk_level', 'UNKNOWN'),
            report_data.get('recommendations', [])
        )
        
        # Add password analysis
        if 'password' in report_data:
            pwd = report_data['password']
            self.add_password_analysis(
                pwd.get('strength', 'Unknown'),
                pwd.get('score', 0),
                pwd.get('feedback', [])
            )
        
        # Add URL analysis
        if 'url' in report_data:
            url = report_data['url']
            self.add_url_analysis(
                url.get('status', 'Unknown'),
                url.get('score', 0),
                url.get('feedback', [])
            )
        
        # Add WiFi scan
        if 'wifi' in report_data:
            wifi = report_data['wifi']
            self.add_wifi_scan(
                wifi.get('data', ''),
                wifi.get('error')
            )
        
        self.add_footer()
        
        # Build PDF
        self.doc.build(self.story)
        print(f"✅ PDF Report generated: {os.path.abspath(self.filename)}")
        return self.filename


# Example usage
if __name__ == "__main__":
    # Sample report data
    sample_data = {
        'risk_level': '🟡 MEDIUM RISK',
        'recommendations': [
            'Strengthen your passwords',
            'Be cautious with unknown links',
            'Verify WiFi network authenticity'
        ],
        'password': {
            'strength': 'Medium',
            'score': 40,
            'feedback': ['Add special characters', 'Increase length']
        },
        'url': {
            'status': 'Suspicious',
            'score': 60,
            'feedback': ['Missing HTTPS', 'Suspicious keywords found']
        },
        'wifi': {
            'data': 'Network 1: HomeWiFi (Strong)\nNetwork 2: OfficeNet (Medium)',
            'error': None
        }
    }
    
    generator = PDFReportGenerator("sample_report.pdf")
    generator.generate_report(sample_data)
