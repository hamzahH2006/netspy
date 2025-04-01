import socket

def start_listener(LHOST, LPORT):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind((LHOST, LPORT))
    listener.listen(5)
    print(f"Listener started on {LHOST}:{LPORT}")
    client_socket, client_address = listener.accept()
    print(f"Connection received from {client_address}")
    # تفاعل مع العميل هنا مثل تنفيذ أوامر أو استلام بيانات
