# John wood
# Aug 31, 2020
# this example is on freecodecamp
import urllib.request, urllib.parse, urllib.error
import bs4

url = input('Eneter - ')
html = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
