# based on the links n this form https://www.cracked.com/humor-history.html?date_year=2020&date_month=1
# scrape the craced website and store all artcles n Docs or loca html / just articles and pcs now extra fllers
# use beautfullsou 4
from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = 'https://www.cracked.com/humor-history.html?date_year=2020&date_month=1'
x = requests.get(url)

# pprint(x.text)
# div class=content-cards-info
# print (x.find_all("content-cards-info") )

soup = BeautifulSoup(x.text, "html.parser")

content_cards_info = soup.find_all(class_='content-cards-info')
article_per_month_topic = []
for content in content_cards_info:
    print("****************")
    href = content.find_all("a", href=True)
    for link in href:
        # pprint(dir(link))
        if "https://www.cracked.com/article_" in link['href']:
            article_per_month_topic.append(link['href'])


for art in article_per_month_topic:
    art_x = requests.get(art)
    art_soup = BeautifulSoup(art_x.text, "html.parser")

    print (art_soup)

    delete_1 = art_soup.find_all("div")
    


    exit()


# to delete: div
# third_producer = soup.find_all("li")[2]
# div_name = third_producer.div
# div_name.decompose()
# print(third_producer.prettify())
# <div id="recommendedForYourPleasure">
#
# <header class="comments-header">
#
# < footer class ="footer" id="footer" >
#
