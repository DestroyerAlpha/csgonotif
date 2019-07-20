from bs4 import BeautifulSoup
import requests
import json
import urllib.request as urllib2
import threading
import os
import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    print(message)
    return


def clear():
    os.system('clear')

url = 'https://www.hltv.org/ranking/teams/'
source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}).text
soup = BeautifulSoup(source, 'lxml')
ranking_container = soup.findAll("div",{"class":"ranked-team standard-box"})
top30 = []
for team in ranking_container:
	team_name = team.find("span",{"class":"name"}).string
	top30.append(team_name)


def scoreRetreiver():
	clear()
	threading.Timer(115.0,scoreRetreiver).start()
	url = 'http://esportlivescore.com/g_csgo.html'
	source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}).text
	soup = BeautifulSoup(source, 'lxml')
	filtered = soup.findAll("div",{"data-status":"Started"})

	for div in filtered:
		match_id = div['data-event-id']
		match_info = div.find("div", {"class":"event-tournament-info"})
		event_name = match_info.a['title']
		
		teams = div.a['title']
		team1,team2 = teams.split(" vs ")
		message = ""
		if team1 in top30 or team1 in top30:
			message += '\n'+event_name+'\n'
			message+= teams + '\n'
			api_url = "http://dc1.esportlivescore.com/api/events?ids[]="+str(match_id)
			data = json.load(urllib2.urlopen(api_url))
			data = data[0]
			maps = data['maps']
			scores = data['scores']
			for map_no in maps:
				if maps[map_no] != None:
					team1 = 'team_1_cell_'+map_no
					team2 = 'team_2_cell_'+map_no
					score1 = scores[team1]
					score2 = scores[team2]
					notification = maps[map_no]+" : "+score1+" - " + score2
					message += notification + '\n'
		if message != "":
			sendmessage(message)


scoreRetreiver()

