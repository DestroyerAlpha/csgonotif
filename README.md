# csgonotif
A small python program which gives you live scores of the matches being played by Top 30 teams.

This program first retrieves the HLTV top 30 teams. Then it only gives you the notification about the live matches played by these teams.
(Because honestly, no one gives a crap about other matches.)

It updates the score every 1 min 55 secs, that is how long a CSGO round usually lasts. It updates the score on the terminal as well as
sends you a notification.

I have used the data from the website http://esportlivescore.com and also used there API for the live scores.
My initial attempt was to use HLTV but they have a private API and the score updation mechanics on their website sucks.

I plan to also incorporate a SMS notif service using Twilio.
