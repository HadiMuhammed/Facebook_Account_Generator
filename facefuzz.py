from selenium import webdriver
from time import sleep
from pyvirtualdisplay import Display 
import os
import random

os.system("bash remove.sh")
os.system("bash email.sh")
os.system("service tor restart")
sleep(1)

with open('email.txt', 'r') as myfile:
    email=myfile.read().replace('\n', '')
    myfile.close()

firstname="bobby"
lastname="chemma" 
print ("                                  FaceFuzZ.. version 0.1      ")
print ("                                facebook account generator")
print ("                                 Created By Hadi Muhammed")
print ("   WARNING : Use at Your Own risk .. Iam not responsible for anything done by you")
print ("                                                    ")
os.system("read a")


Day='1'
Month='1'
Year='1997'
sex='2'
os.system("clear") 
os.system("bash logo.sh")


print ("[] Welcome To FaceFuzz")
print ("[] Connecting to Facebook..")



display = Display(visible=0, size=(800, 600))
display.start()


driver = webdriver.Firefox()
driver.get('https://www.facebook.com/reg')
os.system("clear")
os.system("bash logo.sh")
print ("[] Welcome To FaceFuzz")
print ("[] Connected to Facebook !")
print (" ")
print ("[] +ALERT+ Click Enter to Generate a Facebook Account +ALERT+ [] ")
os.system("read a")
os.system("clear")
os.system("bash logo.sh")
print ("[] Selecting Random Name ")
sleep(1)


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
firstname= random_line("unames.txt")
lastname= random_line("unames.txt")

 
username_box = driver.find_element_by_id('u_0_i')
username_box.send_keys(firstname)
print ("[] Generating Profile name")
sleep(1)
 
password_box = driver.find_element_by_id('u_0_k')
password_box.send_keys(lastname)
print ("[] Generating Profle name")
sleep(1)

password_box = driver.find_element_by_id('u_0_n')
password_box.send_keys(email)
print ("[] Generating Email")
sleep(1)

password_box = driver.find_element_by_id('u_0_q')
password_box.send_keys(email)
print ("[] Generating Email")
sleep(1)


password_box = driver.find_element_by_id('u_0_u')
password_box.send_keys(email)
print ("[] Setting Password")
sleep(1)

password_box = driver.find_element_by_id('day')
password_box.send_keys(Day)
print ("[] Creating user details")
sleep(1)

password_box = driver.find_element_by_id('month')
password_box.send_keys(Month)
print ("[] Entering User Details")
sleep(1)


password_box = driver.find_element_by_id('year')
password_box.send_keys(Year)
print ("[] Succuss")
sleep(1)





driver.find_elements_by_css_selector("input[type='radio'][value='2']")[0].click()
print ("[] Getting Confirm Code")
sleep(1)




login_box = driver.find_element_by_id('u_0_10')
login_box.click()
sleep(10)

os.system("bash confirm.sh")

code=os.system("head -n 1 confirm_code.txt")

sleep(1)
os.system("bash remove.sh")
os.system("service tor stop")
os.system("clear")
os.system("bash logo.sh")
print(" ")
print("**EMAIL AND PASSWORD ARE SAME**")
print(" ")
print("EMAIL n PASS                CONFIRMATION_CODE")
print(os.system("cat logs.txt"))




print ("Done")


driver.quit()
print("Finished")