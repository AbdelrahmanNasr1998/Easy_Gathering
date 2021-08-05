import argparse
import getopt
import sys
import os
global opts

argv = sys.argv[1:]

def usage():
    print('''
     _____                 ____       _   _               _             
    | ____|__ _ ___ _   _ / ___| __ _| |_| |__   ___ _ __(_)_ __   __ _ 
    |  _| / _` / __| | | | |  _ / _` | __| '_ \ / _ \ '__| | '_ \ / _` |
    | |__| (_| \__ \ |_| | |_| | (_| | |_| | | |  __/ |  | | | | | (_| |
    |_____\__,_|___/\__, |\____|\__,_|\__|_| |_|\___|_|  |_|_| |_|\__, |
                    |___/                                         |___/ 

    welcome to Easy Gathering | v 1.0
    usage: python Easy_Gathering.py -u <url>
    example: sudo python Easy_Gathering.py -u example.com
    ''')

def AutoPrint(AP):
	print(f'''

============================================================
| -> {AP}
============================================================
	''')

def AutoRun(AR):
	os.system(AR)

def run(url):
    print('''
         _____                 ____       _   _               _             
        | ____|__ _ ___ _   _ / ___| __ _| |_| |__   ___ _ __(_)_ __   __ _ 
        |  _| / _` / __| | | | |  _ / _` | __| '_ \ / _ \ '__| | '_ \ / _` |
        | |__| (_| \__ \ |_| | |_| | (_| | |_| | | |  __/ |  | | | | | (_| |
        |_____\__,_|___/\__, |\____|\__,_|\__|_| |_|\___|_|  |_|_| |_|\__, |
                        |___/                                         |___/ 
        ''')
    try:
        AutoPrint('nmap')
        AutoRun(f'nmap {url} -sV -O -A')
    except:
        print("nmap failed")

    try:
        AutoPrint('nikto')
        AutoRun(f'nikto -h {url}')
    except:
        print("nikto failed")

    try:
        AutoPrint('sublist3r')
        AutoRun(f'sublist3r -d {url}')
    except:
        print("sublist3r failed")

    try:
        AutoPrint('amass')
        AutoRun(f'amass enum -d {url}')
    except:
        print("amass failed")

    try:
        AutoPrint('assetfinder')
        AutoRun(f'assetfinder --subs-only {url}')
    except:
        print("assetfinder failed")

    try:
        AutoPrint('subfinder')
        AutoRun(f'subfinder -d {url}')
    except:
        print("subfinder failed")

    try:
        AutoPrint('gobuster')
        AutoRun(f"gobuster dir -u {url} -c 'session=123456' -t 50 -w common-files.txt -x .php,.html")
    except:
        print("gobuster failed")

    try:
        AutoPrint('dirsearch')
        AutoRun(f'dirsearch -u {url}')
    except:
        print("dirsearch failed")

    try:
        AutoPrint('arjun')
        AutoRun(f'arjun -u {url} -c 1')
    except:
        print("arjun failed")



try:
    opts, args = getopt.getopt(argv, 'u:', ['url'])
except getopt.GetoptError as err:
    print(err)

if argv:
    for opt, arg in opts:
        if opt in ['-u', '--url']:
            run(arg)

else:
    usage()
    sys.exit()


