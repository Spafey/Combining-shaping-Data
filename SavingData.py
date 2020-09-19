
import pandas as pd

# get data
df = pd.read_csv('pokemon_data.csv')

# Modify data
df["Total"] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# Create csv file in the project directory:

df.to_csv('Modified.csv', index=False)

# There are issues with Pandas & Openpyxl that are above my head.
# # quick and dirty fixes apparently include overwriting the header_style dictionary,
# downgrading openpyxl to 1.86,
# or just using anaconda ( i got it working by uninstalling & reinstalling openpyxl without specifying versions)

#pd.core.format.header_style = None
df.to_excel('Modified.xlsx', index=False)

# Saving to a specific tab:

df.to_csv('modified.txt', index=False, sep='\t')


