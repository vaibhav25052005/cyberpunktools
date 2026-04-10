import re
from datetime import datetime
from urllib.parse import urlparse
from phishing_detector import check_url
from ai_phishing_detector import AIPhishingDetector

class EmailPhishingDetector:
    """
    Advanced Email Phishing Detection Module
    Analyzes email content, headers, and links for phishing indicators
    """
    
    def __init__(self):
        self.ai_detector = AIPhishingDetector()
        
    def analyze_email(self, subject="", sender="", body="", links=None, attachments=None):
        """
        Complete email phishing analysis
        Returns: dict with analysis results and risk assessment
        """
        if links is None:
            links = []
        if attachments is None:
            attachments = []
            
        analysis_results = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Subject": subject,
            "Sender": sender,
            "Overall Risk": "UNKNOWN",
            "Risk Score": 0,
            "Warnings": [],
            "Details": {}
        }
        
        # Analyze different components
        sender_risk = self.analyze_sender(sender)
        subject_risk = self.analyze_subject(subject)
        body_risk = self.analyze_body(body)
        link_risks = [self.analyze_link(link) for link in links]
        attachment_risk = self.analyze_attachments(attachments)
        
        # Calculate overall risk
        all_risks = [
            sender_risk.get("Risk Score", 0),
            subject_risk.get("Risk Score", 0),
            body_risk.get("Risk Score", 0),
            attachment_risk.get("Risk Score", 0)
        ]
        all_risks.extend([lr.get('Risk Score', 0) for lr in link_risks])
        
        risk_score = sum(all_risks) / len(all_risks) if all_risks else 0
        analysis_results["Risk Score"] = min(int(risk_score), 100)
        
        # Collect all warnings
        analysis_results["Warnings"].extend(sender_risk.get("Warnings", []))
        analysis_results["Warnings"].extend(subject_risk.get("Warnings", []))
        analysis_results["Warnings"].extend(body_risk.get("Warnings", []))
        analysis_results["Warnings"].extend(attachment_risk.get("Warnings", []))
        
        for lr in link_risks:
            analysis_results["Warnings"].extend(lr.get("Warnings", []))
        
        # Determine overall risk level
        if risk_score >= 70:
            analysis_results["Overall Risk"] = "HIGH"
        elif risk_score >= 40:
            analysis_results["Overall Risk"] = "MEDIUM"
        elif risk_score >= 20:
            analysis_results["Overall Risk"] = "LOW"
        else:
            analysis_results["Overall Risk"] = "SAFE"
        
        # Store detailed analysis
        analysis_results["Details"] = {
            "Sender Analysis": sender_risk,
            "Subject Analysis": subject_risk,
            "Body Analysis": body_risk,
            "Link Analysis": link_risks,
            "Attachment Analysis": attachment_risk
        }
        
        return analysis_results
    
    def analyze_sender(self, sender):
        """Analyze email sender for suspicious indicators"""
        risk_score = 0
        warnings = []
        
        if not sender:
            return {"Risk Score": 0, "Warnings": []}
        
        # Check for suspicious patterns in email address
        sender_lower = sender.lower()
        
        # Check 1: Free email providers (higher risk for business emails)
        free_providers = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"]
        is_free_provider = any(provider in sender_lower for provider in free_providers)
        
        # Check 2: Suspicious domain patterns
        suspicious_patterns = [
            r'\d+',  # Numbers in domain
            r'[-_]+' # Multiple hyphens/underscores
        ]
        
        # Extract domain
        domain_match = re.search(r'@([\w.-]+)', sender)
        if domain_match:
            domain = domain_match.group(1)
            
            # Check for typosquatting (common phishing technique)
            legitimate_domains = ["google.com", "microsoft.com", "amazon.com", "apple.com", 
                                "paypal.com", "netflix.com", "facebook.com"]
            
            for legit in legitimate_domains:
                if self.is_typosquatting(domain, legit):
                    risk_score += 50
                    warnings.append(f"⚠️ Possible typosquatting: {domain} resembles {legit}")
                    break
            
            # Check if domain has suspicious patterns
            for pattern in suspicious_patterns:
                if re.search(pattern, domain):
                    risk_score += 15
                    warnings.append(f"⚠️ Suspicious domain pattern detected: {domain}")
                    break
        
        # Check 3: Display name mismatch
        if '<' in sender and '>' in sender:
            name_match = re.match(r'(.+?)\s*<(.+?)>', sender)
            if name_match:
                display_name = name_match.group(1).lower()
                email_addr = name_match.group(2).lower()
                
                # Check if display name claims to be from a company but email doesn't match
                company_names = ["support", "admin", "security", "bank", "paypal", "amazon"]
                for company in company_names:
                    if company in display_name and company not in email_addr:
                        risk_score += 35
                        warnings.append(f"⚠️ Display name/email mismatch: Claims to be '{company}'")
                        break
        
        # Check 4: Very long email address (often used in phishing)
        if len(sender) > 50:
            risk_score += 10
            warnings.append("ℹ️ Unusually long email address")
        
        return {
            "Risk Score": min(risk_score, 100),
            "Warnings": warnings,
            "Is Free Provider": is_free_provider
        }
    
    def analyze_subject(self, subject):
        """Analyze email subject line for phishing indicators"""
        risk_score = 0
        warnings = []
        
        if not subject:
            return {"Risk Score": 0, "Warnings": []}
        
        subject_lower = subject.lower()
        
        # Urgency and fear tactics
        urgency_keywords = [
            "urgent", "immediate action", "suspended", "verify now", "confirm",
            "alert", "warning", "compromised", "unusual activity", "locked",
            "expiring", "final notice", "overdue", "illegal"
        ]
        
        # Reward/greed tactics
        reward_keywords = [
            "won", "prize", "congratulations", "claim now", "free", "gift",
            "reward", "lottery", "inheritance", "million"
        ]
        
        # Check for urgency
        urgency_count = sum(1 for keyword in urgency_keywords if keyword in subject_lower)
        if urgency_count >= 2:
            risk_score += 30
            warnings.append(f"⚠️ High urgency detected ({urgency_count} urgency indicators)")
        elif urgency_count == 1:
            risk_score += 15
            warnings.append("ℹ️ Urgent language detected")
        
        # Check for reward tactics
        reward_count = sum(1 for keyword in reward_keywords if keyword in subject_lower)
        if reward_count >= 1:
            risk_score += 25
            warnings.append(f"⚠️ Reward/bait language detected ({reward_count} indicators)")
        
        # Check for ALL CAPS (shouting)
        if subject.isupper() and len(subject) > 10:
            risk_score += 15
            warnings.append("ℹ️ ALL CAPS subject line (aggressive tactic)")
        
        # Check for excessive punctuation
        if subject.count('!') >= 3 or subject.count('?') >= 3:
            risk_score += 10
            warnings.append("ℹ️ Excessive punctuation detected")
        
        # Check for very long subject
        if len(subject) > 80:
            risk_score += 10
            warnings.append("ℹ️ Unusually long subject line")
        
        return {
            "Risk Score": min(risk_score, 100),
            "Warnings": warnings,
            "Urgency Indicators": urgency_count,
            "Reward Indicators": reward_count
        }
    
    def analyze_body(self, body):
        """Analyze email body content for phishing indicators"""
        risk_score = 0
        warnings = []
        
        if not body:
            return {"Risk Score": 0, "Warnings": []}
        
        body_lower = body.lower()
        
        # Check for suspicious keywords
        suspicious_keywords = [
            "click here", "verify your account", "update payment", "confirm identity",
            "suspended account", "unusual activity", "login now", "password expired",
            "bank account", "credit card", "social security", "ssn", "date of birth"
        ]
        
        keyword_count = sum(1 for keyword in suspicious_keywords if keyword in body_lower)
        if keyword_count >= 3:
            risk_score += 40
            warnings.append(f"⚠️ Multiple suspicious keywords detected ({keyword_count})")
        elif keyword_count >= 1:
            risk_score += 20
            warnings.append(f"ℹ️ Some suspicious keywords found ({keyword_count})")
        
        # Check for poor grammar/spelling indicators
        poor_grammar_indicators = [
            "dear valued customer", "dear user", "kindly", "kind regards",
            "kindly verify", "please do this", "do this immediately"
        ]
        
        grammar_count = sum(1 for phrase in poor_grammar_indicators if phrase in body_lower)
        if grammar_count >= 2:
            risk_score += 20
            warnings.append("ℹ️ Generic/poor grammar patterns detected")
        
        # Check for threats
        threat_keywords = ["consequences", "legal action", "penalty", "fine", "prosecution"]
        threat_count = sum(1 for keyword in threat_keywords if keyword in body_lower)
        if threat_count >= 1:
            risk_score += 25
            warnings.append("⚠️ Threatening language detected")
        
        # Check for requests for sensitive information
        sensitive_requests = [
            "password", "credit card", "social security", "bank account",
            "pin", "otp", "verification code", "cvv"
        ]
        
        sensitive_count = sum(1 for keyword in sensitive_requests if keyword in body_lower)
        if sensitive_count >= 1:
            risk_score += 35
            warnings.append(f"⚠️ Request for sensitive information detected")
        
        return {
            "Risk Score": min(risk_score, 100),
            "Warnings": warnings,
            "Suspicious Keywords": keyword_count,
            "Sensitive Requests": sensitive_count
        }
    
    def analyze_link(self, url):
        """Analyze individual link in email"""
        warnings = []
        
        if not url:
            return {"URL": url, "Risk Score": 0, "Warnings": []}
        
        # Use existing URL phishing detection
        url_status, url_score, url_feedback = check_url(url)
        
        # Also use AI detection
        try:
            ai_status, ai_score, ai_confidence = self.ai_detector.predict(url)
            combined_score = (url_score + ai_score) / 2
        except:
            combined_score = url_score
        
        if combined_score >= 60:
            warnings.append(f"⚠️ Suspicious link detected: {url}")
        
        return {
            "URL": url,
            "Risk Score": int(combined_score),
            "Status": url_status,
            "Warnings": warnings,
            "Feedback": url_feedback
        }
    
    def analyze_attachments(self, attachments):
        """Analyze email attachments for risks"""
        risk_score = 0
        warnings = []
        
        if not attachments:
            return {"Risk Score": 0, "Warnings": [], "Count": 0}
        
        # Dangerous file extensions
        dangerous_extensions = [
            '.exe', '.bat', '.cmd', '.com', '.scr', '.pif', '.vbs', '.js',
            '.jar', '.msi', '.dll', '.cpl', '.wsf', '.ps1'
        ]
        
        risky_extensions = [
            '.doc', '.docx', '.xls', '.xlsx', '.pdf', '.zip', '.rar',
            '.7z', '.iso', '.ppt', '.pptx'
        ]
        
        for attachment in attachments:
            attachment_lower = attachment.lower()
            
            # Check for dangerous extensions
            if any(attachment_lower.endswith(ext) for ext in dangerous_extensions):
                risk_score += 50
                warnings.append(f"⚠️ Dangerous attachment: {attachment}")
            
            # Check for risky extensions
            elif any(attachment_lower.endswith(ext) for ext in risky_extensions):
                risk_score += 20
                warnings.append(f"ℹ️ Potentially risky attachment: {attachment}")
            
            # Check for double extensions (e.g., document.pdf.exe)
            if attachment_lower.count('.') >= 2:
                risk_score += 30
                warnings.append(f"⚠️ Double extension detected: {attachment}")
        
        return {
            "Risk Score": min(risk_score, 100),
            "Warnings": warnings,
            "Count": len(attachments),
            "Attachments": attachments
        }
    
    def is_typosquatting(self, domain1, domain2):
        """Check if domain1 is a typosquat of domain2"""
        if domain1 == domain2:
            return False
        
        # Calculate Levenshtein distance (simplified)
        if abs(len(domain1) - len(domain2)) > 2:
            return False
        
        # Common typosquatting patterns
        # 1. Character substitution (e.g., g00gle.com)
        # 2. Missing/extra characters (e.g., gooogle.com)
        # 3. Character transposition (e.g., goolge.com)
        
        distance = self.levenshtein_distance(domain1, domain2)
        
        # If distance is 1-2, likely typosquatting
        return 1 <= distance <= 2
    
    def levenshtein_distance(self, s1, s2):
        """Calculate Levenshtein distance between two strings"""
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                # Calculate insertions, deletions, substitutions
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    def format_results(self, analysis):
        """Format analysis results for display"""
        output = []
        output.append("="*70)
        output.append("EMAIL PHISHING ANALYSIS RESULTS")
        output.append("="*70)
        output.append(f"Timestamp: {analysis['Timestamp']}")
        output.append(f"Subject: {analysis['Subject']}")
        output.append(f"Sender: {analysis['Sender']}")
        output.append(f"Overall Risk: {analysis['Overall Risk']}")
        output.append(f"Risk Score: {analysis['Risk Score']}/100")
        output.append("="*70)
        
        if analysis['Warnings']:
            output.append("\n⚠️ WARNINGS:")
            for warning in analysis['Warnings']:
                output.append(f"  • {warning}")
        
        output.append("\n" + "="*70)
        return '\n'.join(output)


# Quick test
if __name__ == "__main__":
    from colorama import init, Fore, Style
    init(autoreset=True)
    
    detector = EmailPhishingDetector()
    
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    print(Fore.CYAN + Style.BRIGHT + "📧 EMAIL PHISHING DETECTOR")
    print(Fore.CYAN + Style.BRIGHT + "="*70)
    
    # Test with a suspicious email
    test_email = {
        "subject": "URGENT: Your Account Has Been Suspended!",
        "sender": "support@paypa1-secure.com",
        "body": "Dear valued customer, your account has been suspended due to unusual activity. Please click here to verify your identity and update your payment information immediately. Failure to do so will result in permanent account closure.",
        "links": ["http://paypa1-secure.com/verify"],
        "attachments": ["invoice.pdf.exe"]
    }
    
    print(Fore.MAGENTA + "\n📌 Analyzing suspicious email...")
    result = detector.analyze_email(**test_email)
    formatted = detector.format_results(result)
    print(Fore.WHITE + formatted)
