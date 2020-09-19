
import pandas as pd


tmr = 0
print("\nit's possible to chunk data to get around size restrictions:\n")

for df in pd.read_csv('Modified.csv', chunksize=20):
    print("CHUNK DF")
    print(df)
    tmr = (tmr + 1)
print(tmr)

print("\nYou can declare a new dataframe borrowing columns prior dataframes:\n")
df = pd.read_csv('Modified.csv')
new_df = pd.DataFrame(columns=df.columns)

print("\n& Concatenation can be used to decrease data size while combining datasets: \n")

for df in pd.read_csv('Modified.csv', chunksize=20):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat(([new_df, results]))
    print(new_df)
