from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#Acessar o site https://www.novaliderinformatica.com.br/computadores
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores')

#Coletando os nomes dos produtos (Perifericos)
titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

#Coletando os preços dos produtos (Perifiericos)
precos = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")

for titulo, preco in zip(titulos, precos):
    for dados in(titulo.text,preco.text):
        print(dados)