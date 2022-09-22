import requests
from bs4 import BeautifulSoup
import re
import time



def find(lstring):
    try:
        time. sleep(6)
        url = (f"https://pypi.org/project/" + str(lstring) +"/")
        requests_results = requests.get(url, headers={'Cache-Control': 'no-cache'})
        if requests_results.status_code == 200:
            soup = BeautifulSoup(requests_results.content, "lxml")
            links = soup.find_all("a")
            name = soup.find('h1')
            pip = soup.find(id="pip-command")
            name = name.get_text()
            pip = pip.get_text()
            s = ''.join(str(links))
            r = (r"https://github.com/[\w-]+/[\w-]+")
            reg = re.search(r,s)  
            home = reg.group()
            final = str(name.strip()) + '\n' + str(pip) + '\n' + str(home)
            print('\n')
            print('--------------------------------')
            print('\n')
            print(final)
        else:
            print('\n')
            print('--------------------------------')
            print('\n')
            print(f"URL doesn't exist for '{lstring}' please check it manually")
    except KeyboardInterrupt:
        print("Interrupted")
    except:
        print('\n')
        print('--------------------------------')
        print('\n')
        print(f"Couldn't found anything for '{lstring}'")












    
    