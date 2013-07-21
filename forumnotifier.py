import willie.web as web
import time
import willie.module

lastPost = 0

def checkPost(dateData):
	global lastPost
	if dateData[24] is '<':
		dateData = dateData[:24]
	elif dateData[23] is '<':
		dateData = dateData[:23]
	timeStamp = time.mktime(time.strptime(dateData, '%a %b %d, %Y %I:%M %p') )
	if timeStamp > lastPost:
		lastPost = timeStamp
		return 1
	else: 
		return 0

@willie.module.interval(40)
def forumScan(bot):
	x = 1
	bytes = web.get('http://hackmaine.org/forums/')[7700:]
	if lastPost is 0:
		while bytes[x:].find('View the latest') != -1:
			x += bytes[x:].find('View the latest') + 64
			checkPost(bytes[x:x+25])
	else:
		while bytes[x:].find('View the latest') != -1:
			x += bytes[x:].find('View the latest') + 64
			if checkPost(bytes[x:x+25]):
				loc = bytes[:x].rfind('forumtitle') + 12
				forum = bytes[loc : bytes[loc:].find('<')+loc]
				forum = forum.replace('&amp;', '&')
				loc += bytes[loc:].find('./viewtopic')
				url = bytes[loc : bytes[loc:].find('>') + loc - 1]
				url = 'http://www.hackmaine.org/forums'+url[1:]
				url = url.replace('&amp;', '&')
				bot.msg('#lucidchat', 'There is a new forum post in '+forum+': '+url)
