import time
import sys
import random

# Warna ANSI untuk terminal Linux
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

def slow_print(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def run_simulation():
    print(f"{GREEN}{BOLD}root@kali:~# sudo exploit --target bank_server_remote{END}")
    time.sleep(1)
    
    print(f"{YELLOW}[*] Scanning for vulnerabilities...{END}")
    time.sleep(1.5)
    
    vulnerabilities = ["SQL Injection", "Buffer Overflow", "Broken Auth", "Zero Day"]
    for v in vulnerabilities:
        slow_print(f"{GREEN}[+] Found: {v}{END}")
        time.sleep(0.3)

    print(f"\n{BOLD}{RED}ATTEMPTING BRUTE FORCE...{END}")
    for i in range(1, 11):
        sys.stdout.write(f"\r{YELLOW}Trying password combo {i*1234} of 12340...{END}")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print(f"\n\n{GREEN}[SUCCESS] Password cracked: 'admin123'{END}")
    time.sleep(0.5)
    
    # Progress Bar ala Linux
    print(f"{BOLD}Downloading Ledger Database:{END}")
    for i in range(21):
        bar = '█' * i + '-' * (20 - i)
        sys.stdout.write(f"\r[{bar}] {i*5}%")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print(f"\n\n{BOLD}{GREEN}ACCESS GRANTED. BALANCE REDIRECTED.{END}")
    print(f"{YELLOW}Status: System Cleaned. Logs Deleted.{END}")

if __name__ == "__main__":
    try:
        run_simulation()
    except KeyboardInterrupt:
        print(f"\n{RED}Process aborted by user.{END}")
