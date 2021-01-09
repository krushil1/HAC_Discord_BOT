
from selenium import webdriver
from credentials import userName, password
from dhooks import Webhook
import time

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("headless")

#Enter your chromedriver's path right in parenthesis 

browser = webdriver.Chrome('ENTER YOUR CHROMEDRIVER'S PATH', options = option)



browser.get("http://pldhomeaccess.spihost.com/")
time.sleep(2)

#username input
text_area = browser.find_element_by_id('LogOnDetails_UserName') 
text_area.send_keys(userName) 

#password input
text_area = browser.find_element_by_id('LogOnDetails_Password') 
text_area.send_keys(password) 

#sign in button click
browser.find_element_by_id('login').click() 
time.sleep(4)

#clicks the classes button to view the classes
browser.find_element_by_id('hac-Classes').click()
time.sleep(2)

browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="sg-legacy-iframe"]'))

'''
For this section, create a variable of on the name of your class like gym which I used an example. Then copy that class's xpath. 
To get the xpath of a class, simply open inspect element by right clicking or pressing F12, then on the super top-left of the inspect element
and you will find a icon which will look like a mouse cursor and a sqaure. Click on that and then click on your class's current average 
that you to get the xpath for, once you have clicked on the class's current average, a section of code will be highlighted in inspect element,
simple right click that highlighted code and look for Copy option. Hover over Copy and there should be a option for Copy XPath, simply click on Copy XPath,
and now you got the XPATH!
'''
gym = browser.find_element_by_id('ENTER YOUR XPATH FOR THE CLASS').text + " IN GYM" #<- Where you see IN GYM is your class name, edit it with the name of your class.
# A side note, you can add as many classes as you wish to! Simply edit the gym variable with the name of your class!
time.sleep(1)

browser.quit()

time.sleep(2)

#Enter your Discord's Webhook URL in the parenthesis                            
hook = Webhook('ENTER YOUR DISCORD'S WEBHOOK URL HERE')

'''
So for this part, you will need to type hook.send() and put the name class's variable you created. For example, I created a variable called gym where my
gym grade gets stored. so inside the hook.send() parenthesis, enter your class variable!
'''
hook.send(gym)



