
import pandas as pd


df = pd.read_csv('Modified.csv')

print("\nGroupby can look at the 'Type 1' column, grouping similar (identical?) objects & returning the mean:\n")
print(df.groupby(['Type 1']).mean())

print("\nSort_values() can be used here - e.g., type organized by mean defense:\n")
print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))

print("\nOrganized by 'Attack\n")
print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

print("\nOrganized by 'Sp. Atk\n")
print(df.groupby(['Type 1']).mean().sort_values('Sp. Atk', ascending=False))

print("You could also use sum() - not really useful here\n")
print(df.groupby(['Type 1']).sum())

print("\nThere is also count():\n")
print(df.groupby(['Type 1']).count())

print("\n just returning a 'count' variable is slightly cleaner:\n")
df['count'] = 1
print(df.groupby(['Type 1']).count()['count'])

print("\nYou can also group using multiple columns:\n")
print(df.groupby(['Type 1', 'Type 2']).count()['count'])




