from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By

from captcha_bypass import solve_captcha
import captcha_bypass

options = webdriver.ChromeOptions()


# Headless?
options.add_argument("--headless")

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver=webdriver.Chrome(options=options)

driver.get("https://www.daraz.pk/") 

#finding all title elements on the page 
heading_elements=driver.find_elements_by_tag_name("h1")
for heading in heading_elements:
    # if heading.get_attribute("src").startswith(give captcha link)
        captcha=heading 

#extracting text from each title element
# headings=[heading.text for heading in heading_elements ]

result=captcha_bypass.solve_captcha(driver,captcha)

if result:
    print(result)
    exit(0)
else:
    print("Failed!")
    exit(1)

#close the webdriver
driver.quit()