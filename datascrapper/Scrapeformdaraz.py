from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
driver = webdriver.Chrome(ChromeDriverManager().install())

#implicit wait
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()


filename = './data/daraz-all-new.csv'
with open(filename, 'a', newline='') as f:
    w = csv.DictWriter(f,['category','products-name','products-link'])
    w.writeheader()

    category = "Treadmills"
    i=1
    while(i<=5):
      driver.implicitly_wait(5)
      url = "https://www.daraz.com.bd/treadmills/?page={}&spm=a2a0e.searchlistcategory.cate_11.1.30134e47ScR5KE".format(i)

      print(url)
      driver.get(url)
      driver.implicitly_wait(5)
      i+=1
      items = driver.find_elements(By.CLASS_NAME, 'c3KeDq')
      for item in items:
        namediv = item.find_element(By.CLASS_NAME, 'c16H9d')
        link = item.find_element(By.TAG_NAME, 'a')
        url = link.get_attribute('href')
        name = link.get_attribute('innerHTML')
        data = {}
        data['category'] = category
        data['products-name'] = name
        data['products-link'] = url
        print(data)
        
        w.writerow(data)
    f.close()