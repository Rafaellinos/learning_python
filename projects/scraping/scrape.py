# every web site has /robots.txt to show what u can screap

# beatifulsoap -> pip3 install beautifulsoup4
# requests -> pip3 install requests

import requests
from bs4 import BeautifulSoup
import pprint


# parse html.parser, can have something like xml.parser
# print(soup.body)
# print(soup.find_all('a'))
# print(soup.select('.score')) # grab all the elements that has a class score
# print(soup.select('#score')) # grab all the elements that has that id

def get_page(page_num):
    """
    makes the request to hacker news and parse the html to beautiful soup
    """
    try:
        res = requests.get(f'https://news.ycombinator.com/news?p={page_num}')
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    except Exception as err:
        print(f"Error: {err}")
        exit()
    

def sort_stories_by_votes(hn):
    """
        receive a list of dics and sort based on the key points.
        the key= param only receice a function to select which item
        will be selected.
        Also reverse the list.
    """
    return sorted(hn,key=lambda hn: hn['points'], reverse=True)

def create_custom_hn(links, subtext):
    """
        params: links, to get href and title

        select the class .score from subtexts
        and see if has score on it.
        if has score, tranform the score string into a int
        checks if ponts is greater than 99, if yes, append the title, link and points
        
        return: List of dics containing title, link and points.
    """
    hn = []
    for i, item in enumerate(links):
        title = item.getText() # get the titles on the page
        href = item.get('href', None) # get the href of the story
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'points': points})
    return hn

pages = 2

lista = []
for page in range(pages):
    s = get_page(page)
    links = s.select('.storylink')
    subtexts = s.select('.subtext')
    lista += create_custom_hn(links, subtexts)


pprint.pprint(sort_stories_by_votes(lista))