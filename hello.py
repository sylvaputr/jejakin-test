from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)

driver.get("")

button = driver.find_element(By.CLASS_NAME, "board-departure")
button.click()

driver.implicitly_wait(10)
modalDeparture = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/h2')
print(modalDeparture.is_displayed())

input_element = driver.find_element(By.CLASS_NAME, "Form_formControl__j2pFZ")
input_element.send_keys("zzzzz")

driver.implicitly_wait(30)
emptyMessage = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/p')
print(emptyMessage.text)

from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("")

button = driver.find_element(By.CLASS_NAME, "board-departure")
button.click()

input_element = driver.find_element(By.CLASS_NAME, "Form_formControl__j2pFZ")
input_element.send_keys("Bandar Udara")

driver.implicitly_wait(30)

search_results = driver.page_source
if "Bandar" in search_results and "Udara" in search_results:
    print("Pencarian berhasil. Hasil mengandung kata kunci yang sesuai.")
else:
    print("Pencarian gagal atau hasil tidak mengandung kata kunci yang sesuai.")

index_to_click = 2

css_selector = f".th-list:nth-of-type({index_to_click})"
element_to_click = driver.find_element(By.CSS_SELECTOR, css_selector)

element_to_click.click()
