# I am specifically doing this for facebook. But, by doing some minor changes you can do this for other sites as well

user_id=input("Enter email or phone number : ")
pswd=input("Enter the password : ")

from selenium import webdriver

# Download chrodriver.exe as per according to the version of Chrome you are having
browser=webdriver.Chrome('<path of chromedriver.exe>')
browser.get('https://www.facebook.com/')#give the link of the website which you want to open

ep=browser.find_element_by_id("email")
ep.send_keys(user_id)
ps=browser.find_element_by_id("pass")
ps.send_keys(pswd)

login=browser.find_element_by_id("u_0_b")# "u_0_b" is the id of the login button on the facebook page
login.click()
