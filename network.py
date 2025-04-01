import socket

def check_connection():
    try:
        socket.create_connection(('www.google.com', 80))
        print("Network is up!")
    except OSError:
        print("Network is down!")
        exit(1)
