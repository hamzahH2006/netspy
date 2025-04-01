# ui.py
import random
from banners import banners  # تأكد من استيراد المتغير بشكل صحيح

# دالة لإظهار الشكل العشوائي
def display_banner():
    print(random.choice(banners))

# دالة لعرض القائمة
def show_menu():
    print("\033[1;32mSelect an option:\033[0m")
    print("[1] Create Payload")
    print("[2] Start Listener")
    print("[3] Exit")
    
    choice = input("\033[1;34mEnter your choice: \033[0m")
    return choice
