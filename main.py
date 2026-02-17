
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.sanitizar import sanitizar





"""Escribe una función llamada procesar_input que reciba como parámetro el texto que ingresó el usuario y regrese el texto "clima" en caso de que el usuario desee conocer el clima o la temperatura en alguna ciudad, o bien "precio" en caso de que se trate de una consulta sobre el precio de una acción.

//pseudocódigo

funcion procesar_input(texto)
  si el texto contiene palabras como clima o temperatura,
    return "clima"
  si el texto contiene palabras como precio o accion,
    return "precio"
  en todo caso contrario
    return None"""


def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return "clima"
    elif "precio" in user_input or "acción" in user_input:
        return "precio"
    else:
        return None
    
"""¡Debemos hacer un proceso de limpieza antes de procesar el input! Crea una función llamada santizar que reciba el input del usuario como parámetro y regrese el texto limpio:en minúsculas sin tildes sin ñ sin diéresis"""




print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
user_input = sanitizar(input("---> "))

