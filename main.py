"""Chatbot simple que responde a preguntas sobre precios de acciones y clima."""

# Importar librerías necesarias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

# Importar funciones de los agentes
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from funciones_agentes.obtener_clima import obtener_clima

# Importar funciones necesarias
from utils.sanitizar import sanitizar

# Configuración de Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled')

# Inicialización del driver con manejo correcto de rutas
driver_path = ChromeDriverManager().install()
if os.path.basename(driver_path) != 'chromedriver':
    potential_path = os.path.join(os.path.dirname(driver_path), 'chromedriver')
    if os.path.exists(potential_path):
        driver_path = potential_path
os.chmod(driver_path, 0o755)

driver = webdriver.Chrome(service=Service(driver_path), options=options)

def procesar_input(user_input):
    # Corregir la lógica de condiciones
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None

print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
while True:
    user_input = sanitizar(input("---> "))
    funcion_agente = procesar_input(user_input)
    if funcion_agente is None:
        print("No entendí tu solicitud. Intenta de nuevo.")
    else:
        respuesta = funcion_agente(driver, user_input)
        print(f">>> {respuesta}")