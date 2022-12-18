sys.path.append('Modules')
#!/usr/bin/python3

import requests
import sys

from sqli import sqlil
from kittyscan import kittyscan
from xssi import xssi
from ip import ip

def menu():
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
    print('------------------------------------------------------------------------------')
    print('''
    (1) SQLI Bypass login page
    (2) SQL Injection (CAN TAKE TIME)
    (3) XSS injector
    (4) NMAP NSE Vuln Scan (CAN TAKE TIME)
    (5) IpInfo
    ''')
    print('------------------------------------------------------------------------------')

    try:
        choice = input("root☠KSVD: ")
        if choice == "1":
            sqlil()
            input('enter to main menu ...')
            menu()
        elif choice == "2":
            sqli()
            input('enter to main menu ...')
            menu()
        elif choice == "3":
            xssi()
            input('enter to main menu')
            menu()
        elif choice == "4":
            kittyscan()
            input('enter to main menu')
            menu()
        elif choice == "5":
            ip()
            input('enter to main menu')
            menu()
        else:
            print('  incorrect choice ')
            print('\r')
            input('enter to main menu ...')
            menu()
    except KeyboardInterrupt:
            print('\n')
            sys.exit()

menu()
