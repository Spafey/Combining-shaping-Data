import pandas as pd

#get data
df = pd.read_csv('pokemon_data.csv')

print("\n Getting headers -  \n")
print(df.columns)

print("\nReading columns - can pass single or multiple columns - \n")
print(df[["Name", "Type 1", "HP"]])

print("\nInteger Location - df.iloc - can be used to grab specific rows - \n")
print(df.iloc[10:14])

print("\nOr read a specific location - \n")
print(df.iloc[2, 1])

print("\nUsing FOR loops to iterate over data - for each row in the data, print the corresponding index & row\n")
br = 0
for index, row in df.iterrows():

    if br < 10:
        print(index, row)
        br = br + 1

else:
    print("\n                     *capped for brevity*\n")

print("\n You can do the same thing while specifying the columns given\n")
crr = 0

for index, row in df.iterrows():
    if crr < 10:
        print(index, row['Name'])
        crr = crr + 1
else:
    print("\n                     *capped for brevity*\n")

print("\n df.loc - finding specific data without specifically asking for numerical data, e.g., textual\n")
print(df.loc[df['Type 1'] == "Fire"])

print("\n df.describe - gives basic stats about the dataframe: \n")
print(df.describe())

print("\n df.sort_values - allows sorting of columns based on given rules: \n")
print(df.sort_values("Name", ascending=False))


print("\nYou can also use multiple sorts - eg., 'type 1' & 'HP'\n")
print(df.sort_values(["Type 1", "HP"], ascending=[1, 0]))




