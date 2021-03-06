import getopt
import sys
import os
global opts

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white


argv = sys.argv[1:]

def usage():
    print(f'''{Y}
 _____                 ____       _   _               _             
| ____|__ _ ___ _   _ / ___| __ _| |_| |__   ___ _ __(_)_ __   __ _ 
|  _| / _` / __| | | | |  _ / _` | __| '_ \ / _ \ '__| | '_ \ / _` |
| |__| (_| \__ \ |_| | |_| | (_| | |_| | | |  __/ |  | | | | | (_| |
|_____\__,_|___/\__, |\____|\__,_|\__|_| |_|\___|_|  |_|_| |_|\__, |
               |___/                                          |___/  

[*] welcome to Easy Gathering (1.0) | by Abdelrahman Nasr
[*] usage: python Easy_Gathering.py -u <url>
[*] example: sudo python Easy_Gathering.py -u example.com
    ''')

def AutoPrint(AP):
	print(f'''{G}
============================================================
| -> {AP}
============================================================
	''')

def AutoRun(AR):
	os.system(AR)

def run(url):
    print(f'''{Y}
 _____                 ____       _   _               _             
| ____|__ _ ___ _   _ / ___| __ _| |_| |__   ___ _ __(_)_ __   __ _ 
|  _| / _` / __| | | | |  _ / _` | __| '_ \ / _ \ '__| | '_ \ / _` |
| |__| (_| \__ \ |_| | |_| | (_| | |_| | | |  __/ |  | | | | | (_| |
|_____\__,_|___/\__, |\____|\__,_|\__|_| |_|\___|_|  |_|_| |_|\__, |
               |___/                                          |___/  
               
[*] welcome to Easy Gathering (1.1) | by Abdelrahman Nasr
[*] sacn: {url}
[*] process starting ...
        ''')
    try:
        AutoPrint('nmap')
        AutoRun(f'nmap {url} -sV -O -A')
    except:
        print(f"{R}nmap failed")

    try:
        AutoPrint('nikto')
        AutoRun(f'nikto -h {url}')
    except:
        print(f"{R}nikto failed")

    try:
        AutoPrint('sublist3r')
        AutoRun(f'sublist3r -d {url}')
    except:
        print(f"{R}sublist3r failed")

    try:
        AutoPrint('amass')
        AutoRun(f'{R}amass enum -d {url}')
    except:
        print(f"{R}amass failed")

    try:
        AutoPrint('assetfinder')
        AutoRun(f'assetfinder --subs-only {url}')
    except:
        print(f"{R}assetfinder failed")

    try:
        AutoPrint('subfinder')
        AutoRun(f'subfinder -d {url}')
    except:
        print(f"{R}subfinder failed")

    try:
        AutoPrint('gobuster')
        AutoRun(f"gobuster dir -u {url} -c 'session=123456' -t 50 -w common-files.txt -x .php,.html")
    except:
        print(f"{R}gobuster failed")

    try:
        AutoPrint('dirsearch')
        AutoRun(f'dirsearch -u {url}')
    except:
        print(f"{R}dirsearch failed")

    try:
        AutoPrint('arjun')
        AutoRun(f'arjun -u {url} -c 1')
    except:
        print(f"{R}arjun failed")



try:
    opts, args = getopt.getopt(argv, 'u:', ['url'])
except getopt.GetoptError as err:
    print(err)

if argv:
    try:
        for opt, arg in opts:
            if opt in ['-u', '--url']:
                run(arg)
    except:
        usage()

else:
    usage()
    sys.exit()
