import re

def check_url(url):
    """
    Detect potential phishing URLs based on suspicious patterns.
    Returns: (status, risk_score, feedback)
    """
    feedback = []
    risk_score = 10

    # Check for HTTPS
    if "https://" not in url:
        risk_score += 30
        feedback.append("❌ Not using HTTPS encryption")

    # Check for suspicious keywords
    suspicious_keywords = ["login", "verify", "bank", "secure", "account", "update", "confirm"]
    found_keywords = [word for word in suspicious_keywords if word in url.lower()]
    
    if found_keywords:
        risk_score += 40
        feedback.append(f"❌ Suspicious keywords found: {', '.join(found_keywords)}")

    # Check URL length (phishing URLs are often long)
    if len(url) > 50:
        risk_score += 20
        feedback.append("⚠️ Unusually long URL (possible obfuscation)")

    # Check for IP address instead of domain
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    if re.search(ip_pattern, url):
        risk_score += 30
        feedback.append("❌ URL contains IP address instead of domain name")

    # Check for multiple subdomains
    if url.count('.') > 3:
        risk_score += 15
        feedback.append("⚠️ Multiple subdomains detected")

    # Determine status
    if risk_score >= 70:
        status = "Dangerous"
    elif risk_score >= 40:
        status = "Suspicious"
    elif risk_score >= 20:
        status = "Risky"
    else:
        status = "Safe"

    return status, risk_score, feedback
