import bs4
import requests

url = 'http://www.jadwalsholat.pkpu.or.id/?id=296'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
print(data)

sholat = {}
i = 0
for i in data():
    if i == 1:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['zuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1

print(sholat)
#print(sholat['subuh'])