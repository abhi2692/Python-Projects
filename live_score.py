import requests, prettify
from bs4 import BeautifulSoup

page = requests.get('http://www.cricbuzz.com/cricket-match/live-scores')
soup = BeautifulSoup(page.text, 'html5lib')

head_line = soup.findAll("h1", {"class": "cb-schdl-hdr cb-font-24 line-ht30"})
print(head_line[0].text)

print("------------------")

tours = soup.findAll("h2", {"class": "cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr"})

match = soup.findAll("h3", {"class":"cb-lv-scr-mtch-hdr inline-block"}, "title")

score = soup.findAll("div", {"class":"cb-lv-scrs-col text-black"})

for i, j, k in zip(range(len(tours)), range(len(match)), range(len(score))):
    print("Tour: " + tours[i].text)
    print(" ")
    print(match[j].text)
    print(score[k].text)
    print(" ")
    print("*********************************************")
    print(" ")

