from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests 




def scrap_jadroo(categorie_name, category_slug, page_upto):
    # declare file name and open file
    filename = './data/jadroo-products.csv'
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        while(i<=page_upto):
            url = "https://contents.jadroo.com/api/v1/category/products?category_slug={}&sorting=&page={}".format(category_slug,i)
            print("Page No988: ", i, url)
            res = requests.get(url).json()
            for item in res["results"]["products"]["data"]:
                data = {}
                data['category'] = categorie_name
                data['products-name'] = item["name"]
                data['products-link'] = "https://www.jadroo.com/products/"+ item["product_slug"]
                print(data)
                w.writerow(data)
            i+=1
        f.close()


categorie_name = "consumer-electronics"
category_slug= "consumer-electronics"
page_upto = 15
scrap_jadroo(categorie_name, category_slug, page_upto)