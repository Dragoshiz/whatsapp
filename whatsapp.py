from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/') 
input('Press anything after scanning QR code.')
name = input('Name the User or the Group: ')
msg = input('Enter your message: ')
count = int(input('How many messages do you send?: '))


search = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
search.click()
search.send_keys(name,Keys.RETURN)
msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')


for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()

