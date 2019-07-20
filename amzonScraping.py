import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'URL of the AMAZON product'

headers = {'User-agent':'your Mozilla Firefox user agent'} # google my user agent

def check_price():

	page = requests.get(URL, headers=headers)

	#soup = BeautifulSoup(page.content, 'html.parser')

	soup1 = BeautifulSoup(page.content, "html.parser")
	soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

	price = soup2.find(id='priceblock_ourprice').get_text()

	converted_price = float(price[1:4])

	# check if the price is reduced to a certain value: 200 dollars here 

	if converted_price < 200: 
		send_mail()

	#print(converted_price)

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	server.login('your gmail e-mail here', 'your google app password here') #from google App passwords

	subject = 'Time to do some Shopping, Price fell down !!!'

	body = 'Check the AMAZON link: "URL of the product here"! '

	msg = f"subject: {subject} \n\n {body}"

	server.sendmail(
			'your gmail e-mail here "this will be the sender" ',
			'receiver gmail e-mail here "this will be the receiver" ',
			msg
	)

	print('HEY CHECK YOUR INBOX EMAIL HAS BEEN SENT!')

	server.quit()

# we will check the price 1 time/hour
while(True):
	check_price()
	time.sleep(3600)
