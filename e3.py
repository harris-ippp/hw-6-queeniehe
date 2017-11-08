import pandas as pd
import matplotlib.pyplot as plt

election = []
for i in range(1924,2020,4):
    file = "president_general_{}.csv"
    header = pd.read_csv(file.format(i), nrows = 5).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(file.format(i), index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = i
    election.append(df[["Democratic","Republican","Total Votes Cast","Year"]])

df = pd.concat(election)

df["Republican Share"] = df["Republican"] / df["Total Votes Cast"]
df.reset_index(inplace=True)

AccomackCounty = df['Accomack County'].sort_values(by = 'Year', ascending = True)
fig1 = AccomackCounty.plot(x = "Year", y = "Republican Share", kind = "bar", title = "Republican Vote Share of Accomack County")
fig1.get_figure().savefig('accomack_county.pdf')

AlbemarleCounty = df['Albemarle County'].sort_values(by = 'Year', ascending = True)
fig2 = AlbemarleCounty.plot(x = "Year", y ="Republican Share", kind = "bar", title = "Republican vote share in Accomack County")
fig2.get_figure().savefig('albemarle_county.pdf')

AlexandriaCity = df['Alexandria City'].sort_values(by = 'Year', ascending = True)
fig3 = AlexandriaCity.plot(x = "Year", y ="Republican Share", kind = "bar", title = "Republican Vote Share of Alexandria City")
fig3.get_figure().savefig('alexandra_city.pdf')

AlleghanyCounty = df['Alleghany County'].sort_values(by = 'Year', ascending = True)
fig4 = AlleghanyCounty.plot(x = "Year", y = "Republican Share", kind = "bar", title = "Republican Vote Share of Alleghany County")
fig4.get_figure().savefig('alleghany_county.pdf')
