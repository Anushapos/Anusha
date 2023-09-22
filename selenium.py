from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Step 1: Launch the application URL
url = "https://www.bt.com/"
driver = webdriver.Chrome()  
driver.get(url)

# Step 2: Close accept Cookie pop-up if it appears
try:
    cookie_popup = driver.find_element(By.ID, "acceptCookie")
    if cookie_popup.is_displayed():
        cookie_popup.click()
except Exception as e:
    pass

# Step 3: Hover to Mobile menu
mobile_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Mobile')]")
actions = ActionChains(driver)
actions.move_to_element(mobile_menu).perform()

# Step 4: From mobile menu, select Mobile phones
mobile_phones = driver.find_element(By.XPATH, "//a[contains(text(),'Mobile phones')]")
mobile_phones.click()

# Step 5: Verify the number of banners
banners = driver.find_elements(By.XPATH, "//div[@class='promo-grid--link']")
assert len(banners) >= 3, "Number of banners is less than 3"

# Step 6: Scroll down and click View SIM only deals
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
view_sim_only_deals = driver.find_element(By.XPATH, "//a[contains(text(),'View SIM only deals')]")
view_sim_only_deals.click()

# Step 7: Validate the title for the new page
expected_title = "SIM Only Deals | Best SIM Card Deals | BT Mobile"
assert driver.title == expected_title, f"Page title is not as expected. Actual: {driver.title}, Expected: {expected_title}"

# Step 8: Validate "30% off and double data" details
plan_details = driver.find_element(By.XPATH, "//p[contains(text(),'30% off and double data')]").text
expected_details = "30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month"
assert plan_details == expected_details, f"Plan details do not match. Actual: {plan_details}, Expected: {expected_details}"

# Step 9: Close the browser & exit
driver.quit()
