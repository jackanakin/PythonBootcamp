import requests
import bs4

siteUrl = 'https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)'

result = requests.get(siteUrl)

soup = bs4.BeautifulSoup(result.text, "lxml")

images = soup.select('.thumbimage')

computerImg = images[0]
computerImgSrc = computerImg['src']
computerImgReq = requests.get('https:' + computerImgSrc)

f = open("computer_image.jpg", "wb")
f.write(computerImgReq.content)
f.close()