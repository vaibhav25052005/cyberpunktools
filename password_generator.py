import secrets
import string
import hashlib
import json
import os
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

class PasswordGenerator:
    """
    Advanced Password Generator and Manager
    Generates secure passwords and manages them with encryption
    """
    
    def __init__(self, storage_file="passwords.json"):
        self.storage_file = storage_file
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)
        
    def _load_or_generate_key(self):
        """Load encryption key from file or generate new one"""
        key_file = "encryption.key"
        
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            return key
    
    def generate_password(self, length=16, use_uppercase=True, use_lowercase=True, 
                         use_digits=True, use_symbols=True, exclude_chars="",
                         must_include=None):
        """
        Generate a cryptographically secure password
        Returns: (password, strength_info)
        """
        # Build character pool
        char_pool = ""
        
        if use_uppercase:
            char_pool += string.ascii_uppercase
        if use_lowercase:
            char_pool += string.ascii_lowercase
        if use_digits:
            char_pool += string.digits
        if use_symbols:
            char_pool += string.punctuation
        
        # Remove excluded characters
        if exclude_chars:
            char_pool = ''.join(c for c in char_pool if c not in exclude_chars)
        
        if not char_pool:
            raise ValueError("No characters available in pool")
        
        # Generate password
        password = ''.join(secrets.choice(char_pool) for _ in range(length))
        
        # Ensure must_include characters are present
        if must_include:
            password_list = list(password)
            for char in must_include:
                if char not in password_list:
                    # Replace a random character
                    idx = secrets.randbelow(len(password_list))
                    password_list[idx] = char
            password = ''.join(password_list)
        
        # Analyze strength
        strength_info = self.analyze_password_strength(password)
        
        return password, strength_info
    
    def analyze_password_strength(self, password):
        """Analyze password strength and return detailed info"""
        info = {
            "Length": len(password),
            "Has Uppercase": any(c.isupper() for c in password),
            "Has Lowercase": any(c.islower() for c in password),
            "Has Digits": any(c.isdigit() for c in password),
            "Has Symbols": any(c in string.punctuation for c in password),
            "Unique Characters": len(set(password)),
            "Entropy": self.calculate_entropy(password)
        }
        
        # Calculate strength score
        score = 0
        
        # Length scoring
        if len(password) >= 16:
            score += 40
        elif len(password) >= 12:
            score += 30
        elif len(password) >= 8:
            score += 20
        else:
            score += 10
        
        # Character diversity
        if info["Has Uppercase"]:
            score += 15
        if info["Has Lowercase"]:
            score += 15
        if info["Has Digits"]:
            score += 15
        if info["Has Symbols"]:
            score += 15
        
        # Uniqueness bonus
        uniqueness_ratio = info["Unique Characters"] / len(password) if len(password) > 0 else 0
        if uniqueness_ratio >= 0.8:
            score += 10
        elif uniqueness_ratio >= 0.6:
            score += 5
        
        # Determine strength level
        if score >= 90:
            strength = "VERY STRONG"
        elif score >= 75:
            strength = "STRONG"
        elif score >= 50:
            strength = "MODERATE"
        elif score >= 30:
            strength = "WEAK"
        else:
            strength = "VERY WEAK"
        
        info["Strength"] = strength
        info["Score"] = score
        
        # Time to crack estimate
        info["Crack Time"] = self.estimate_crack_time(password)
        
        return info
    
    def calculate_entropy(self, password):
        """Calculate password entropy in bits"""
        charset_size = 0
        
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in string.punctuation for c in password):
            charset_size += 32
        
        if charset_size == 0:
            return 0
        
        entropy = len(password) * (charset_size.bit_length())
        return entropy
    
    def estimate_crack_time(self, password):
        """Estimate time to crack password (assuming 10 billion guesses/sec)"""
        charset_size = 0
        
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in string.punctuation for c in password):
            charset_size += 32
        
        if charset_size == 0:
            return "Instant"
        
        # Total combinations
        combinations = charset_size ** len(password)
        
        # Assuming 10 billion guesses per second (powerful GPU cluster)
        guesses_per_second = 10_000_000_000
        seconds_to_crack = combinations / guesses_per_second
        
        if seconds_to_crack < 1:
            return "Instantly"
        elif seconds_to_crack < 60:
            return f"{int(seconds_to_crack)} seconds"
        elif seconds_to_crack < 3600:
            return f"{int(seconds_to_crack / 60)} minutes"
        elif seconds_to_crack < 86400:
            return f"{int(seconds_to_crack / 3600)} hours"
        elif seconds_to_crack < 31536000:
            return f"{int(seconds_to_crack / 86400)} days"
        elif seconds_to_crack < 31536000 * 1000:
            return f"{int(seconds_to_crack / 31536000)} years"
        else:
            return "Centuries+"
    
    def generate_passphrase(self, num_words=6, separator="-", capitalize=True, add_number=True):
        """
        Generate a memorable passphrase using common words
        Returns: (passphrase, strength_info)
        """
        # Common English words (subset for demonstration)
        word_list = [
            "correct", "horse", "battery", "staple", "monkey", "dragon",
            "phoenix", "thunder", "shadow", "crystal", "forest", "ocean",
            "mountain", "river", "sunset", "cosmos", "galaxy", "quantum",
            "digital", "cyber", "secure", "alpha", "bravo", "charlie",
            "delta", "echo", "foxtrot", "golf", "hotel", "india",
            "juliet", "kilo", "lima", "mike", "november", "oscar",
            "papa", "quebec", "romeo", "sierra", "tango", "uniform",
            "victor", "whiskey", "xray", "yankee", "zulu", "ninja",
            "warrior", "knight", "wizard", "falcon", "eagle", "tiger",
            "lion", "bear", "wolf", "shark", "whale", "dolphin"
        ]
        
        # Select random words
        selected_words = [secrets.choice(word_list) for _ in range(num_words)]
        
        # Capitalize if requested
        if capitalize:
            selected_words = [word.capitalize() for word in selected_words]
        
        # Add number if requested
        if add_number:
            random_number = secrets.randbelow(1000)
            selected_words.append(str(random_number))
        
        passphrase = separator.join(selected_words)
        
        # Analyze strength
        strength_info = self.analyze_password_strength(passphrase)
        
        return passphrase, strength_info
    
    def store_password(self, service, username, password, url="", notes=""):
        """
        Store password securely (encrypted)
        """
        passwords_data = self._load_passwords()
        
        # Create entry
        entry = {
            "Service": service,
            "Username": username,
            "Password": self._encrypt(password),
            "URL": url,
            "Notes": notes,
            "Created": datetime.now().isoformat(),
            "Last Modified": datetime.now().isoformat()
        }
        
        # Check if service already exists
        existing_idx = None
        for idx, existing in enumerate(passwords_data):
            if existing["Service"].lower() == service.lower():
                existing_idx = idx
                break
        
        if existing_idx is not None:
            passwords_data[existing_idx] = entry
        else:
            passwords_data.append(entry)
        
        self._save_passwords(passwords_data)
        return True
    
    def retrieve_password(self, service):
        """Retrieve and decrypt password for a service"""
        passwords_data = self._load_passwords()
        
        for entry in passwords_data:
            if entry["Service"].lower() == service.lower():
                return {
                    "Service": entry["Service"],
                    "Username": entry["Username"],
                    "Password": self._decrypt(entry["Password"]),
                    "URL": entry.get("URL", ""),
                    "Notes": entry.get("Notes", ""),
                    "Created": entry.get("Created", ""),
                    "Last Modified": entry.get("Last Modified", "")
                }
        
        return None
    
    def list_services(self):
        """List all stored services"""
        passwords_data = self._load_passwords()
        return [entry["Service"] for entry in passwords_data]
    
    def delete_password(self, service):
        """Delete stored password for a service"""
        passwords_data = self._load_passwords()
        
        new_data = [entry for entry in passwords_data if entry["Service"].lower() != service.lower()]
        
        if len(new_data) < len(passwords_data):
            self._save_passwords(new_data)
            return True
        
        return False
    
    def generate_password_report(self):
        """Generate a report of stored passwords (without revealing them)"""
        passwords_data = self._load_passwords()
        
        report = {
            "Total Passwords": len(passwords_data),
            "Generated At": datetime.now().isoformat(),
            "Services": []
        }
        
        for entry in passwords_data:
            password = self._decrypt(entry["Password"])
            strength = self.analyze_password_strength(password)
            
            report["Services"].append({
                "Service": entry["Service"],
                "Username": entry["Username"],
                "Strength": strength["Strength"],
                "Score": strength["Score"],
                "Length": strength["Length"],
                "Created": entry.get("Created", "")
            })
        
        return report
    
    def check_password_health(self):
        """Check overall health of stored passwords"""
        passwords_data = self._load_passwords()
        
        if not passwords_data:
            return {"Status": "No passwords stored"}
        
        health_report = {
            "Total": len(passwords_data),
            "Strong": 0,
            "Moderate": 0,
            "Weak": 0,
            "Duplicate Passwords": 0,
            "Short Passwords": 0,
            "Recommendations": []
        }
        
        passwords_list = []
        
        for entry in passwords_data:
            password = self._decrypt(entry["Password"])
            passwords_list.append(password)
            
            strength = self.analyze_password_strength(password)
            
            if strength["Score"] >= 75:
                health_report["Strong"] += 1
            elif strength["Score"] >= 50:
                health_report["Moderate"] += 1
            else:
                health_report["Weak"] += 1
            
            if len(password) < 12:
                health_report["Short Passwords"] += 1
        
        # Check for duplicates
        unique_passwords = set(passwords_list)
        health_report["Duplicate Passwords"] = len(passwords_list) - len(unique_passwords)
        
        # Generate recommendations
        if health_report["Weak"] > 0:
            health_report["Recommendations"].append(
                f"⚠️ {health_report['Weak']} weak password(s) should be updated"
            )
        
        if health_report["Duplicate Passwords"] > 0:
            health_report["Recommendations"].append(
                f"⚠️ {health_report['Duplicate Passwords']} duplicate password(s) detected"
            )
        
        if health_report["Short Passwords"] > 0:
            health_report["Recommendations"].append(
                f"ℹ️ {health_report['Short Passwords']} password(s) are too short (< 12 chars)"
            )
        
        if not health_report["Recommendations"]:
            health_report["Recommendations"].append("✅ All passwords are strong and unique!")
        
        return health_report
    
    def _encrypt(self, plaintext):
        """Encrypt plaintext"""
        return self.cipher.encrypt(plaintext.encode()).decode()
    
    def _decrypt(self, ciphertext):
        """Decrypt ciphertext"""
        return self.cipher.decrypt(ciphertext.encode()).decode()
    
    def _load_passwords(self):
        """Load passwords from file"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _save_passwords(self, passwords_data):
        """Save passwords to file"""
        with open(self.storage_file, 'w') as f:
            json.dump(passwords_data, f, indent=2)
    
    def format_password_info(self, password, strength_info):
        """Format password and strength information for display"""
        output = []
        output.append("="*60)
        output.append("GENERATED PASSWORD")
        output.append("="*60)
        output.append(f"Password: {password}")
        output.append(f"Length: {strength_info['Length']}")
        output.append(f"Strength: {strength_info['Strength']}")
        output.append(f"Score: {strength_info['Score']}/100")
        output.append(f"Entropy: {strength_info['Entropy']} bits")
        output.append(f"Crack Time: {strength_info['Crack Time']}")
        output.append(f"Unique Characters: {strength_info['Unique Characters']}")
        output.append("="*60)
        
        return '\n'.join(output)


# Quick test
if __name__ == "__main__":
    from colorama import init, Fore, Style
    init(autoreset=True)
    
    generator = PasswordGenerator()
    
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    print(Fore.CYAN + Style.BRIGHT + "🔐 PASSWORD GENERATOR & MANAGER")
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    
    # Generate a strong password
    print(Fore.MAGENTA + "\n📌 Generating strong password...")
    password, strength = generator.generate_password(length=20)
    print(Fore.WHITE + generator.format_password_info(password, strength))
    
    # Generate a passphrase
    print(Fore.MAGENTA + "\n📌 Generating memorable passphrase...")
    passphrase, pass_strength = generator.generate_passphrase(num_words=5)
    print(Fore.WHITE + generator.format_password_info(passphrase, pass_strength))
