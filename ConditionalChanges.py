
import pandas as pd

df = pd.read_csv("Modified.csv")

print("\nConditional changes can be used to automate data processing:\n")

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamey boi'
print(df)
df.loc[df['Type 1'] == 'Flamey boi', 'Type 1'] = 'Fire'

print("\nYou can alter other columns than the one you are reading, like making all fire pokemon legendary:\n")
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

print(df)

df = pd.read_csv('Modified.csv')

print("\nYou use conditions on the data, and specify a list of changes\n")
df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['test 1','Test 2']
print(df)




