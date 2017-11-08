from bs4 import BeautifulSoup as bs
import requests

url = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
req = requests.get(url)
soup = bs(req.content,'html.parser').find_all('tr','election_item')

ELECTION_ID = []
for t in soup:
    y1 = t.td.text
    y2 = t['id'][-5:]
    y = [y1, y2]
    ELECTION_ID.append(y)
    print(y1, y2)

with open('ELECTION_ID', 'w') as file:
    for line in ELECTION_ID:
        file.write(line[0] + ' ' + line[1])
        print(line[0],line[1])
