import socket, sys
import subprocess

ip = '127.0.0.1'
p = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, p))
s.listen(2)
print('listening to {}:{}'.format(ip,p))
con, addr = s.accept()
con.send('connected!\n'.encode())
while True:
    con.send('\nzshell~# '.encode())
    command = con.recv(1024).decode()
    print(f"\nzshell~# {command}")
    subprocess.run(command, shell=True)
    console = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    con.send(console.stdout.read())
    con.send(console.stderr.read())
