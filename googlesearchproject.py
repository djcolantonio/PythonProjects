import requests, sys, webbrowser, bs4

print('Searching...')

res = requests.get('http://google.com/search?q=music'+' '.join(sys.argv[1:]))
res.raise_for_status() #change keyword at end for search bar

soup = bs4.BeautifulSoup(res.text, 'lxml')

linkElems = soup.select('.r a')

numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

