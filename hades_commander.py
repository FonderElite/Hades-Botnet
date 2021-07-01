import os,sys,time,socket,platform
from tabulate import tabulate
from colorama import Fore,init 
from colorama import Back as bg
init(autoreset=True)
def show_banner(s):
    for c in s + '\n':
        sys.stdout.write(bg.BLACK + Fore.WHITE + c)
        sys.stdout.flush()
        time.sleep(1.2 / 100)
    time.sleep(1.5)
    print('-----------------------------------------------------------------')
    print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']Made By Droid | Github:https://github.com/FonderElite')
    print('-----------------------------------------------------------------')
    time.sleep(1)
def options():
      table = [["Options","Severity"],["Ddos-attack(0)",5],["Backdoor(1)",5],["Auto-Root(2)",5]]
      print(tabulate(table,headers='firstrow',tablefmt='grid'))

def execute():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    if os.getuid() == 0:
        global root_fmt
        root_fmt = '''
{red}┌──(root💀{host_name})-[{cwd}]
└─Option# '''.format(host_name=host,cwd=os.getcwd(),red=Fore.RED,white=Fore.WHITE)
    elif os.getuid() != 0:
        root_fmt = '''
{blue}┌──({host_name}㉿Hades)-[{cwd}]
└─Option$ '''.format(host_name=host,cwd=os.getcwd(),blue=Fore.BLUE,white=Fore.WHITE)
    print(root_fmt,end='')
    choice = input("")
    if choice == "0":
        ip = input("Server Ip: ")
        port = int(input("Server Port: "))
        while True:
            s.connect((ip, port))
            cmd = bytes(input("Input: "),'utf-8')
            s.send(cmd)

    else:
        print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Invalid Option.')

if __name__ == '__main__':
    banner = show_banner('''
______________________________________________________________
  ____  
 / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| | ___ _ __ 
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |/ _ \ '__|
| |__| (_) | | | | | | | | | | | (_| | | | | (_| |  __/ |   
 \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|\___|_|   
______________________________________________________________
        ''')
    options()
    execute()
