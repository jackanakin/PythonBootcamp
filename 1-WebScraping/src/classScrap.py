import requests
import bs4

siteUrl = 'https://en.wikipedia.org/wiki/Grace_Hopper'

result = requests.get(siteUrl)

soup = bs4.BeautifulSoup(result.text, "lxml")

content = soup.select('.toctext')

for item in content:
    print(item.text)