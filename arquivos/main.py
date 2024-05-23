import os
import pandas as pd #pip install pandas

#import main2
#import main3
#print(main2,main3)

data_arquivo_folder = 'arquivos/'

df = []

for file in os.listdir(data_arquivo_folder):
    if file.endswith('.xlsx'):
        print('loading file{}...'.format(file))
        df.append(pd.read_excel(os.path.join(data_arquivo_folder, file)))
print(len(df))

df_principal = pd.concat(df, axis=0)
df_principal.to_excel('arquivos/master_store.xlsx', index=False)