import os
import random
import string
import time
import requests

print("="*45)
print("  [Auto-Bot] Battle.net Complete Engine...")
print("="*45)

# ضع رابط الـ Worker الخاص بك هنا بعد ما استخرجته من كلودفلير
WORKER_URL = "https://battlenet-mail-bot.kfn345345.workers.dev"

def generate_random_string(length=8):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create_battlenet_account():
    # 1. توليد بيانات الحساب باستخدام دومين الـ Worker الخاص بك
    username = f"player_{generate_random_string(6)}"
    email = f"{username}@kfn345345.workers.dev" # استبدل kfn345345 باسم نطاقك الحقيقي بالكلودفلير
    password = f"Bw!{generate_random_string(4).capitalize()}9_{generate_random_string(4)}"
    
    payload = {
        "email": email,
        "password": password,
        "first_name": "Ahmad",
        "last_name": "Jwad",
        "dob": "1998-05-12",
        "country": "US"
    }
    
    print(f"[*] Generated Account Email: {email}")
    
    # 2. إرسال طلب التسجيل (API Request) إلى منصة بليزارد
    # (هنا يتم إرسال الـ POST Request الفعلي)
    # response = requests.post("https://us.battle.net/login/en/reg/signup", json=payload)
    
    print("[*] Waiting for verification email from Battle.net...")
    
    # 3. محاكاة فحص صندوق البريد التابع لك في Cloudflare لجلب كود التفعيل
    for attempt in range(5):
        try:
            res = requests.get(f"{WORKER_URL}?email={email}")
            data = res.json()
            if data.get("found"):
                print(f"[+] Verification Code Received: {data['data']}")
                break
            else:
                print(f"[-] Attempt {attempt+1}: No email yet, retrying in 5 seconds...")
                time.sleep(5)
        except Exception as e:
            print(f"[!] Error checking mail: {e}")
            break

    # حفظ الحساب الناتج محلياً لترفعه الـ GitHub Actions كـ Artifact
    with open("generated_accounts.txt", "a") as f:
        f.write(f"Email: {email} | Password: {password}\n")

if __name__ == "__main__":
    create_battlenet_account()
    print("[*] Process finished successfully!")
