from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.binary_location = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=chrome_options)

try:
    print("Iniciando navegación...")
    driver.get("https://www.google.com")
    time.sleep(2)
    
    driver.get("https://hybridge.education")
    time.sleep(2)
    
    driver.get("https://openai.com")
    print("Proceso completado con éxito.")

finally:
    driver.quit()
