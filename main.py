from bs4 import BeautifulSoup as bs
import requests


url = 'http://sofifa.com/players?offset=0'


def soup_maker(url):
    r = requests.get(url)
    markup = r.content
    soup = bs(markup, 'lxml')
    return soup


def find_player_secondary_info(soup):
    player_data = {}
    player_data['preff_foot'] = soup.find('label', text='Preferred Foot') \
        .parent.contents[2].strip('\n ')
    player_data['club'] = soup.find('ul').find('a').text
    player_data['club_pos'] = soup.find('label', text='Position') \
        .parent.find('span').text
    return player_data


soup = soup_maker(url)
data = find_player_secondary_info(soup)

for key, value in data.items():
    print(key, value)
