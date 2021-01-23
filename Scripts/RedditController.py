import praw
from Scripts.envcontroller import ReturnEnv as gv
reddit = praw.Reddit(
     client_id=gv("REDDIT_ID"),
     client_secret=gv("REDDIT_CS"),
     user_agent=gv("REDDIT_UG")
 )
