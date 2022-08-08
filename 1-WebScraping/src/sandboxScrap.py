import requests
import bs4

baseUrl = 'https://books.toscrape.com/catalogue/page-{}.html'
pageNumber = 1

res = requests.get(baseUrl.format(1))

soup = bs4.BeautifulSoup(res.text, 'lxml')

productList = soup.select('.product_pod')

example = productList[0]

rating = example.select(".star-rating.Three")
title = example.select("a")[1]['title']

twoStarTitles = []

for n in range(1, 51):
    scrapeUrl = baseUrl.format(n)
    res = requests.get(scrapeUrl)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    bookList = soup.select('.product_pod')

    for book in bookList:
        if "star-rating Two" in str(book):
            title = book.select("a")[1]['title']
            twoStarTitles.append(title)

print(twoStarTitles)