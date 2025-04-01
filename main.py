# main.py
import os
import time
from ui import display_banner, show_menu
from commands import create_payload, start_listener

def main():
    # عرض الواجهة والعنوان
    display_banner()
    
    while True:
        # عرض القائمة وطلب إدخال المستخدم
        choice = show_menu()

        if choice == '1':
            # تنفيذ إنشاء Payload
            create_payload()
        elif choice == '2':
            # تنفيذ أمر بدء Listener
            start_listener()
        elif choice == '3':
            # الخروج من الأداة
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
