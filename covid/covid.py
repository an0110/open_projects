import json
from  pprint import pprint
from time import time, sleep
from urllib.request import urlopen


## get updated stats from site
url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json"
json_url = urlopen(url)
data = json.loads(json_url.read())

# # read from local manually downloaded file
# with open("covid_stats.json", "r") as fh:
#     data = json.load(fh)


deaths_lst = []
death_country = {}

for item in data['records']:
    if item['countriesAndTerritories']  in death_country:
        death_country [item['countriesAndTerritories']] = death_country [item['countriesAndTerritories']] + int(item['deaths'])
    else:
        death_country[item['countriesAndTerritories']] = int(item['deaths'])

    deaths_lst.append(   death_country   )

death_dict = deaths_lst[-1]

# print(len(death_dict))
# sorted = {k: v for k, v in sorted(death_dict.items(), key=lambda item: item[1])}
# how to sort dict by val --- need to understand

death_computed_list = []
for k, v in death_dict.items():
    death_computed_list.append(v)

sum_80_per = 0
sum_total = 0
for item in death_computed_list:
    sum_total += item

death_computed_list_no_zero = death_computed_list
death_computed_list_no_zero.remove(0)
death_computed_list_no_zero.sort()
for item in range(round(0.8*len(death_computed_list_no_zero))):
    sum_80_per += death_computed_list_no_zero[item]


max_deaths = death_computed_list_no_zero[-1]
counter = 0
for item in reversed(death_computed_list_no_zero):
    if item != max_deaths:
        print(max_deaths)
        max_deaths -= item
    if max_deaths > 0:
        counter += 1
    else:
        break

# *************************************************************************************************
print("="*100)
# print (death_computed_list_no_zero)
print("totl: {}".format(sum_total))
print("80% countries have {}% deaths".format(sum_80_per/sum_total*1000) )
print("max out of total : {}".format(death_computed_list_no_zero[-1]/sum_total) )
print("deaths in 1st country = deaths in the next {} countires combined".format(counter))
print("="*100)


# https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data
# https://opendata.ecdc.europa.eu/covid19/casedistribution/json
# # webpage that displayes stats about covid -
# # use django. pyspark
# # use the probabilistic stuff: gauss bell, paretto principle, etc
# what a DOCTEST
# encapsulation
#
# runtime compplexity of .append on list  O notation
#
