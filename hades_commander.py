import multiprocessing,os,sys,platform,argparse,time,platform
from multiprocessing import Process
from tabulate import tabulate
from colorama import Fore,init
from colorama import Back as bg
parser = argparse.ArgumentParser(description='BotNet Attacker Main Controller')
parser.add_argument('-o','--option',metavar='',help='')
args = parser.parse_args()
init(autoreset=True)
class Controller(object):
    def __init__(self,option):
        self.option = option
    @staticmethod
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
    def command(self):
        try:
            table = [["Options","Severity"],["Ddos-attack(0)",5],["Backdoor(1)",5],["Auto-Root(2)",5]]
            print(tabulate(table,headers='firstrow',tablefmt='grid'))
            if  args.option == 0:
                print('Proceeding with a DDOS-Attack')
            elif args.option == None:
                print('Pass Arguments to python3 <hades-commander.py> -o (number)')
            else:
                print('Use python3 <hades-commander.py> -h for help.')
        except Exception as Err:
            print(Err)


if __name__ == '__main__':
    class_object = Controller(args.option)
    command = Process(target=class_object.command)
    banner = Process(target=class_object.show_banner,args=('''
______________________________________________________________
  ____  
 / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| | ___ _ __ 
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |/ _ \ '__|
| |__| (_) | | | | | | | | | | | (_| | | | | (_| |  __/ |   
 \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|\___|_|   
______________________________________________________________
        ''',))
    banner.start()
    banner.join()
    command.start()
    command.join()
