
import pandas as pd
import numpy as np

df = pd.read_excel('sales-funnel.xlsx')
print(df.head())
print(df.tail())

df["Status"] = df["Status"].astype("category")
df["Status"].cat.set_categories(["won", "pending", "presented", "declined"], inplace=True)

print("\nStandard pivot\n")
print(pd.pivot_table(df, index=["Price"]))

print("\nMultiple Indexes\n")
print(pd.pivot_table(df, index=["Manager", "Rep"]))

print("\n Values[] - designates the information you want to look at ")
print(pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"]))

print("\n aggfunc - aggregate functions allow for mathematic operations\n")
print(pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=np.sum))

print("\n aggfunc[np.mean,len] - mean using len to count\n")
print(pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=[np.mean,len]))

print("\n Sales broken down by products & Quantity using columns - fill_value used to format cells\n")
print(pd.pivot_table(df, index=["Manager", "Rep"], values=["Price", "Quantity"],
                     columns=["Product"], aggfunc=[np.sum], fill_value=0))

print("\n The same breakdown - better formatting achieved by moving 'Product' into the index\n")
print(pd.pivot_table(df,index=["Manager", "Rep", "Product"],
                     values=["Price", "Quantity"], aggfunc=[np.sum], fill_value=0))

print("\nmargins=True - gives totals\n")
print(pd.pivot_table(df,index=["Manager", "Rep", "Product"],
                     values=["Price", "Quantity"], aggfunc=[np.sum,np.mean], fill_value=0, margins=True))

print("\n Manager's sales performance\n")

print(pd.pivot_table(df, index=["Manager","Status"], values=["Price"],
                     aggfunc=[np.sum], fill_value=0, margins=True))

print("\nYou can pass aggfunc libraries, enabling aggfunc to perform different functions for different values:\n")
print(pd.pivot_table(df,index=["Manager", "Status"], columns=["Product"], values=["Quantity","Price"],
                     aggfunc={"Quantity":len,"Price":np.sum}, fill_value=0))

print("\nYou can provide a list within the library, to target a specific value with multiple aggfunctions\n")
table = pd.pivot_table(df,index=["Manager","Status"],columns=["Product"],values=["Quantity","Price"],
               aggfunc={"Quantity":len,"Price":[np.sum,np.mean]},fill_value=0)

print("\nOnce the data is generated you can filter using standard DataFrame functions\n")

print(table)

print("\nQuery a single manager\n")

print(table.query('Manager == ["Debra Henley"]'))

print("\nFiltered for pending & won deals\n")

print(table.query('Status == ["pending","won"]'))