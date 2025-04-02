import time
from banners import get_banner
from ui import get_os_choice, get_connection_type_for_os, show_menu
from commands import create_payload, start_listener, scan_network

def main():
    print(get_banner())
    print("\nWelcome to NetSpy! 🔥\n")

    while True:
        choice = show_menu()

        if choice == '1':
            os_choice = get_os_choice()
            conn_choice = get_connection_type_for_os(os_choice)
            lhost = input("Enter LHOST (Your IP address): ").strip()
            lport = input("Enter LPORT (Port to listen on): ").strip()
            create_payload(os_choice, conn_choice, lhost, lport)

        elif choice == '2':
            lhost = input("Enter the Listener Host IP: ").strip()
            lport = input("Enter the Listener Port: ").strip()
            start_listener(lhost, lport)

        elif choice == '3':
            scan_network()

        elif choice == '4':
            print("\nExiting...")
            time.sleep(1)
            break

        else:
            print("\nInvalid choice! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
