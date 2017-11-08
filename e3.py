import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

election = []
for i in range(1924,2020,4):
    file = "president_general_{}.csv"
    header = pd.read_csv(file.format(i), nrows = 5).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(file.format(i), index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = i
    election.append(df.loc[:,["Democratic","Republican","Total Votes Cast","Year"]])

df1 = pd.concat(election)

county = ["Accomack County","Albemarle County","Alexandria City","Alleghany County"]
df1["Republican Share"] = df1["Republican"] / df1["Total Votes Cast"]

accomack = df1.loc['Accomack County'].astype(float)
albemarle = df1.loc['Albemarle County'].astype(float)
alexandria = df1.loc['Alexandria City'].astype(float)
alleghany = df1.loc['Alleghany County'].astype(float)
fig1 = accomack.plot(kind = "bar", x = "Year", y = "Republican Share", title = "Accomack County")
fig1.get_figure().savefig('accomack_county.pdf')
fig2 = albemarle.plot(kind = "bar", x = "Year", y = "Republican Share", title = "Albemarle County")
fig2.get_figure().savefig('albemarle_county.pdf')
fig3 = alexandria.plot(kind = "bar", x = "Year", y = "Republican Share", title = "Alexandria City")
fig3.get_figure().savefig('alexandria_city.pdf')
fig4 = alleghany.plot(kind = "bar", x = "Year", y = "Republican Share", title = "Alleghany County")
fig4.get_figure().savefig('alleghany_county.pdf')
