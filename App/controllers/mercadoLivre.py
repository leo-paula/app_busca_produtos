from fastapi import HTTPException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome()
baseUrl = 'https://lista.mercadolivre.com.br/'

def getProductMercadoLivre(query):
    try:
        completeUrl = baseUrl + query
        web.get(completeUrl)
        time.sleep(1)
        returnedResults = []
        product_linksSaved = []
        product_link = web.find_element(By.XPATH, '//ol/li//h3/a')
        finalProduct = product_link.get_attribute('href')

        web.get(finalProduct)
        time.sleep(0.5)
        try:
            title = web.find_element(By.XPATH, '//h1[@class="ui-pdp-title"]').text
            shipment = web.find_element(By.XPATH, '//p[@class="ui-pdp-color--BLACK ui-pdp-family--REGULAR ui-pdp-media__title"]').text
            price = web.find_element(By.XPATH, '//span[@class="andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact"]').text.replace('\n', '')            
            seller = web.find_element(By.XPATH, '//div[@class="ui-pdp-seller__header__title"]').text
            times = web.find_element(By.XPATH, '//p[@class="ui-pdp-color--BLACK ui-pdp-size--MEDIUM ui-pdp-family--REGULAR"]').text
            description = web.find_element(By.XPATH, '//p[@class="ui-pdp-description__content"]').text
            rating = web.find_element(By.XPATH, '//span[@class="ui-pdp-review__rating"]').text
            

            images = []
            imagesBrute = web.find_elements(By.XPATH, '//img[@class="ui-pdp-image"]')
            for image in imagesBrute:
                srcImage = image.get_attribute('src')
                if srcImage:
                    images.append(srcImage)

            product = {'title': title,
                       'shipment': shipment,
                       'price': price,
                       'images': images,
                       'seller': seller,
                       'times': times,
                       'description': description,
                       'rating': rating}
            
        
            returnedResults.append(product)
            return returnedResults
            
        except Exception:
            returnedResults.append(None)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Não foi possível realizar a ação: {e}')
