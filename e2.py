from bs4 import BeautifulSoup as bs
import requests

url = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
req = requests.get(url)
soup = bs(req.content,'html.parser').find_all('tr','election_item')

year = []
for t in soup:
    year.append(t.contents[1].text)

ELECTION_ID = []
for i in range(len(soup)):
    ELECTION_ID.append(soup[i]['id'][-5:])

file = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"
d = dict(zip(ELECTION_ID, year))

for id in ELECTION_ID:
    data = file.format(id)
    text = requests.get(data).text
    ElecYearData = "president_general_" + d[id] + ".csv"
    with open(ElecYearData, 'w') as output:
