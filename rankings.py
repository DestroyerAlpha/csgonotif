from bs4 import BeautifulSoup
import requests

url = 'https://www.hltv.org/ranking/teams/'
source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}).text

soup = BeautifulSoup(source, 'lxml')

ranking_container = soup.findAll("div",{"class":"ranked-team standard-box"})
top30 = []
for team in ranking_container:
	team_name = team.find("span",{"class":"name"}).string
	top30.append(team_name)
print(top30)


team1 = "ENCER"
team2 = "Vitality"

if team1 or team2 in top30:
	print("Okurrrrr")