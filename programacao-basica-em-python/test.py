import imp
from selenium import webdriver
import pyperclip

navegador = webdriver.Edge()

navegador.get('http://www.mcce.org.br/newsletter#')

texto = navegador.find_elements('By.TAG_NAME','td')

for c in range(0,len(texto)):
    print(texto[c].text)