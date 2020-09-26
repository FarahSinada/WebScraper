import requests
from bs4 import BeautifulSoup
import pprint #pretty print

res = requests.get('https://news.ycombinator.com/news')
# print(res)
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

subtext = soup.select('.subtext')

# get url of next page, a is hyperlink tag
next_page_url = soup.find_all('a', {'class': 'morelink', 'rel': 'next'})
# print(next_page_url[0].get('href'))
if next_page_url:
    next_page_url = 'https://news.ycombinator.com/' + next_page_url[0].get('href')
    # print(next_page_url)

res2 = requests.get(next_page_url)
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup2)

links2 = soup2.select('.storylink')
subtext2 = soup.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)


def create_custom_hm(links, subtext):
    hn = []
    # enumerate to have index for subtext
    for index, item in enumerate(links):

        title = links[index].getText()
        # default second param in case no link
        href = links[index].get('href', None)
        # there are some stories that don't have votes, making votes list shorter than link list
        vote = subtext[index].select('.score')
        # if there is a vote attribute in the subtext, i.e. vote !=null
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})


    return sort_stories_by_votes(hn)


# print(create_custom_hm(links, subtext))
pprint.pprint(create_custom_hm(mega_links, mega_subtext))

