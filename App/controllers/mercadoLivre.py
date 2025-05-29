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
        product_links = web.find_elements(By.XPATH, '//ol/li//h3/a')
        for link in product_links:
            href = link.get_attribute('href')
            if href:
                product_linksSaved.append(href)

        for linkProductX in product_linksSaved:
            web.get(linkProductX)
            time.sleep(0.5)
            try:
                title = web.find_element(By.XPATH, '//h1[@class="ui-pdp-title"]').text
                shipment = web.find_element(By.XPATH, '//p[@class="ui-pdp-color--BLACK ui-pdp-family--REGULAR ui-pdp-media__title"]').text
                price = web.find_element(By.XPATH, '//span[@class="andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact"]').text.replace('\n', '')

                images = []
                imagePicker = web.find_elements(By.XPATH, '//img[@class="ui-pdp-image"]').text
                
                images.append(imagePicker)

                product = {'title': title,
                           'shipment': shipment,
                           'price': price,
                           'images': images}
                
                returnedResults.append(product)
            except Exception:
                returnedResults.append(None)

        return returnedResults
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Não foi possível realizar a ação: {e}')
