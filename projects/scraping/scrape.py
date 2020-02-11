# every web site has /robots.txt to show what u can screap

# beatifulsoap -> pip3 install beautifulsoup4
# requests -> pip3 install requests

import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# parse html.parser, can have something like xml.parser
# print(soup.body)
# print(soup.find_all('a'))
print(soup.select('.score')) # grab all the elements that has a class score
print(soup.select('#score')) # grab all the elements that has that id