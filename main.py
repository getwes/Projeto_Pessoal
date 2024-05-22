#Importando bibliotecas
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

from main2 import test
from main3 import dados

#criando a planilha
workbook = openpyxl.Workbook()
#criando a pagina 'produtos'
workbook.create_sheet('produtos')
#selecionando a pagina produtos
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'produto'
sheet_produtos['B1'].value = 'preço'
# inserir os titulos e preços na planilha ##zip para que se um titulo não tiver um preço não é atribuido
for total in zip(test,dados):
    sheet_produtos.append([total.text])

#salvar
workbook.save('produtos.xlsx')





#if dados == '1,000':
    #print(dados)
#else:
    #print('wesley deu certo n')