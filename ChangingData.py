

import pandas as pd

# get data
df = pd.read_csv('pokemon_data.csv')

print("\nMaking a 'Total' column which aggregates other stats: \n")
df["Total"] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df.head(5))

print("\ndf.drop() - deletes a column/row \n")
df = df.drop(columns=['Total'])
print(df.head(5))

print("\nA more succint approach to summation: \n")
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df)

print("\nOrdering: careful when hard-coding numbers like this \n")
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]
print(df)


