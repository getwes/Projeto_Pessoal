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

#criando a planilha
workbook = openpyxl.Workbook()
#criando a pagina 'produtos'
workbook.create_sheet('produtos')
#selecionando a pagina produtos
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'produto'
sheet_produtos['B1'].value = 'preço'
# inserir os titulos e preços na planilha ##zip para que se um titulo não tiver um preço não é atribuido
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text,preco.text])
        
#salvar
workbook.save('./arquivos/produtos.xlsx')