import requests


try:
    requests.head('http://pudim.com.br/')
except:
    print('\033[31mO site pudim está offline!\033[m')
else:    
    print('\033[32mO site pudim está online!\033[m')

