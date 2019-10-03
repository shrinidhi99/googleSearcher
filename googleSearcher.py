import requests
import sys
import webbrowser
import bs4

res = requests.get('https://google.com/search?q=shrinidhi99')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
# linkElements = soup.select('.r a')
# linkToOpen = min(5, len(linkElements))
i = 0
for a in soup.find_all('a', href=True):
    if i < 100:
        webbrowser.open(a['href'])
        i += 1
    else:
        break
