from fastapi import HTTPException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome()
base_url = 'https://lista.mercadolivre.com.br/'

def safe_find(xpath):
    try:
        return web.find_element(By.XPATH, xpath).text
    except Exception:
        return None
    
def acess_base_site(base_url, query):
    complete = base_url + query
    web.get(complete)

def trim_links(brute_links):
    results = []
    for link in brute_links:
        src = link.get_attribute('href')
        if src:
            results.append(src)
    return results

def getProductMercadoLivre(query):
    try:
        acess_base_site(base_url, query)
        time.sleep(1)
        returnedResults = []
        brute_links = web.find_elements(By.XPATH, '//ol/li//h3/a')
        trimmed_links = trim_links(brute_links)

        try:
            for link in trimmed_links:

                web.get(link)
                title = safe_find('//h1[@class="ui-pdp-title"]')
                shipment = safe_find('//p[@class="ui-pdp-color--BLACK ui-pdp-family--REGULAR ui-pdp-media__title"]')
                price = safe_find('//span[@class="andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact"]')
                seller = safe_find('//div[@class="ui-pdp-seller__header__title"]')
                times = safe_find('//p[@class="ui-pdp-color--BLACK ui-pdp-size--MEDIUM ui-pdp-family--REGULAR"]')
                description = safe_find('//p[@class="ui-pdp-description__content"]')
                rating = safe_find('//span[@class="ui-pdp-review__rating"]')

                brute_product = {
                    'title': title,
                    'shipment': shipment,
                    'price': price,
                    'seller': seller,
                    'times': times,
                    'description': description,
                    'rating': rating
                }

                product = {}

                for fieldname, item in brute_product.items():
                    if item:
                        product[fieldname] = item

                returnedResults.append(product)
            return returnedResults
        except Exception as e:
                print(f"Error while scraping product: {e}")
                returnedResults.append(None)
                return returnedResults
    except Exception as e:
        print(f"Error in getProductMercadoLivre: {e}")
        raise HTTPException(status_code=400, detail=f'Não foi possível realizar a ação: {e}')