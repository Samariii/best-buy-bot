# Importing selenium webdriver and selenium wait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Importing the json module to interact with details.json
import json

# Grab the webdriver from the local filesystem
# Load the json to grab details
browser = webdriver.Chrome(ChromeDriverManager().install())
j = open('details.json')
data = json.load(j)

# Send the webdriver to the intended website
browser.get(data['link'])

# Setup the loops for the add to cart button
completeOrder = False

while not completeOrder:
	# Attempt to find the addTC button
	try:
		addTC = WebDriverWait(browser, 10).until(
			EC.element_to_be_clickable(By.CSS_SELECTOR, '.add-to-cart-button')
		)
	except:
		browser.refresh()
		print("Bot is working..")
		continue

	print("Got the add to cart button")

	try:
		# Try to click the button and go to cart
		addTC.click()
		browser.get("https://www.bestbuy.com/cart")

		checkout = WebDriverWait(browser, 10).until(
			EC.presence_of_all_elements_located(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button")
		)
		checkout.click()

		# Redirected to the sign in page and logging in
		print("Got it in the cart, potentially")

		email = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
		email.send_keys(data['email'])

		password = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
		password.send_keys(data['password'])

		signin = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button"))
        )
		signin.click()
		print("Signing you in..")

		# Entering the cvv #
		cvv = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
		cvv.send_keys(data['cvv'])

		# Clicking the place order button
		placeOrder = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
		placeOrder.click()

		completeOrder = True

	except:
		# Just incase we get caught up in the checkout
		# Go back to the link and try again if not in the cart
		browser.get(data['link'])
		print("Not in the cart go back!!")
		continue

print("You got it!")
