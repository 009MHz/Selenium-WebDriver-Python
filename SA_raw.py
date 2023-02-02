from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

"Open the page as fresh user"
driver.get("https://skillacademy.com/")

"Close the welcome screen"
# By hit on the close button
# wait.until(ec.presence_of_element_located((By.CLASS_NAME, "css-15wy7rm"))).click()

# By hit the outer body
# wait.until(ec.presence_of_element_located((By.CLASS_NAME, "css-wh8vrs"))).click()


"Redirect to Login Page"
# Tap the welcome screen body
wait.until(ec.presence_of_element_located((By.CLASS_NAME, "css-wh8vrs"))).click()


"Validating the Login page"
# Validate the URL
assert wait.until(ec.url_to_be("https://skillacademy.com/auth/login?redirectTo=%2Fgamification%3F")), "Incorrect URL detected"

# Validate the Global SA components
assert wait.until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "css-nv5zp7"))), "SA component is missing"

# Validate Global Login components
assert wait.until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "css-7p994x"))), "Login Component is missing"

# Validate Login components - Masuk Tab
assert wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "css-fm4lp1"))), "Masuk tab is missing"

# Validate Login components - Daftar Tab
assert wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "css-1v3ribi"))), "Daftar tab is missing"

# Validate Login components - Masuk ke akun Text
enter_text = driver.find_element(By.CLASS_NAME, "css-1i8ebie")
assert enter_text.text == "Masuk ke akun Skill Academy kamu!", "Displayed text is not as expected"

# Validate Login components - Email Textbox
assert wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@type='text']"))), "Email field is missing"

# Validate Login components - Password textbox
assert wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@type='password']"))), "Password field is missing"

# Validate Login components - Eye Icon
assert wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "css-umc2e0"))), "Eye Icon is missing"
assert wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "css-umc2e0"))), "Eye icon is unclickable"

# Validate Login components - Lupa Password CTA
assert wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Lupa Password"))), "Forget Password CTA is missing"
assert wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Lupa Password"))), "Forget Password is unclickable"

# Validate Login components - Masuk Button
assert wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'css-wc5b3e'))), "Masuk button is missing"
assert wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'css-wc5b3e'))), "Masuk button is unclickable"
assert driver.find_element(By.CLASS_NAME, 'css-wc5b3e').text == "MASUK", "Login button text is not as expected"

# Validate Login components - Masuk dengan SSO text
assert wait.until(ec.visibility_of_element_located((By.XPATH, "(//p[@class='css-zwgrk9'])[2]"))), "Optional Login Text is missing"
assert driver.find_element(By.XPATH, "(//p[@class='css-zwgrk9'])[2]").text == "Atau masuk dengan", "Optional Login text incorrect"

# Validate Login components - Login with Facebook
assert wait.until(ec.presence_of_element_located((By.XPATH, "//div[@data-testid='facebook-login-button']"))), "Facebook SSO is missing"
assert wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@data-testid='facebook-login-button']"))), "Facebook SSO is unclickable"
assert driver.find_element(By.XPATH, "//div[@data-testid='facebook-login-button']").text == "Login dengan Facebook", "Facebook SSO text is not as expected"

# Validate Login components - Login with Google
assert wait.until(ec.visibility_of_element_located((By.XPATH, "(//div[@class='css-8831uy'])[2]"))), "Google SSO is missing"
assert wait.until(ec.element_to_be_clickable((By.XPATH, "(//div[@class= 'css-8831uy'])[2]"))), "Google SSO is unclickable"
assert driver.find_element(By.XPATH, "(//div[@class= 'css-8831uy'])[2]").text == "Login dengan Google", "Google SSO text is not as expected"

# Validate Login components - Footer
assert wait.until(ec.presence_of_element_located((By.CLASS_NAME, "css-1j9wixf"))), "Footer is missing"
assert driver.find_element(By.XPATH, "(//span[@class='css-1mjdaa0'])[1]").text == "Belum memiliki akun? Silakan ", "Footer text is not as expected"
assert wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Daftar"))), "Footer is unclickable"
