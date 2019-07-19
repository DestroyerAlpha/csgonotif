from bs4 import BeautifulSoup
import requests


url = 'https://www.hltv.org/matches'
source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}).text

soup = BeautifulSoup(source, 'lxml')

live = soup.findAll("div", {"class" : "live-match"})
# print(live)

for match in live:
	event = match.find("div", {"class":"event-name"})
	maps = match.findAll(lambda tag: tag.name == 'td' and tag.get('class') == ['map'])
	teams = match.findAll("span", {"class":"team-name"})
	print(event.string)
	print(teams[0].string,"vs",teams[1].string)
	for index,mapping in enumerate(maps):
		map_number = index+1
		scores = match.findAll("span", {"data-livescore-map" : map_number})
		print(mapping.string,":",scores[0].string,"-",scores[1].string)

