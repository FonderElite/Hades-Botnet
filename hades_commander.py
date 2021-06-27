import multiprocessing,os,sys,platform
from multiprocessing import Process
from tabulate import tabulate
from colorama import Fore
from colorama import Back as bg
class Controller(object):
    def __init__(self,option):
        self.option = option
    def show_banner(s):
        for c in s + '\n':
            sys.stdout.write(bg.BLACK + Fore.YELLOW + c)
            sys.stdout.flush()
            time.sleep(1.2 / 100)
        time.sleep(1.5)
        print('-----------------------------------------------------------------')
        print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']Made By Droid | Github:https://github.com/FonderElite')
        print('-----------------------------------------------------------------')
        time.sleep(1.5)
    def command(self):
        table = [["Options","Severity"],["Ddos-attack",5],["Backdoor",4],["Auto-Root",5]]
        print(tabulate(table,headers='firstrow',tablefmt='grid'))
if __name__ == '__main__':
    class_object = Controller()
    command = Process(target=class_object.command)
    command.start()
    command.join()
                  
