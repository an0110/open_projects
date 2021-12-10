import os
import re
import time
from pprint import pprint

site = "https://chaturbate.com/"

model_names = ['nikyblonnd', 'coverm', 'sweetygirlanastasia', 'belka22', 'victoria_tabu', 'joannabailes', 'stacy_swift',
'cassandra_19', 'antonia98x', 'mothcorrupts', 'i_am_sarahxxx', 'arabicsugar', 'emilymoons', 'lindacain', 'lauraxx_',
'hi_bye_', '_shania_', 'so_immoral', 'skycouple', 'clairelinn', 'miss_bee', 'alwayssomewhere', '_gabrielle_',
'skylar__', 'jenny_taborda', 'blondie___cake', 'beniceandhug', 'twix_girl', '2stars4you', 'ingridnight', 'emiliajons',
'decarabiasixth', '3threesomelove3', 'fetish_life', 'jenny_cute_', 'youramyx', 'extra_topping', 'tonnyign3', 'bat_bad',
'dianaholiday', 'jessacarter', 'queenafina', 'sherilyndior', 'julia_wilson', 'anabelle_wet', 'lollipop995',
'jessikabanks', 'mirniy', 'goddes_selene', 'wendyhale', 'lulacum69', 'diffgirls', 'nursedoll', 'kellytesh', 'jykfqy',
'alice_harris', 'kissamorous', 'alisa_bb', 'dakota_twin', 'rachelaniston', 'sophia__gray', 'queensy_sins_x',
'sexyru_couple','sweetsonnie', 'eva_maliby', 'katybugatti1', 'forsuperhero_', 'wildsexalexandalexis', 'onegreatdivaa',
'xjustajokex', 'catherinstone', 'sarahadams', 'getting_high_', 'jkxbk', 'mary_rosse', '_emily_rose_', 'melanie_miracle',
'arlyn_vicel', 'ninaxflower', 'haileygrx', 'anamistress', 'adrenaline_rush_', 'vanessa__queen', 'lusyanna', 'ms_evien',
'melanyredwine', 'ms_lola', 'sonya_kelsey', 'keira_knight', 'valerieluvsugar', "jacky_smith", "eveelynnex", "mirniy",
"jasminarcher", "cumwithjulie", "jessacarter", "nikyblonnd", "priya_rose", "sara_daisy", "catch_me_", "allicce_1",
"haileygrx"]


full_path = []
for el in model_names:
    el = site + el
    full_path.append(el)

old_links = []
with open ("name_full_links.txt") as fh:
    old_links = fh.readlines()


mmodels = []
for x in old_links:
    x = x.strip(".jpg")
    x = x.strip("\"url\"")
    x = x.strip("\"")
    x = x.strip(":")
    x = x.strip()
    x = x.strip("\"")
    mmodels.append(x)

old_links = mmodels
my_set = set()
for line in  full_path:
    my_set.add(line)

for line in  old_links:
    my_set.add(line)

pprint (my_set)
pprint (len(my_set))