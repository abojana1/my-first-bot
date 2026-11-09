import requests
import random

print("="*40)
print("  [Auto-Bot] Starting Zero-Cost Automation Engine...")
print("="*40)

def generate_fake_email():
    domains = ["mydomain.workers.dev", "tempmail.com"]
    random_string = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=10))
    return f"{random_string}@{random.choice(domains)}"

def check_current_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=10)
        print(f"[Network] Current Execution IP: {response.json()['ip']}")
    except Exception as e:
        print(f"[Error] Failed to fetch IP: {e}")

if __name__ == "__main__":
    print(f"[*] Generated Test Email: {generate_fake_email()}")
    check_current_ip()
    print("[*] Bot cycle completed successfully.")
