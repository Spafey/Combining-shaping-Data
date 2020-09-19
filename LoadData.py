
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#df_xlsx = pd.read_excel(' .xlsx')

#df_txt = pd.read_csv(' .txt', delimiter='\t')

print(df.head(5))
print(df.tail(5))

