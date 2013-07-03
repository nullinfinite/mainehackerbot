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
	else: return 0

@willie.module.interval(60)
def forumScan(bot):
	i = 8
	x = 0
	bytes = web.get('http://hackmaine.org/forums/')[7700:]
	if lastPost is 0:
		while i:
			x += bytes[x:].find('View the latest')
			if x == -1:
				return
			x += 64
			checkPost(bytes[x:x+25])
			i-=1
	else:
		while i:
			x += bytes[x:].find('View the latest')
			if x == -1:
				return
			x += 64
			if checkPost(bytes[x:x+25]):
				if i is 1:
					whichForum = 'Open Vehicle Tracker'
				if i is 2:
					whichForum = 'Electro-Mechanical'
				if i is 3:
					whichForum = 'Raspberry Pi'
				if i is 4:
					whichForum = 'Arduino'
				if i is 5:
					whichForum = 'Node.js'
				if i is 6:
					whichForum = 'Projects'
				if i is 7:
					whichForum = 'General Discussion'
				if i is 8:
					whichForum = 'Announcements and Events'
				bot.msg('#lucidchat', 'There is a new forum post in '+whichForum)
			i-=1
