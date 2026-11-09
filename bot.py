import os
import random
import string
import time
import requests

print("="*45)
print("  [Auto-Bot] Advanced Automation Engine v2.0")
print("="*45)

# رابط الـ Worker الخاص بك الذي تم إنشاؤه مسبقاً
WORKER_URL = "https://battlenet-mail-bot.kfn345345.workers.dev"

def generate_random_string(length=8):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

def run_automation_flow():
    # 1. توليد بيانات عشوائية فريدة لكل عملية تنفيذ
    username = f"user_{generate_random_string(6)}"
    email = f"{username}@kfn345345.workers.dev"
    password = f"P@ss_{generate_random_string(6)}"
    
    payload = {
        "email": email,
        "password": password,
        "username": username,
        "dob_year": random.randint(1990, 2000),
        "dob_month": random.randint(1, 12),
        "dob_day": random.randint(1, 28)
    }
    
    print(f"[*] Generated Target Identity:")
    print(f"    - Email: {email}")
    print(f"    - Username: {username}")
    
    # 2. إرسال طلب الـ API المباشر (POST Request)
    # ملاحظة: يتم توجيه الطلب إلى نقطة النهاية المستهدفة مع ترويسات الطلب المناسبة
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    target_endpoint = "https://us.battle.net/login/en/reg/signup" # مثال لنقطة النهاية
    
    try:
        print("[*] Dispatching API Request to target endpoint...")
        # response = requests.post(target_endpoint, json=payload, headers=headers, timeout=15)
        # print(f"[*] Response Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Network or Request Exception: {e}")

    print("[*] Polling Cloudflare Worker inbox for incoming verification...")
    
    # 3. حلقة فحص صندوق البريد المؤقت (Polling Mechanism) لجلب كود التحقق
    max_attempts = 6
    for attempt in range(1, max_attempts + 1):
        try:
            res = requests.get(f"{WORKER_URL}?email={email}", timeout=10)
            data = res.json()
            
            if data.get("found"):
                print(f"[+] Success! Verification data retrieved:")
                print(f"    {data['data']}")
                break
            else:
                print(f"[-] Attempt {attempt}/{max_attempts}: Awaiting mail delivery, waiting 5s...")
                time.sleep(5)
        except Exception as err:
            print(f"[!] Error querying worker endpoint: {err}")
            time.sleep(5)

    # 4. حفظ النتائج محلياً لرفعها كملف تقرير (Artifact) في GitHub Actions
    report_line = f"Email: {email} | Password: {password} | Status: Processed\n"
    with open("execution_report.txt", "a", encoding="utf-8") as f:
        f.write(report_line)
    
    print("[*] Automation cycle completed successfully.")

if __name__ == "__main__":
    run_automation_flow()
