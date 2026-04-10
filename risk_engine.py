def calculate_risk(scores):
    """
    Calculate overall risk level from multiple security scores.
    Returns: (risk_level, recommendations)
    """
    if not scores:
        return "UNKNOWN", ["No security checks performed"]

    # Calculate weighted average
    total_score = sum(scores) / len(scores)

    # Determine risk level
    if total_score >= 70:
        risk_level = "🔴 HIGH RISK"
        recommendations = [
            "⚠️ Immediate action required!",
            "🔑 Change all passwords immediately",
            "🔗 Avoid clicking suspicious links",
            "📡 Connect only to trusted WiFi networks",
            "🛡️ Enable two-factor authentication"
        ]
    elif total_score >= 40:
        risk_level = "🟡 MEDIUM RISK"
        recommendations = [
            "⚠️ Security improvements needed",
            "🔑 Strengthen your passwords",
            "🔗 Be cautious with unknown links",
            "📡 Verify WiFi network authenticity"
        ]
    elif total_score >= 20:
        risk_level = "🟢 LOW RISK"
        recommendations = [
            "✅ Good security practices",
            "🔑 Keep passwords updated regularly",
            "🔗 Stay vigilant against phishing",
            "📡 Use VPN on public networks"
        ]
    else:
        risk_level = "🔵 VERY LOW RISK"
        recommendations = [
            "✅ Excellent security posture!",
            "🔒 Continue following best practices",
            "📚 Stay informed about new threats"
        ]

    return risk_level, recommendations
