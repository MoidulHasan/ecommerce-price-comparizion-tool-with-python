import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Banglarshopers_Scraper(query):
    #Open File
    file = pd.read_csv('./banglashoppers.csv')

    #Declare Data
    price = 999999999999
    product_Data = []
    
    #Loop throw file
    for index, row in file.iterrows():
        #check wather query is present or not
        if query in str(row['products-name']):
            try:
                #initialize chrome web driver
                driver = webdriver.Chrome(ChromeDriverManager().install())

                #maximize browser
                driver.maximize_window()

                #scrap site data
                driver.get(row['products-link-href'])
                driver.implicitly_wait(3)

                #scrap price
                product_price = driver.find_element(By.CLASS_NAME, 'price').text
                product_price = product_price[2:] #onno site er belay eita baad jabe
                product_price = int(product_price)
                
                # check and set product data for lower priced product
                if(product_price<price):
                    price = product_price
                    product_title = driver.find_element(By.CLASS_NAME, 'base').text
                    product_url = row['products-link-href']
                    product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                    product_Data = [product_title, price, product_url, product_image_url]
                    
                #terminate webdriver
                driver.quit()
            except:
                pass
    
    return product_Data
       

qry = input('Enter Product Name: ')
product_Data = Banglarshopers_Scraper(qry)
print(product_Data)