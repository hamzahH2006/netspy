def get_os_choice():
    print("""\nSelect Target Operating System:
1. Windows
2. Linux
3. Mac
4. Android
5. iOS
    """)
    return input("Enter your choice (1-5): ").strip()

def get_connection_type_for_os(os_choice):
    options = {
        "1": ["windows/meterpreter/reverse_tcp", "windows/shell/reverse_tcp"],
        "2": ["linux/x86/shell_reverse_tcp", "linux/x86/shell_bind_tcp"],
        "3": ["osx/x86/shell_reverse_tcp", "osx/x86/shell_bind_tcp"],
        "4": ["android/meterpreter/reverse_tcp", "android/meterpreter/bind_tcp"],
        "5": ["ios/shell_reverse_tcp", "ios/shell_bind_tcp"],
    }

    if os_choice in options:
        print(f"\nSelect Connection Type for {os_choice}:")
        for i, conn in enumerate(options[os_choice], 1):
            print(f"{i}. {conn}")
        return input("Enter your choice: ").strip()
    return "1"

def show_menu():
    print("\nSelect an option:")
    print("1. Create Payload")
    print("2. Start Listener")
    print("3. Network Scan")
    print("4. Exit")
    return input("Enter your choice: ").strip()
