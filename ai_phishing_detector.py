import pickle
import os
import numpy as np
from urllib.parse import urlparse
import re

class AIPhishingDetector:
    """
    AI-based phishing URL detection using machine learning.
    Uses URL features like length, special characters, domain age indicators, etc.
    """
    
    def __init__(self):
        self.model_trained = False
        self.model = None
        
    def extract_features(self, url):
        """
        Extract features from URL for ML prediction.
        Returns a feature vector.
        """
        features = []
        
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            path = parsed.path
            
            # Feature 1: URL length
            features.append(len(url))
            
            # Feature 2: Domain length
            features.append(len(domain))
            
            # Feature 3: Has HTTPS
            features.append(1 if url.startswith('https://') else 0)
            
            # Feature 4: Has IP address
            ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
            features.append(1 if re.search(ip_pattern, url) else 0)
            
            # Feature 5: Number of subdomains
            features.append(domain.count('.'))
            
            # Feature 6: Has suspicious characters (@, -, _)
            features.append(url.count('@') + url.count('-') + url.count('_'))
            
            # Feature 7: URL depth (number of slashes)
            features.append(url.count('/'))
            
            # Feature 8: Has digits in domain
            features.append(1 if any(c.isdigit() for c in domain) else 0)
            
            # Feature 9: Length of path
            features.append(len(path))
            
            # Feature 10: Has suspicious keywords
            suspicious = ['login', 'verify', 'bank', 'secure', 'account', 'update', 'confirm', 'signin']
            features.append(sum(1 for word in suspicious if word in url.lower()))
            
            # Feature 11: Has double extension
            features.append(1 if url.count('.') > 2 else 0)
            
            # Feature 12: Domain age indicator (new domains often suspicious)
            features.append(1 if len(domain) > 20 else 0)
            
            return np.array(features).reshape(1, -1)
            
        except Exception as e:
            print(f"Error extracting features: {e}")
            return np.zeros((1, 12))
    
    def train_model(self):
        """
        Train the AI model with sample dataset.
        In production, you'd use a real dataset like PhishTank.
        """
        from sklearn.ensemble import RandomForestClassifier
        
        # Sample training data (URL features + labels)
        # Features: [url_len, domain_len, https, has_ip, subdomains, suspicious_chars, 
        #            url_depth, domain_digits, path_len, suspicious_keywords, double_ext, long_domain]
        # Label: 0 = Safe, 1 = Phishing
        
        X_train = np.array([
            # Safe URLs
            [30, 15, 1, 0, 2, 0, 3, 0, 10, 0, 0, 0],  # google.com
            [35, 18, 1, 0, 2, 0, 4, 0, 15, 0, 0, 0],  # github.com
            [28, 12, 1, 0, 1, 0, 2, 0, 8, 0, 0, 0],   # stackoverflow.com
            [40, 20, 1, 0, 3, 1, 5, 0, 20, 0, 0, 0],  # amazon.com
            [32, 16, 1, 0, 2, 0, 3, 0, 12, 0, 0, 0],  # microsoft.com
            
            # Phishing URLs
            [65, 30, 0, 1, 5, 3, 8, 1, 35, 4, 1, 1],  # suspicious IP with login
            [70, 35, 0, 0, 6, 4, 9, 1, 40, 5, 1, 1],  # long suspicious URL
            [55, 25, 0, 0, 4, 2, 7, 1, 30, 3, 1, 1],  # verify-account scam
            [80, 40, 0, 1, 7, 5, 10, 1, 45, 6, 1, 1], # complex phishing
            [60, 28, 0, 0, 5, 3, 8, 1, 32, 4, 1, 1],  # bank-login fake
        ])
        
        y_train = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        
        # Train Random Forest model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        self.model_trained = True
        
        # Save model
        self.save_model()
        
        return True
    
    def predict(self, url):
        """
        Predict if URL is phishing or safe.
        Returns: (prediction, confidence, risk_score)
        """
        if not self.model_trained:
            # Try to load trained model
            if not self.load_model():
                # Train new model if none exists
                self.train_model()
        
        # Extract features
        features = self.extract_features(url)
        
        # Predict
        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]
        confidence = max(probabilities) * 100
        
        # Calculate risk score
        if prediction == 1:  # Phishing
            risk_score = int(confidence)
            status = "🔴 PHISHING DETECTED"
        else:  # Safe
            risk_score = int(100 - confidence)
            status = "🟢 SAFE"
        
        return status, risk_score, confidence
    
    def save_model(self, filename='ai_phishing_model.pkl'):
        """Save trained model to file"""
        if self.model:
            with open(filename, 'wb') as f:
                pickle.dump(self.model, f)
            print(f"✅ Model saved to {filename}")
    
    def load_model(self, filename='ai_phishing_model.pkl'):
        """Load trained model from file"""
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.model = pickle.load(f)
            self.model_trained = True
            print(f"✅ Model loaded from {filename}")
            return True
        return False


# Quick test
if __name__ == "__main__":
    detector = AIPhishingDetector()
    
    # Train model
    print("Training AI Phishing Detection Model...")
    detector.train_model()
    
    # Test URLs
    test_urls = [
        "https://www.google.com",
        "http://login-verify-bank-account.com/signin",
        "https://github.com/user/repo",
        "http://192.168.1.1/secure-update"
    ]
    
    print("\n" + "="*60)
    print("AI PHISHING DETECTION TEST")
    print("="*60)
    
    for url in test_urls:
        status, risk, confidence = detector.predict(url)
        print(f"\nURL: {url}")
        print(f"Status: {status}")
        print(f"Risk Score: {risk}/100")
        print(f"Confidence: {confidence:.1f}%")
