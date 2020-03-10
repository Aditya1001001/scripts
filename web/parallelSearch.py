""" Searches google for 'query' written after the file name and opens the top 'limit' searches in new tabs. """


import urllib, webbrowser, sys
import requests
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = ' '.join(sys.argv[1:-1])
limit = int(sys.argv[-1])
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"
headers = {"user-agent": USER_AGENT}
res = requests.get(URL, headers=headers)
results = []
count = 0
if res.status_code == 200:
    soup = BeautifulSoup(res.content, "html.parser")
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            if count>=limit:
                break
            count+=1
            results.append(item)

for result in results:
    webbrowser.open(result["link"])