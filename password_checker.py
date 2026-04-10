import re

def check_password(password):
    """
    Check password strength based on multiple criteria.
    Returns: (strength_level, risk_score)
    """
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters")

    # Uppercase check
    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter")

    # Number check
    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number")

    # Special character check
    if re.search("[@#$%^&*!]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (@#$%^&*!)")

    # Determine strength level
    if score <= 1:
        strength = "Weak"
        risk_score = 75
    elif score == 2:
        strength = "Medium"
        risk_score = 40
    elif score == 3:
        strength = "Strong"
        risk_score = 20
    else:
        strength = "Very Strong"
        risk_score = 10

    return strength, risk_score, feedback
