import requests
import bs4

result = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(result.text, "lxml")

pageTitle = soup.select('title')[0].getText()

print(pageTitle)