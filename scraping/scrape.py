import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res)
# grab the data only in string format, don't need styling info
# print(res.text)
# give string, and convert type (html/xml), creates soup object
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print(soup.body.contents)
# find all a tags - links on page
# print(soup.find_all('a'))
# print(soup.title)
# can grab the id belonging to a certain tag like the score/vote
# print(soup.find(id="score_24575770"))

# using a css selector, grab all scores within the span class
# .score = class
# print(soup.select('.score'))
# print(soup.select('#score_24593028'))

#grab link item
# print(soup.select('.storylink')[0])
#grab vote item
# print(soup.select('.score')[0])

links = soup.select('.storylink')
votes = soup.select('.score')
# print(votes[0])
# votes.get to get attribute

# href attribute is actual link
def create_custom_hm(links, votes):
    hn = []
    for index, item in enumerate(links):

        title = links[index].getText()
        # default second param in case no link
        href = links[index].get('href', None)
        # there are some stories that don't have votes, making votes list shorter than link list
        points = int(votes[index].getText().replace(' points', ''))
        print(points)
        hn.append({'title': title, 'link': href})
    return hn


print(create_custom_hm(links, votes))
