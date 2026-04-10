"""
Ethical Cybersecurity Framework
Educational module on legal vs illegal cybersecurity practices
For educational purposes only
"""

from colorama import init, Fore, Style
import time

init(autoreset=True)

class EthicalCybersecurityFramework:
    """
    Comprehensive guide to ethical and legal cybersecurity practices
    Educates users on what's legal vs illegal
    """
    
    def __init__(self):
        self.illegal_practices = [
            {
                'category': '🚫 Unauthorized Access',
                'practices': [
                    'Cracking passwords on devices you don\'t own',
                    'Bypassing security without authorization',
                    'Accessing others\' devices without permission',
                    'Hacking into accounts that aren\'t yours',
                    'Unauthorized network access',
                    'Breaking into secured systems'
                ],
                'laws_violated': [
                    'Computer Fraud and Abuse Act (CFAA)',
                    'Cybercrime Prevention Act',
                    'Unauthorized Access laws',
                    'Privacy violations'
                ],
                'consequences': [
                    'Criminal charges (felony)',
                    'Heavy fines ($100,000+)',
                    'Imprisonment (1-20 years)',
                    'Permanent criminal record',
                    'Civil lawsuits'
                ]
            },
            {
                'category': '🚫 Illegal Exploitation',
                'practices': [
                    'Exploiting vulnerabilities without permission',
                    'Using exploits for malicious purposes',
                    'Creating/distributing malware',
                    'Ransomware attacks',
                    'Data theft and selling',
                    'Denial of Service attacks'
                ],
                'laws_violated': [
                    'Malware creation laws',
                    'Data protection regulations',
                    'Cyber terrorism laws',
                    'Intellectual property theft'
                ],
                'consequences': [
                    'Federal prosecution',
                    'Decades in prison',
                    'Millions in fines',
                    'Asset forfeiture',
                    'International warrants'
                ]
            },
            {
                'category': '🚫 Privacy Violations',
                'practices': [
                    'Spying on others without consent',
                    'Installing keyloggers on others\' devices',
                    'Intercepting communications illegally',
                    'Stalking through digital means',
                    'Unauthorized surveillance',
                    'Data harvesting without permission'
                ],
                'laws_violated': [
                    'Wiretapping laws',
                    'Privacy Protection Act',
                    'GDPR (Europe)',
                    'CCPA (California)',
                    'Electronic Communications Privacy Act'
                ],
                'consequences': [
                    'Privacy violation charges',
                    'Restraining orders',
                    'Civil damages',
                    'Regulatory fines',
                    'Criminal prosecution'
                ]
            },
            {
                'category': '🚫 Encryption Breaking',
                'practices': [
                    'Breaking encryption without authorization',
                    'Decrypting others\' protected data',
                    'Bypassing DRM illegally',
                    'Cracking protected systems',
                    'Unauthorized decryption',
                    'Circumventing security measures'
                ],
                'laws_violated': [
                    'Digital Millennium Copyright Act (DMCA)',
                    'Encryption laws',
                    'Copyright infringement',
                    'Trade secret theft'
                ],
                'consequences': [
                    'DMCA violations',
                    'Copyright infringement charges',
                    'Federal prosecution',
                    'Heavy financial penalties',
                    'Potential imprisonment'
                ]
            }
        ]
        
        self.legal_practices = [
            {
                'category': '✅ Authorized Security Testing',
                'practices': [
                    'Penetration testing WITH written permission',
                    'Bug bounty programs (authorized)',
                    'Security audits for clients',
                    'Vulnerability research (responsible disclosure)',
                    'Red team exercises (contracted)',
                    'Security consulting (authorized)'
                ],
                'requirements': [
                    'Written authorization/contract',
                    'Clearly defined scope',
                    'Rules of engagement document',
                    'Legal agreement signed',
                    'Owner consent documented'
                ],
                'certifications': [
                    'CEH (Certified Ethical Hacker)',
                    'OSCP (Offensive Security Certified Professional)',
                    'GPEN (GIAC Penetration Tester)',
                    'CompTIA PenTest+'
                ]
            },
            {
                'category': '✅ Defensive Security',
                'practices': [
                    'Network monitoring and defense',
                    'Incident response',
                    'Security awareness training',
                    'Vulnerability assessment',
                    'Security architecture design',
                    'Threat intelligence analysis'
                ],
                'requirements': [
                    'Work for organization being protected',
                    'Authorized by management',
                    'Within job scope',
                    'Follow company policies',
                    'Legal compliance maintained'
                ],
                'certifications': [
                    'CompTIA Security+',
                    'CISSP (Certified Information Systems Security Professional)',
                    'CISM (Certified Information Security Manager)',
                    'GCIH (GIAC Certified Incident Handler)'
                ]
            },
            {
                'category': '✅ Educational & Research',
                'practices': [
                    'Learning cybersecurity in controlled labs',
                    'CTF (Capture The Flag) competitions',
                    'Home lab experiments',
                    'Academic research',
                    'Security tool development',
                    'Writing educational content'
                ],
                'requirements': [
                    'Use your own equipment',
                    'Isolated lab environments',
                    'No unauthorized access',
                    'Educational purpose only',
                    'Legal boundaries respected'
                ],
                'platforms': [
                    'HackTheBox (legal platform)',
                    'TryHackMe (educational)',
                    'CTF competitions',
                    'Home virtual labs',
                    'Bug bounty programs'
                ]
            },
            {
                'category': '✅ User Education & Compliance',
                'practices': [
                    'Teaching security best practices',
                    'Creating educational tools',
                    'Developing security awareness programs',
                    'Writing security documentation',
                    'Conducting legal training sessions',
                    'Building defensive security tools'
                ],
                'requirements': [
                    'Accurate information',
                    'Legal compliance',
                    'Ethical guidelines',
                    'Professional standards',
                    'User consent'
                ],
                'impact': [
                    'Improves overall security',
                    'Prevents cyber attacks',
                    'Educates users',
                    'Builds security culture',
                    'Reduces risk'
                ]
            }
        ]
    
    def display_illegal_practices(self):
        """Show what's ILLEGAL and why"""
        print(Fore.RED + Style.BRIGHT + "\n" + "="*80)
        print(Fore.RED + Style.BRIGHT + "🚫 ILLEGAL CYBERSECURITY PRACTICES (NEVER DO THESE)")
        print(Fore.RED + Style.BRIGHT + "="*80)
        
        for item in self.illegal_practices:
            print(Fore.MAGENTA + f"\n{item['category']}")
            print(Fore.WHITE + "-"*80)
            
            print(Fore.YELLOW + "\n❌ Illegal Practices:")
            for practice in item['practices']:
                print(f"  • {practice}")
            
            print(Fore.RED + "\n⚖️ Laws Violated:")
            for law in item['laws_violated']:
                print(f"  • {law}")
            
            print(Fore.RED + "\n💀 Consequences:")
            for consequence in item['consequences']:
                print(f"  • {consequence}")
            
            print()
        
        print(Fore.RED + Style.BRIGHT + "\n⚠️  REMEMBER: These practices are CRIMES with serious consequences!")
    
    def display_legal_practices(self):
        """Show what's LEGAL and encouraged"""
        print(Fore.GREEN + Style.BRIGHT + "\n" + "="*80)
        print(Fore.GREEN + Style.BRIGHT + "✅ LEGAL & ETHICAL CYBERSECURITY PRACTICES")
        print(Fore.GREEN + Style.BRIGHT + "="*80)
        
        for item in self.legal_practices:
            print(Fore.CYAN + f"\n{item['category']}")
            print(Fore.WHITE + "-"*80)
            
            print(Fore.GREEN + "\n✅ Legal Practices:")
            for practice in item['practices']:
                print(f"  • {practice}")
            
            print(Fore.YELLOW + "\n📋 Requirements:")
            for req in item['requirements']:
                print(f"  • {req}")
            
            if 'certifications' in item:
                print(Fore.MAGENTA + "\n🎓 Recommended Certifications:")
                for cert in item['certifications']:
                    print(f"  • {cert}")
            
            if 'platforms' in item:
                print(Fore.CYAN + "\n💻 Legal Practice Platforms:")
                for platform in item['platforms']:
                    print(f"  • {platform}")
            
            if 'impact' in item:
                print(Fore.GREEN + "\n🌟 Positive Impact:")
                for impact in item['impact']:
                    print(f"  • {impact}")
            
            print()
    
    def display_comparison(self):
        """Side-by-side comparison"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*80)
        print(Fore.CYAN + Style.BRIGHT + "📊 ILLEGAL vs LEGAL: QUICK COMPARISON")
        print(Fore.CYAN + Style.BRIGHT + "="*80)
        
        comparisons = [
            {
                'scenario': 'Testing Network Security',
                'illegal': 'Scanning networks you don\'t own without permission',
                'legal': 'Scanning your own network or with written authorization'
            },
            {
                'scenario': 'Password Testing',
                'illegal': 'Cracking passwords on others\' accounts/devices',
                'legal': 'Testing password strength on your own systems'
            },
            {
                'scenario': 'Vulnerability Discovery',
                'illegal': 'Exploiting found vulnerabilities for personal gain',
                'legal': 'Responsible disclosure to vendor/bug bounty'
            },
            {
                'scenario': 'Device Access',
                'illegal': 'Bypassing security on devices you don\'t own',
                'legal': 'Recovering your own device with proof of ownership'
            },
            {
                'scenario': 'Data Access',
                'illegal': 'Accessing others\' private data without consent',
                'legal': 'Accessing data you own or have authorization for'
            },
            {
                'scenario': 'Tool Development',
                'illegal': 'Creating malware or hacking tools for attacks',
                'legal': 'Building defensive tools and educational resources'
            }
        ]
        
        for comp in comparisons:
            print(Fore.MAGENTA + f"\nScenario: {comp['scenario']}")
            print(Fore.WHITE + "-"*80)
            print(Fore.RED + f"  ❌ ILLEGAL: {comp['illegal']}")
            print(Fore.GREEN + f"  ✅ LEGAL:  {comp['legal']}")
            print()
    
    def display_career_path(self):
        """Show legitimate cybersecurity career path"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*80)
        print(Fore.CYAN + Style.BRIGHT + "🎓 LEGAL CYBERSECURITY CAREER PATH")
        print(Fore.CYAN + Style.BRIGHT + "="*80)
        
        careers = [
            {
                'role': 'Penetration Tester',
                'salary': '$70,000 - $120,000/year',
                'description': 'Legally test security with authorization',
                'requirements': ['CEH or OSCP certification', 'Written contracts', 'Legal authorization']
            },
            {
                'role': 'Security Analyst',
                'salary': '$60,000 - $100,000/year',
                'description': 'Monitor and defend against cyber threats',
                'requirements': ['Security+ certification', 'Analytical skills', 'Incident response']
            },
            {
                'role': 'Security Consultant',
                'salary': '$80,000 - $150,000/year',
                'description': 'Advise organizations on security',
                'requirements': ['CISSP certification', 'Experience', 'Client trust']
            },
            {
                'role': 'Bug Bounty Hunter',
                'salary': '$10,000 - $500,000+/year',
                'description': 'Find vulnerabilities legally for rewards',
                'requirements': ['Technical skills', 'Platforms: HackerOne, Bugcrowd', 'Responsible disclosure']
            },
            {
                'role': 'Security Researcher',
                'salary': '$70,000 - $130,000/year',
                'description': 'Research new security threats',
                'requirements': ['Advanced degree', 'Publications', 'Ethical guidelines']
            }
        ]
        
        for career in careers:
            print(Fore.MAGENTA + f"\n💼 {career['role']}")
            print(Fore.WHITE + "-"*80)
            print(Fore.YELLOW + f"  💰 Salary: {career['salary']}")
            print(Fore.GREEN + f"  📝 Description: {career['description']}")
            print(Fore.CYAN + f"  📋 Requirements:")
            for req in career['requirements']:
                print(f"    • {req}")
            print()
    
    def display_legal_framework(self):
        """Show key cybersecurity laws"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*80)
        print(Fore.CYAN + Style.BRIGHT + "⚖️ KEY CYBERSECURITY LAWS TO KNOW")
        print(Fore.CYAN + Style.BRIGHT + "="*80)
        
        laws = [
            {
                'name': 'Computer Fraud and Abuse Act (CFAA)',
                'country': 'United States',
                'covers': 'Unauthorized computer access',
                'penalty': 'Up to 20 years imprisonment'
            },
            {
                'name': 'General Data Protection Regulation (GDPR)',
                'country': 'European Union',
                'covers': 'Data protection and privacy',
                'penalty': 'Up to €20 million or 4% of revenue'
            },
            {
                'name': 'Digital Millennium Copyright Act (DMCA)',
                'country': 'United States',
                'covers': 'Digital copyright protection',
                'penalty': 'Up to $500,000 fines, 5 years prison'
            },
            {
                'name': 'Cybercrime Prevention Act',
                'country': 'Various Countries',
                'covers': 'Online criminal activities',
                'penalty': 'Varies by country (often 5-20 years)'
            },
            {
                'name': 'Electronic Communications Privacy Act',
                'country': 'United States',
                'covers': 'Wiretapping and interception',
                'penalty': 'Up to 5 years imprisonment'
            }
        ]
        
        for law in laws:
            print(Fore.MAGENTA + f"\n📜 {law['name']}")
            print(Fore.WHITE + "-"*80)
            print(Fore.YELLOW + f"  🌍 Country/Region: {law['country']}")
            print(Fore.GREEN + f"  📋 Covers: {law['covers']}")
            print(Fore.RED + f"  ⚠️ Penalty: {law['penalty']}")
            print()
    
    def display_menu(self):
        """Show main menu"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*80)
        print(Fore.CYAN + Style.BRIGHT + "🛡️ ETHICAL CYBERSECURITY FRAMEWORK")
        print(Fore.CYAN + Style.BRIGHT + "="*80)
        print()
        print(Fore.WHITE + "Choose a topic:")
        print()
        print(Fore.RED + "1. 🚫 Illegal Practices (What NOT to do)")
        print(Fore.GREEN + "2. ✅ Legal Practices (What TO do)")
        print(Fore.YELLOW + "3. 📊 Illegal vs Legal Comparison")
        print(Fore.MAGENTA + "4. 🎓 Legal Career Path")
        print(Fore.CYAN + "5. ⚖️ Cybersecurity Laws")
        print(Fore.WHITE + "0. Exit")
        print()
    
    def run(self):
        """Main loop"""
        options = {
            '1': self.display_illegal_practices,
            '2': self.display_legal_practices,
            '3': self.display_comparison,
            '4': self.display_career_path,
            '5': self.display_legal_framework
        }
        
        while True:
            self.display_menu()
            choice = input(Fore.YELLOW + "Enter your choice (0-5): " + Style.RESET_ALL).strip()
            
            if choice == '0':
                print(Fore.CYAN + "\n🛡️ Remember: Always practice ethical cybersecurity!")
                print(Fore.CYAN + "📚 Stay legal, stay professional, stay ethical!")
                print(Fore.GREEN + "\n✅ Your Future in Cybersecurity Starts with Ethics! 🚀\n")
                break
            elif choice in options:
                options[choice]()
                input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
            else:
                print(Fore.RED + "\n❌ Invalid choice. Please try again.")
                time.sleep(1)


if __name__ == "__main__":
    framework = EthicalCybersecurityFramework()
    framework.run()
