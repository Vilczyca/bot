import praw
import pdb
import re
import os



reddit = praw.Reddit('asd')

#Sprawdza czy path.isfile istnieje
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read() #Zczytuje cały tekst
        posts_replied_to = posts_replied_to.split("\n") #Bierze to zczytane i tworzy liste
        posts_replied_to = list(filter(None, posts_replied_to)) #Usuwa wszystkie niepotrzebne puste miejsca

subreddit = reddit.subreddit('pythonforengineers')#Robi zmienną i łączy się z subreddit
for submission in subreddit.hot(limit=10): #Bierze pierwsze 10

    if submission.id not in posts_replied_to: #Sprawdza, czy to id nie było już wcześniej wpisane

        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Du rum dum dum, du rum dum dum,du rum du rum du rum du rum du dumdumdumdumdumdumdumdum")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")