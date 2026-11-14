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
                               (_.)  _  )   /
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

def show_processes():
    os.system('clear')
    print(current_color + "\n top processes (by memory)\n")
    os.system("ps aux --sort=-%mem | head -n 6")
    input(Fore.YELLOW + "\n press enter to return...")

def scan_local():
    os.system('clear')
    print(current_color + "\n local network check\n")
    print(" pinging router (192.168.1.1)...")
    os.system("ping -c 2 192.168.1.1")
    input(Fore.YELLOW + "\n press enter to return...")

# НОВАЯ ФУНКЦИЯ: Лаунчер скриптов
def show_tools():
    while True:
        os.system('clear')
        print(current_color + "\n tools\n")
        
        # Получаем список файлов в текущей директории
        files = os.listdir('.')
        # Оставляем только .py файлы, кроме самого main.py
        scripts = [f for f in files if f.endswith('.py') and f != 'main.py']
        
        if not scripts:
            print(" no scripts found in cyberdeck folder")
            input(Fore.YELLOW + "\n press enter to return...")
            break
            
        for i, script in enumerate(scripts, 1):
            print(f" [{i}] {script}")
            
        print(f" [{len(scripts) + 1}] back\n")
        
        choice = input(current_color + " select: " + Fore.RESET)
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(scripts):
                selected_script = scripts[choice_num - 1]
                os.system('clear')
                # Запускаем выбранный скрипт
                os.system(f"python3 {selected_script}")
                input(Fore.YELLOW + "\n press enter to return...")
            elif choice_num == len(scripts) + 1:
                break
        except ValueError:
            pass

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
        print(" [3] processes")
        print(" [4] scan local")
        print(" [5] tools")
        print(" [6] settings")
        print(" [7] exit\n")
        
        choice = input(current_color + " select: " + Fore.RESET)
        
        if choice == '1':
            show_monitor()
        elif choice == '2':
            check_network()
        elif choice == '3':
            show_processes()
        elif choice == '4':
            scan_local()
        elif choice == '5':
            show_tools()
        elif choice == '6':
            show_settings()
        elif choice == '7':
            break

if __name__ == "__main__":
    main()