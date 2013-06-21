
import willie.web as web
import time
import willie.module


lastPost = 0

def checkPost(dateData):
	global lastPost
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
			bytes = bytes[x:]
			x = bytes.find('View the latest')
			x += 64
			dateData = bytes[x:x+25]
			if dateData[24] is '<':
				dateData = dateData[:24]
			elif dateData[23] is '<':
				dateData = dateData[:23]
			checkPost(dateData)
			i-=1
	else:
		while i:
			bytes = bytes[x:]
			x = bytes.find('View the latest')
			x += 64
			dateData = bytes[x:x+25]
			if dateData[24] is '<':
				dateData = dateData[:24]
			elif dateData[23] is '<':
				dateData = dateData[:23]
			if checkPost(dateData):
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
				bot.msg('#mainehackerclub', 'There is a new forum post in '+whichForum)
			i-=1
	
