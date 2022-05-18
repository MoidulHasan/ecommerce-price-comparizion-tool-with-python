from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv

def scrap_pickaboo(categorie_name, categorie_link, page_upto):
    #initialize driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #implicit wait
    driver.implicitly_wait(0.5)
    #maximize browser
    driver.maximize_window()
    # declare file name and open file
    filename = './data/pickaboo-products.csv'
    url = categorie_link
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        position_to_replace = categorie_link.find("p=")
        while(i<=page_upto):
            driver.implicitly_wait(1)
            print("Page No988: ", i, url)
            driver.get(url)
            driver.implicitly_wait(1)
            items = driver.find_elements(By.CLASS_NAME, 'product-item-link')
            for item in items:
                products_url = item.get_attribute('href')
                products_name = item.get_attribute('innerHTML').strip()

                data = {}
                data['category'] = categorie_name
                data['products-name'] = products_name
                data['products-link'] = products_url
                print(data)
                w.writerow(data)
            i+=1
            url = url[:position_to_replace+2]+str(i)+url[position_to_replace+3:]
            print(url)
        f.close()





categorie_name = "SHAVER & TRIMMER"
categorie_link= "https://www.pickaboo.com/lifestyle/shaver-trimmer.html?p=1"
page_upto = 5
scrap_pickaboo(categorie_name, categorie_link, page_upto)