import selenium
from selenium import webdriver
import datetime
from datetime import time
import time
import os
import keyboard


class meet_bot:
	def __init__(self):
		self.bot = webdriver.Chrome("chromedriver.exe")


	def login(self,email,pas):
		bot = self.bot
		bot.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

		time.sleep(2)
		email_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
		email_in.send_keys(email)
		time.sleep(2)
		next_btn = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
		next_btn.click()
		time.sleep(2)
		pas_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
		pas_in.send_keys(pas)
		time.sleep(2)
		next_btn2 = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
		next_btn2.click()
		time.sleep(2)


	def join(self,meeting_link):
		bot = self.bot
		bot.get(meeting_link)
		time.sleep(2)
		diss_btn = bot.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[3]/div/span/span")
		diss_btn.click()
		time.sleep(4)
		keyboard.send("tab",do_press=True,do_release=True)
		keyboard.send("tab",do_press=True,do_release=True)
		keyboard.send("enter",do_press=True,do_release=True)
		time.sleep(4)
		mic_btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
		mic_btn.click()
		cam_btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
		cam_btn.click()
		time.sleep(4)
		join_btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
		join_btn.click()




now = datetime.datetime.now()
tday = datetime.date.today()
tweek =tday.isoweekday()	#mon(1),tue(2).....sat(6),sun(7)
thour = now.strftime('%H:%M')	#we need only hours and minutes
print(thour)
print(tday)
print(tweek)



if tweek == 1:			#Monday
	if thour>"10:00" and thour<= "12:00":
		print("C1")
		link = open("C1.txt","r").read()
	elif thour>"14:00" and thour<= "15:30":
		print("C2")
		link = open("C2.txt","r").read()

elif tweek == 2:		#Tuesday
	if thour>"10:00" and thour<= "12:00":
		print("C3")
		link = open("C3.txt","r").read()
	elif thour>"14:00" and thour<= "15:30":
		print("C4")
		link = open("C4.txt","r").read()

elif tweek == 3:		#Wednsday                               
	if thour>"10:00" and thour<= "12:00":
		print("C5")
		link = open("C5.txt","r").read()
	elif thour>"14:00" and thour<= "15:30":
		print("C6")
		link = open("C6.txt","r").read()
elif tweek == 4:		#Thursday
	if thour>"10:00" and thour<= "12:00":
		print("C7")
		link = open("C7.txt","r").read()
	elif thour>"14:00" and thour<= "15:30":
		print("C8")
		link = open("C8.txt","r").read()
elif tweek == 5:		#Friday
	if thour>"10:00" and thour<= "12:00":
		print("C9")
		link = open("C9.txt","r").read()
	elif thour>"14:00" and thour<= "15:30":
		print("C10")
		link = open("C10.txt","r").read()
elif tweek == 6:		#Saturday
	if thour>"10:00" and thour<= "12:00":
		print("C11")
		link = open("C11.txt","r").read()
	elif thour>"14:00" and thour<= "15:30":
		print("C12")
		link = open("C12.txt","r").read()

else:
	link = open("0_0.txt","r").read()       #Example link avaliable in 0_0.txt

print(link)

obj = meet_bot()
obj.login("example@example.ac.in","Password@123")
obj.join(link)
