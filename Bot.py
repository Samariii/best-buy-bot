import time
from selenium import webdriver

# grab the webdriver from the local filesystem
browser = webdriver.Chrome('chromedriver.exe')


# Send the webdriver var to the intended website
browser.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440')

# Test page
# browser.get('https://www.bestbuy.com/site/ibuypower-trace-mr-gaming-desktop-amd-ryzen-5-3600-8gb-memory-nvidia-geforce-gt-710-2gb-240gb-ssd/6463678.p?skuId=6463678')

complete = False

while not complete:
	try:
		atcbtn = browser.find_element_by_class_name('btn-disabled')
		browser.refresh()
	except:
		atcbtn = browser.find_element_by_class_name('btn-primary')
		atcbtn.click()

print("Got to cart")
browser.get('https://www.bestbuy.com/cart')


time.sleep(2)
checkoutButton = browser.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button')

print("Checkout imminent")
checkoutButton.click()

time.sleep(2)
emailBox = browser.find_element_by_xpath('//*[@id="fld-e"]')

time.sleep(1)
passBox = browser.find_element_by_xpath('//*[@id="fld-p1"]')

print("Email entered")
emailBox.send_keys("samarid1010@gmail.com")

print("Password through")
passBox.send_keys("Samari225!")

signBox = browser.find_element_by_class_name('btn-lg')

print("Signing in")
signBox.click()