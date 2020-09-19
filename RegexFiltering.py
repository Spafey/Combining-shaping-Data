
import pandas as pd
import regex as re
df = pd.read_csv('Modified.csv')

print("\nUsing df.loc[] to find a column name & using str.contains() to filter fields containing the string 'Mega'\n")
print(df.loc[df["Name"].str.contains('Mega')])

print("\nthis can also be used to remove certain phrases/responses:\n")
print(df.loc[~df["Name"].str.contains('Mega')])

print("\nYou can also hand str.contains() regular expressions - flags=re.I -  tells the loc to ignore case: \n")
print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])

print("\n Using Regex to search through the 'Name' column - .str.contains(Pi[a - z]*) - accepts metacharacters assuming 'pi' exists\n ")
print(df.loc[df['Name'].str.contains('Pi[a - z]*', flags=re.I, regex=True)])

print("\n  accepts metacharacters assuming 'pi' exists, but controls start of line using '^' :\n ")
print(df.loc[df['Name'].str.contains('^Pi[a - z]*', flags=re.I, regex=True)])

