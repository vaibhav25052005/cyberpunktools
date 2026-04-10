"""
Legal Password Recovery Guide
Provides legitimate methods to recover YOUR OWN device password
"""

from colorama import init, Fore, Style
import time

init(autoreset=True)

class PasswordRecoveryGuide:
    """
    LEGAL password recovery methods for device owners
    Only for devices you legally own
    """
    
    def __init__(self):
        self.methods = {
            'android': self.android_recovery,
            'iphone': self.iphone_recovery,
            'windows': self.windows_recovery,
            'general': self.general_tips
        }
    
    def display_menu(self):
        """Show recovery options"""
        print(Fore.CYAN + Style.BRIGHT + "="*70)
        print(Fore.CYAN + Style.BRIGHT + "🔐 LEGAL PASSWORD RECOVERY ASSISTANT")
        print(Fore.CYAN + Style.BRIGHT + "="*70)
        print()
        print(Fore.YELLOW + "⚠️  DISCLAIMER: Only use these methods on devices YOU OWN")
        print(Fore.YELLOW + "⚠️  Unauthorized access to others' devices is ILLEGAL")
        print()
        print(Fore.WHITE + "Select your device type:")
        print()
        print(Fore.GREEN + "1. 🤖 Android Device")
        print(Fore.GREEN + "2. 🍎 iPhone/iPad")
        print(Fore.GREEN + "3. 💻 Windows Computer")
        print(Fore.GREEN + "4. 📋 General Recovery Tips")
        print(Fore.GREEN + "0. Exit")
        print()
    
    def android_recovery(self):
        """Legal Android recovery methods"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*70)
        print(Fore.CYAN + Style.BRIGHT + "🤖 ANDROID PASSWORD RECOVERY (LEGAL METHODS)")
        print(Fore.CYAN + Style.BRIGHT + "="*70)
        
        methods = [
            {
                'name': 'Google Find My Device',
                'data_loss': True,
                'difficulty': 'Easy',
                'steps': [
                    'Visit: google.com/android/find',
                    'Sign in with your Google account',
                    'Select your locked device',
                    'Click "Erase Device"',
                    'Device will be reset to factory settings',
                    'Set up device again with new password',
                    'Restore data from Google backup if available'
                ],
                'requirements': [
                    'Device must be connected to internet',
                    'Location services enabled',
                    'Signed into Google account',
                    'Find My Device was enabled'
                ]
            },
            {
                'name': 'Samsung Find My Mobile',
                'data_loss': False,
                'difficulty': 'Easy',
                'steps': [
                    'Visit: smartthingsfind.samsung.com',
                    'Sign in with Samsung account',
                    'Select your device',
                    'Click "Unlock"',
                    'Enter Samsung account password',
                    'Device will be unlocked WITHOUT data loss'
                ],
                'requirements': [
                    'Samsung device only',
                    'Samsung account signed in',
                    'Remote unlock enabled',
                    'Internet connection active'
                ]
            },
            {
                'name': 'Recovery Mode (Factory Reset)',
                'data_loss': True,
                'difficulty': 'Medium',
                'steps': [
                    'Power off the device completely',
                    'Boot into Recovery Mode:',
                    '  - Most phones: Volume Up + Power button',
                    '  - Samsung: Volume Up + Bixby + Power',
                    'Navigate to "Wipe data/factory reset"',
                    'Confirm with power button',
                    'Select "Reboot system now"',
                    'Set up as new device',
                    'Restore from backup if available'
                ],
                'requirements': [
                    'Physical access to device',
                    'Will erase ALL data',
                    'Google account credentials (after reset)',
                    'Backup recommended before attempt'
                ]
            },
            {
                'name': 'ADB Method (USB Debugging Enabled)',
                'data_loss': False,
                'difficulty': 'Hard',
                'steps': [
                    'Requires USB debugging already enabled',
                    'Connect device to computer via USB',
                    'Open command prompt/terminal',
                    'Type: adb devices (verify connection)',
                    'Type: adb shell rm /data/system/gesture.key',
                    'Reboot device',
                    'Password should be removed'
                ],
                'requirements': [
                    'USB debugging MUST be enabled beforehand',
                    'ADB tools installed on computer',
                    'USB connection to computer',
                    'Technical knowledge required'
                ]
            }
        ]
        
        for i, method in enumerate(methods, 1):
            print(Fore.MAGENTA + f"\nMethod {i}: {method['name']}")
            print(Fore.WHITE + "-"*70)
            print(Fore.YELLOW + f"Data Loss: {'⚠️ YES' if method['data_loss'] else '✅ NO'}")
            print(Fore.YELLOW + f"Difficulty: {method['difficulty']}")
            print()
            print(Fore.GREEN + "Steps:")
            for j, step in enumerate(method['steps'], 1):
                print(f"  {j}. {step}")
            print()
            print(Fore.CYAN + "Requirements:")
            for req in method['requirements']:
                print(f"  • {req}")
            print()
    
    def iphone_recovery(self):
        """Legal iPhone recovery methods"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*70)
        print(Fore.CYAN + Style.BRIGHT + "🍎 iPHONE/IPAD PASSWORD RECOVERY (LEGAL METHODS)")
        print(Fore.CYAN + Style.BRIGHT + "="*70)
        
        methods = [
            {
                'name': 'iCloud Find My iPhone',
                'data_loss': True,
                'difficulty': 'Easy',
                'steps': [
                    'Visit: icloud.com/find',
                    'Sign in with Apple ID',
                    'Select your device from "All Devices"',
                    'Click "Erase iPhone/iPad"',
                    'Enter Apple ID password to confirm',
                    'Device will be erased and reset',
                    'Set up device again',
                    'Restore from iCloud backup during setup'
                ],
                'requirements': [
                    'Find My iPhone was enabled',
                    'Device connected to internet',
                    'Apple ID and password',
                    'iCloud backup (to restore data)'
                ]
            },
            {
                'name': 'Recovery Mode with iTunes/Finder',
                'data_loss': True,
                'difficulty': 'Medium',
                'steps': [
                    'Connect iPhone to computer with USB',
                    'Force restart into Recovery Mode:',
                    '  - iPhone 8+: Volume Up, Volume Down, hold Power',
                    '  - iPhone 7: Volume Down + Power',
                    '  - iPhone 6s: Home + Power',
                    'iTunes/Finder will detect recovery mode',
                    'Click "Restore" (NOT "Update")',
                    'Wait for restore to complete',
                    'Set up device again',
                    'Restore from backup if available'
                ],
                'requirements': [
                    'Computer with iTunes (Windows) or Finder (Mac)',
                    'USB cable',
                    'Apple ID password (after restore)',
                    'Backup recommended (data will be erased)'
                ]
            },
            {
                'name': 'Apple Support (With Proof of Purchase)',
                'data_loss': True,
                'difficulty': 'Easy',
                'steps': [
                    'Contact Apple Support: support.apple.com',
                    'Schedule appointment at Apple Store',
                    'Bring proof of purchase (receipt)',
                    'Bring valid photo ID',
                    'Explain situation to technician',
                    'They will assist with recovery',
                    'Data may not be recoverable'
                ],
                'requirements': [
                    'Original purchase receipt REQUIRED',
                    'Valid government-issued ID',
                    'Device serial number',
                    'AppleCare+ helpful but not required'
                ]
            }
        ]
        
        for i, method in enumerate(methods, 1):
            print(Fore.MAGENTA + f"\nMethod {i}: {method['name']}")
            print(Fore.WHITE + "-"*70)
            print(Fore.YELLOW + f"Data Loss: {'⚠️ YES' if method['data_loss'] else '✅ NO'}")
            print(Fore.YELLOW + f"Difficulty: {method['difficulty']}")
            print()
            print(Fore.GREEN + "Steps:")
            for j, step in enumerate(method['steps'], 1):
                print(f"  {j}. {step}")
            print()
            print(Fore.CYAN + "Requirements:")
            for req in method['requirements']:
                print(f"  • {req}")
            print()
    
    def windows_recovery(self):
        """Legal Windows password recovery"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*70)
        print(Fore.CYAN + Style.BRIGHT + "💻 WINDOWS PASSWORD RECOVERY (LEGAL METHODS)")
        print(Fore.CYAN + Style.BRIGHT + "="*70)
        
        methods = [
            {
                'name': 'Microsoft Account Reset',
                'data_loss': False,
                'difficulty': 'Easy',
                'steps': [
                    'Visit: account.live.com/password/reset',
                    'Enter your Microsoft email',
                    'Verify identity (email/phone code)',
                    'Create new password',
                    'Connect PC to internet',
                    'Sign in with new password'
                ],
                'requirements': [
                    'Using Microsoft account (not local)',
                    'Access to recovery email/phone',
                    'Internet connection',
                    'Account recovery info up to date'
                ]
            },
            {
                'name': 'Password Reset Disk',
                'data_loss': False,
                'difficulty': 'Easy',
                'steps': [
                    'Insert password reset USB drive',
                    'Click "Reset password" on login screen',
                    'Follow Password Reset Wizard',
                    'Create new password',
                    'Sign in with new password'
                ],
                'requirements': [
                    'Reset disk must be created BEFORE forgetting password',
                    'USB drive with reset disk',
                    'Physical access to computer'
                ]
            },
            {
                'name': 'Safe Mode with Administrator',
                'data_loss': False,
                'difficulty': 'Medium',
                'steps': [
                    'Restart computer',
                    'Boot into Safe Mode (F8 during startup)',
                    'Login as Administrator',
                    'Open Control Panel > User Accounts',
                    'Change password for your account',
                    'Restart normally',
                    'Login with new password'
                ],
                'requirements': [
                    'Administrator account access',
                    'Physical access to computer',
                    'Technical knowledge',
                    'May not work on newer Windows versions'
                ]
            }
        ]
        
        for i, method in enumerate(methods, 1):
            print(Fore.MAGENTA + f"\nMethod {i}: {method['name']}")
            print(Fore.WHITE + "-"*70)
            print(Fore.YELLOW + f"Data Loss: {'⚠️ YES' if method['data_loss'] else '✅ NO'}")
            print(Fore.YELLOW + f"Difficulty: {method['difficulty']}")
            print()
            print(Fore.GREEN + "Steps:")
            for j, step in enumerate(method['steps'], 1):
                print(f"  {j}. {step}")
            print()
            print(Fore.CYAN + "Requirements:")
            for req in method['requirements']:
                print(f"  • {req}")
            print()
    
    def general_tips(self):
        """General password recovery tips"""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*70)
        print(Fore.CYAN + Style.BRIGHT + "📋 GENERAL PASSWORD RECOVERY TIPS")
        print(Fore.CYAN + Style.BRIGHT + "="*70)
        
        tips = [
            "💡 Try common passwords you use",
            "💡 Check if Caps Lock is on",
            "💡 Try password variations (add numbers, symbols)",
            "💡 Check for saved passwords in browser",
            "💡 Look for password in password manager",
            "💡 Try biometric login (fingerprint, face)",
            "💡 Check if pattern unlock works (Android)",
            "💡 Try Smart Lock (if enabled)",
            "💡 Contact manufacturer support with proof of purchase",
            "💡 Check cloud backups before factory reset",
            "💡 Document your passwords going forward",
            "💡 Use a password manager to avoid future lockouts"
        ]
        
        print(Fore.GREEN + "\nRecovery Tips:")
        print("-"*70)
        for tip in tips:
            print(f"  {tip}")
        
        print(Fore.MAGENTA + "\n⚠️  Important Reminders:")
        print("-"*70)
        warnings = [
            "Only recover devices YOU legally own",
            "Unauthorized access is ILLEGAL",
            "Factory reset erases ALL data",
            "Always backup important data regularly",
            "Keep proof of purchase for devices",
            "Use password managers to prevent lockouts",
            "Enable biometric as backup method",
            "Write down recovery keys in safe place"
        ]
        for warning in warnings:
            print(f"  {warning}")
        
        print(Fore.CYAN + "\n📚 Prevention for Future:")
        print("-"*70)
        prevention = [
            "✅ Use a password manager (LastPass, Bitwarden, 1Password)",
            "✅ Enable biometric authentication",
            "✅ Set up recovery email/phone",
            "✅ Create password reset disks",
            "✅ Backup data regularly to cloud",
            "✅ Write down passwords in secure location",
            "✅ Enable Find My Device features",
            "✅ Keep proof of purchase documents"
        ]
        for prev in prevention:
            print(f"  {prev}")
    
    def run(self):
        """Main loop"""
        while True:
            self.display_menu()
            choice = input(Fore.YELLOW + "Enter your choice (0-4): " + Style.RESET_ALL).strip()
            
            if choice == '0':
                print(Fore.CYAN + "\nThank you for using Legal Password Recovery Guide!")
                print(Fore.CYAN + "Remember: Only access devices you legally own! 🔐")
                break
            elif choice in self.methods:
                self.methods[choice]()
                input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
            else:
                print(Fore.RED + "\n❌ Invalid choice. Please try again.")
                time.sleep(1)


if __name__ == "__main__":
    guide = PasswordRecoveryGuide()
    guide.run()
