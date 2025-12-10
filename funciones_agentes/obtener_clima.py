from selenium.webdriver.common.by import By
from time import sleep

def obtener_clima(driver, consulta):
    '''
    Función para obtener el clima de una ciudad
    Parámetros:
    - driver: objeto de Selenium WebDriver
    - consulta: cadena de texto que contiene la consulta del usuario    
    '''

    driver.get(f"https://www.google.com/search?q=clima+{consulta}")
    sleep(2)

    try:
        # Obtener el nombre de la ciudad
        ciudad = driver.find_element(By.CSS_SELECTOR, "span[class='BBwThe']").text

        # Obtener la temperatura actual
        temperatura = driver.find_element(By.CSS_SELECTOR, "div[jscontroller='e0Sh5']").text

        return f"El clima en {ciudad} es de {temperatura}."
    except Exception as e:
        return "No se pudo obtener el clima en este momento."