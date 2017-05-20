#based on script by /u/GoldenSights
import praw
import time
import datetime

USER = ''
PASSWORD = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
USER_AGENT = ''
SUBREDDIT = ''
WAIT = 60

def write_log(text):
    print(text)
    log = open('log_deleted_authors.txt', 'a')
    log.write('{} {}\n'.format(str(datetime.datetime.now()),text))
    log.close()

write_log("Logging in")
r = praw.Reddit(client_id = CLIENT_ID,
                client_secret = CLIENT_SECRET,
                user_agent = USER_AGENT,
                username = USER,
                password = PASSWORD)

def scanSub():
    subreddit = r.subreddit(SUBREDDIT)
    posts = subreddit.new()
    for post in posts:
        try:
            pauthor = post.author.name
        except AttributeError:
            write_log('{} is being removed'.format(post.id))
            post.delete()
            write_log('Done')

write_log('Searching '+ SUBREDDIT + '.')
while True:
    try:
        scanSub()
    except Exception as e:
        print('An error has occured:', e)
    time.sleep(WAIT)