"""
This is just a code bruh
"""

import praw

reddit = praw.Reddit(               #Setting up bot 
    client_id="xV3mjpSwaS1xUQ",
    client_secret="F_YwNU8dbASUcQFW3bjEFSfNRkTzyQ",
    user_agent="<console:KARLSONBOT:0.1>",
    username="Karlson_Bot",
    password="njVLUt23gZeD4sQ",
)

subreddit = reddit.subreddit("DaniDev")  #Selecting subreddit

text = "Oh so you don't know what Karlson is? Karlson is just a little game Dany's working on and it's currently in the top 10 most wishlisted games. **SMASH WISHLIST NOW GAMERS SO WE CAN GET TO THE NUMBER ONE SPOT BABY!!!!!**"


for comment in subreddit.stream.comments(): #reading all new comments
		if hasattr(comment,"body"):             #This is to avoid problems with removed comments, which don't have a body
				if comment.author != "Karlson_Bot": #we do not want self-replies, do we?
						comment_low = comment.body.lower()
						if "karlson" in comment_low:    #looking for "Karlson"
								print(comment_low)
								#comment.reply(text)