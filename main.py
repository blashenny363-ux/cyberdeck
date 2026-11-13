import os
import time
from colorama import init, Fore

init(autoreset=True)

current_color = Fore.CYAN

ascii_art = r"""
                                 ,        ,
                                /(        )`
                                \ \___   / |
                                /- _  `-/  '
                               (/\/ \ \   /\
                               / /   | `    \
                               O O   ) /    |
                               `-^--'`<     '
                 Linux         (_.)  _  )   /
|  | |\  | ~|~ \ /             `.___/`    /
|  | | \ |  |   X                `-----' /
`__| |  \| _|_ / \  <----.     __ / __   \
                    <----|====O)))==) \) /====
                    <----'    `--' `.__,' \
                                 |        |
                                  \       /
                             ______( (_  / \______
                           ,'  ,-----'   |        \
                           `--{__________)        \/
"""

def get_cpu_load():
    with open('/proc/loadavg', 'r') as f:
        load = f.read().split()[0]
    return load

def get_memory():
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()
    total = int(lines[0].split()[1]) // 1024
    free = int(lines[1].split()[1]) // 1024
    used = total - free
    
    percent = (used / total) * 100
    blocks = int((percent / 100) * 20)
    bar = "=" * blocks + "-" * (20 - blocks)
    
    return used, total, bar, percent

def show_monitor():
    try:
        while True:
            os.system('clear')
            
            cpu = get_cpu_load()
            mem_used, mem_total, mem_bar, mem_percent = get_memory()
            
            if mem_percent < 60:
                bar_color = Fore.GREEN
            elif mem_percent < 85:
                bar_color = Fore.YELLOW
            else:
                bar_color = Fore.RED

            print(current_color + "\n cyberdeck monitor\n")
            print(" cpu load: " + Fore.GREEN + cpu)
            print(f" ram: {mem_used} mb / {mem_total} mb")
            print("      [" + bar_color + mem_bar + Fore.RESET + f"] {int(mem_percent)}%\n")
            
            print(Fore.RED + " ctrl+c exit")
            time.sleep(1)
            
    except KeyboardInterrupt:
        pass

def check_network():
    os.system('clear')
    print(current_color + "\n network check\n")
    print(" pinging 8.8.8.8...")
    os.system("ping -c 3 8.8.8.8")
    input(Fore.YELLOW + "\n press enter to return...")

def show_settings():
    global current_color
    while True:
        os.system('clear')
        print(current_color + "\n settings\n")
        print(" [1] green")
        print(" [2] cyan")
        print(" [3] red")
        print(" [4] black background")
        print(" [5] back\n")
        
        choice = input(current_color + " select: " + Fore.RESET)
        
        if choice == '1':
            current_color = Fore.GREEN
        elif choice == '2':
            current_color = Fore.CYAN
        elif choice == '3':
            current_color = Fore.RED
        elif choice == '4':
            os.system('clear')
            print("\033[40m") 
            time.sleep(1)
        elif choice == '5':
            break

def main():
    while True:
        os.system('clear')
        print(current_color + ascii_art)
        print(" cyberdeck\n")
        print(" [1] monitor")
        print(" [2] network check")
        print(" [3] settings")
        print(" [4] exit\n")
        
        choice = input(current_color + " select: " + Fore.RESET)
        
        if choice == '1':
            show_monitor()
        elif choice == '2':
            check_network()
        elif choice == '3':
            show_settings()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()