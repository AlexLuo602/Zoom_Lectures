from selenium import webdriver
import time
from secret import pw   #Password in another .py file
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#my login info
username = "alex602"
password = pw()
print (password)

#select which course lecture I want
course = input('Which lecture? \n 1: WRDS 150B \n 2: Chem 154 \n 3: APSCI 160 \n 4: Phys 157 \n 5: Math 100 \n 6: Econ 101 \n').lower()

#Start selenium
chromedriver = 'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=chromedriver, options=options)
driver.get('https://faculty.canvas.ubc.ca/')
driver.implicitly_wait(10)

#Enter into my dashboard
ubc_button = driver.find_element_by_xpath('//*[@id="post-133"]/div/div/div/div[2]/section[1]/a/img')
ubc_button.click()
name_box = driver.find_element_by_xpath('//*[@id="username"]')
password_box = driver.find_element_by_xpath('//*[@id="password"]')
login_button = driver.find_element_by_xpath('//*[@id="col2"]/form/div[3]/button')
name_box.send_keys(username)
password_box.send_keys(password)
login_button.click()

#Depending on the course lecture I chose
if course == "1" or course == "wrds" or course == "wrds 150B":
    WRDS150B_Box = driver.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[8]/div/a/div')
    WRDS150B_Box.click()
    WRDS150B_Zoom_Box = driver.find_element_by_xpath('//*[@id="section-tabs"]/li[3]/a')
    WRDS150B_Zoom_Box.click()

if course == "2" or course == "chem" or course == "chem 154":
    Chem154_Box = driver.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[9]/div/a/div')
    Chem154_Box.click()
    Chem154_Zoom_Box = driver.find_element_by_xpath('//*[@id="section-tabs"]/li[5]/a')
    Chem154_Zoom_Box.click()

if course == "3" or course == "apsci" or course == "apsci 160":
    APSCI160_Box = driver.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[2]/div/a/div')
    APSCI160_Box.click()
    APSCI160_button_1 = driver.find_element_by_xpath('//*[@id="ui-id-3"]')
    APSCI160_button_1.click()
    APSCI160_button_2 = driver.find_element_by_xpath('//*[@id="tab-3"]/table[1]/tbody/tr[2]/td[3]/p/a/span[1]')
    APSCI160_button_2.click()

if course == "4" or course == "phys" or course == "phys 157":
    Phys157_Box = driver.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[6]/div/a/div')
    Phys157_Box.click()
    Phys157_button_1 = driver.find_element_by_xpath('//*[@id="wiki_page_show"]/div[3]/table[3]/tbody/tr[2]/td[1]/p[5]/a')
    Phys157_button_1.click()
    time.sleep(1)
    Phys157_button_2 = driver.find_element_by_xpath('//*[@id="section-tabs"]/li[5]/a')
    Phys157_button_2.click()
    # actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).send_keys(Keys.TAB).perform()
    driver.get("https://app.reef-education.com/api/autosignin/fbb5c788-1c8f-4449-859b-b24ec9617c0c")



if course == "5" or course == "math" or course == "math 100":
    MATH100_Box = driver.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[5]/div/a/div')
    MATH100_Box.click()
    MATH100_button_1 = driver.find_element_by_xpath('//*[@id="section-tabs"]/li[9]/a')
    MATH100_button_1.click()

if course == "6" or course == "econ" or course == "econ 101":
    Econ101_Box = driver.find_element_by_xpath('//*[@id="DashboardCard_Container"]/div/div[3]/div/a/div')
    Econ101_Box.click()
    Econ101_button_1 = driver.find_element_by_xpath('//*[@id="section-tabs"]/li[10]/a')
    Econ101_button_1.click()
    # time.sleep(8)
    # Econ101_button_2 = driver.find_element_by_xpath('//*[@id="side-menu-toggle"]')
    # Econ101_button_2.click()
    # Econ101_button_3 = driver.find_element_by_xpath('//*[@id="side-menu"]/div/nav/ul/li[3]/a/span')
    # Econ101_button_3.click()