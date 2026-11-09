import os
import random
import string
import requests

print("="*45)
print("  [Auto-Bot] Battle.net Account Formatter Engine...")
print("="*45)

def generate_random_string(length=8):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_battlenet_payload():
    # 1. توليد إيميل متوافق مع نطاق الكلاودفلير (Catch-All)
    username = f"player_{generate_random_string(6)}"
    email = f"{username}@mydomain.workers.dev" # راح نربطه بدومينك لاحقاً
    
    # 2. كلمة مرور قوية تتوافق مع شروط بليزارد (حروف كابيتال، سمول، أرقام، ورموز)
    password = f"Bw!{generate_random_string(4).capitalize()}9_{generate_random_string(4)}"
    
    # 3. بيانات إضافية تطلبها منصة بليزارد (مثل تاريخ الميلاد والعمر)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    birth_year = random.randint(1995, 2003) # عمر مضمون فوق الـ 18 سنة
    
    # هيكل البيانات (Payload) الذي يُرسل إلى واجهة برمجة تطبيقات التسجيل
    payload = {
        "email": email,
        "password": password,
        "first_name": "Ahmad",
        "last_name": "Jwad",
        "dob": f"{birth_year}-{birth_month:02d}-{birth_day:02d}",
        "country": "US" # أو الدولة المستهدفة لتجنب قيود بعض المناطق
    }
    
    return payload

if __name__ == "__main__":
    print("[*] Formatting data for Battle.net registration structure...")
    
    sample_account = generate_battlenet_payload()
    
    print(f"\n[Target Email]: {sample_account['email']}")
    print(f"[Target Password]: {sample_account['password']}")
    print(f"[Date of Birth]: {sample_account['dob']}")
    print(f"[Country Region]: {sample_account['country']}")
    print("\n[*] Data structure is ready for API integration.")
