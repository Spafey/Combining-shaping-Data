
import pandas as pd

df = pd.read_csv('Modified.csv')

print("\nFilters can be applied to columns:\n")

print(df.loc[df['Type 1'] == 'Grass'])

print("\n & can filter from multiple columns at once\n")

abc = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
print(abc[["Name", "Type 1", "Type 2"]])

print("\n You can also check for text &/or add conditions:\n")

defg = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print(defg[["Name", "Type 1", "Type 2", "HP"]])

#defg.to_csv('FilteredGrassPoison.csv')

print("\nAlter the index with df.reset_index() - (drop=Bool, inplace=Bool)\n")
defg = defg.reset_index(drop=True)

print(defg[["Name", "Type 1", "Type 2", "HP"]])


print("\nRegex filtering is  ")
