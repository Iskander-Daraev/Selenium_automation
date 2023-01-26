import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

"""Exclude Chrome closing"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\q2364\\Desktop\\pythonselenproj\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()
time.sleep(0.5)

"""SITE AUTHORIZATION"""

"""Enter login"""
user_name = driver_g.find_element(By.XPATH, "//input[@data-test='username']") # data-test XPATH
user_name.send_keys("standard_user")
print("We input login")
time.sleep(0.5)

"""Enter password"""
password = driver_g.find_element(By.CSS_SELECTOR, "#password") # CSS_SELECTOR
password.send_keys("secret_sauce")
print("We input password\n")
time.sleep(0.5)

"""PUSH LOGIN BUTTON"""
button_login = driver_g.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
print("Line 33 Click login button\n")
time.sleep(0.5)

# Info product 1
"""LETS PRINT INFO ABOUT PRODUCT 1 - item name and its price (Sauce Labs Backpack)"""
product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print("Line 40", value_product_1)

price_product_1 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print("Line 44", value_price_product_1)

"""ADD TO CART BUTTON - PRODUCT 1 (Sauce Labs Backpack)"""
select_product_1 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Line 49 prod 1 added to cart", "\n")
time.sleep(1)

"""SCROLL DOWN"""
driver_g.execute_script("window.scrollTo(0, 300)")
time.sleep(1)

"""LETS PRINT INFO ABOUT PRODUCT 2  - item name and its price (Sauce Labs Onesie)"""
product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_2_title_link']")
value_product_2 = product_2.text
print("Line 59", value_product_2)
#time.sleep(1)

price_product_2 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print("Line 64", value_price_product_2)

time.sleep(1)

"""ADD TO CART BUTTON - PRODUCT 2 (Sauce Labs Onesie)"""
select_product_2 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
select_product_2.click()
print("Line 71 prod 2 added to cart", "\n")
time.sleep(0.5)

"""SCROLL UP TO CART"""
driver_g.execute_script("window.scrollTo(0, 0)")
time.sleep(1)

"""LETS GO TO THE CART NOW - PUSH CART BUTTON"""
go_to_cart = driver_g.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
go_to_cart.click()
print("Line 81 we are in the cart\n")
time.sleep(1)

"""Info cart 1 - LETS CHECK IF WHAT WE'VE CHOSEN IS THE SAME AS IN THE CART - product 1"""
cart_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print("Line 87", value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("Line 89 Info cart 1 product OK")

""""SAME CHECK WITH THE PRICE - product 1"""
price_cart_product_1 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print("Line 94", value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("Line 96 Info cart 1 product price OK\n")

"""Info cart 2 - LETS CHECK IF WHAT WE'VE CHOSEN IS THE SAME AS IN THE CART - product 2"""
cart_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_2_title_link']")
value_cart_product_2 = cart_product_2.text
print("Line 101", value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("Line 103 Info cart 2 product OK")

""""SAME CHECK WITH THE PRICE - product 2"""
price_cart_product_2 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_price_product_2 = price_cart_product_2.text
print("Line 108", value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2
print("Line 110 Info cart 2 product price OK\n")
time.sleep(1)

"""CHECKOUT BUTTON"""
checkout = driver_g.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Line 116 click checkout\n")
time.sleep(1)

"""select user info"""
first_name = driver_g.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Cary")
print("input first name")
time.sleep(0.5)

last_name = driver_g.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Grant")
print("input last name")
time.sleep(0.5)

zip = driver_g.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("123456")
print("input zip")
time.sleep(0.5)

"""CONTINUE BUTTON"""
continue_button = driver_g.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Line 138 click continue\n")
time.sleep(0.5)

"""price compare - LET'S CHECK AGAIN IF THE PRODUCT WE PURCHASING IS THE SAME AS WE ORDERED - product 1"""
finish_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print("Line 144 ", value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("Line 146 Info finish 1 product OK")

"""PRICE CHECKING - product 1"""
price_finish_product_1 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print("Line 151 ", value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("Line 153 Info finish 1 product price OK\n")

"""price compare - LET'S CHECK AGAIN IF THE PRODUCT WE PURCHASING IS THE SAME AS WE ORDERED - product 2"""
finish_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_2_title_link']")
value_finish_product_2 = finish_product_2.text
print("Line 158 ", value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("Line 160 Info finish 1 product OK")

"""PRICE CHECKING - product 2"""
price_finish_product_2 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = price_finish_product_2.text
print("Line 165 ", value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2
print("Line 167 Info finish 2 product price OK\n")

"""LET'S SUM OUR PRICES"""
price_1_to_float = float(value_finish_price_product_1[1:]) #deleting $ sign
price_2_to_float = float(value_finish_price_product_2[1:]) #deleting $ sign
total_price = price_1_to_float + price_2_to_float
print("Line 173 Our total price is ", total_price, "\n")
#time.sleep(1)

""" 'Item total price' in checkout page"""
summary_price = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summary_price = summary_price.text[13:] #deleting $ sign
print("Line 179 Item total price is", value_summary_price)

item_total = str(total_price)
print("Line 182 Sum price from cart is ", item_total)

assert value_summary_price == item_total
print("Line 185 Total summary price OK\n")

"""SCROLL DOWN"""
driver_g.execute_script("window.scrollTo(0, 300)")
time.sleep(1)

"""FINISH BUTTON"""
finish_button = driver_g.find_element(By.XPATH, "//button[@id='finish']")
finish_button.click()
print("FINISH\n")
time.sleep(1)

"""BACK HOME BUTTON"""
home_button = driver_g.find_element(By.XPATH, "//button[@id='back-to-products']")
home_button.click()
print("BACK HOME")
