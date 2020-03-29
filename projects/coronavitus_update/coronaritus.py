import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

"""
pip3 install requests
pip3 install beautifulsoup4
pip3 install plyer
"""

res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')
cases = soup.find_all("div", {'class': 'maincounter-number'})
cases = [case.get_text().strip() for case in cases]

def notify_me(tittle, message):
    notification.notify(
        title = tittle,
        message = message,
        timeout = 5)

while True:
    notify_me('Corona Alert', f'Total cases {cases[0]} Deaths {cases[1]} Recovered {cases[2]}')
    time.sleep(600)