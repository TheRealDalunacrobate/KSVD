import requests
import colorama
import os
from colorama import *

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
                    Kitty Scanner Vulnerability SQLI Bypass. by KazuKo (BETA)
            ''')

def sqli():
    # URL de la page de connexion
    target_url = input('[-] ~ Enter a mice homename :  ')
    os.system('clear')

    # Liste de payloads à tester
    with open('payload/sqli.txt', 'r') as f:
        payloads = f.readlines()

    # Boucle sur chaque payload
    for payload in payloads:

        # Envoi de la requête POST
        response = requests.post(target_url)

        # Vérification de la réponse du serveur
        
        if payload in response.text:
            print(Fore.GREEN+'---------------------------------------------------')
            print(f'SQLI found ! :3')
            print(f'payload used : {target_url}+{payload}')
            print('---------------------------------------------------')
        else:
            print(Fore.RED+f'This payload dont work : {payload}')
