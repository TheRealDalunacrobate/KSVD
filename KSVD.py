#!/usr/bin/python3
import requests
import time
from tqdm import tqdm
import os
import colorama
from colorama import *
import sys
sys.path.append('Modules')
import sqli
from sqli import *
import kittyscan
from kittyscan import *
import xssi
from xssi import *
import sqlil
from sqlil import *
import ip
from ip import *

def menu():
    os.system('clear')
    print(Fore.WHITE+'''
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

    print(Fore.WHITE+'------------------------------------------------------------------------------')
    print(Fore.WHITE+'''
    (1)--SQLI Bypass login page--                    (4)-- NMAP NSE Vuln Scan (CAN TAKE TIME) --

    (2)--SQL Injection (CAN TAKE TIME)--             (5)--IpInfo--

    (3)--XSS injector--                                     
    
                   ~Made By KazuKo NetRunner'''+Fore.WHITE)
    print('\r')
    print(Fore.WHITE+'------------------------------------------------------------------------------')
    print('\r')
    try:
        choice = input(Fore.RED+"root"+Fore.WHITE+"☠"+Fore.RED+"KSVD"+Fore.RESET+": ")
        print('\r')
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
        elif choice == "4":
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
