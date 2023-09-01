from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

while True:
    searchedObject = input("Aratmak istediğiniz eşyanın adını yazınız. Çıkış yapmak için 'çıkış' yazınız: ")
    newSearchedObject = searchedObject

    if searchedObject == "çıkış":
        break

    newSearchedObject = newSearchedObject.replace("ğ", "g")
    newSearchedObject = newSearchedObject.replace("ı", "i")
    newSearchedObject = newSearchedObject.replace("İ", "I")

    
    driver = webdriver.Chrome()
    
    newSearchedObject = newSearchedObject.replace(" ", "%20")

    driver.get("https://www.cimri.com/arama?q=" + newSearchedObject)

    try:    
        search = driver.find_element(By.CSS_SELECTOR, "#cimri-product.z7ntrt-0.gLJVmk.s1a29zcm-7.bnaxiu")
        print(search.text)
        driver.quit()
    except:
        print("Arama başarısız oldu lütfen tekrar deneyiniz:")
        driver.quit()
