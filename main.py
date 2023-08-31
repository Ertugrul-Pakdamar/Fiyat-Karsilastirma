from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

turkceKarakterler = 'ŞşİıÖöĞğÜüÇç'
karakterDegisim = 'SsIiOoGgUuCc'

while True:
    searchedObject = input("Aratmak istediğiniz eşyanın adını yazınız. Çıkış yapmak için 'çıkış' yazınız: ")
    newSearchedObject = searchedObject

    if searchedObject == "çıkış":
        break

    driver = webdriver.Chrome()

    for i in newSearchedObject:
        for j in turkceKarakterler:
            if i == j:
                b = 0
                deger = turkceKarakterler.index(j)
                for i in karakterDegisim:
                    b = b + 1
                    if b-1 == deger:
                        newSearchedObject = searchedObject.replace(i, i)
    
    newSearchedObject = newSearchedObject.replace(" ", "%20")

    driver.get("https://www.cimri.com/arama?q=" + newSearchedObject)

    try:    
        search = driver.find_element(By.CSS_SELECTOR, "#cimri-product.z7ntrt-0.gLJVmk.s1a29zcm-7.bnaxiu")
        print(search.text)
        driver.quit()
    except:
        print("Arama başarısız oldu lütfen tekrar deneyiniz:")

