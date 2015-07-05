# coding=utf-8
import praw
import time
import multiprocessing

USER = ''
PASSW = ''

def proc(q):
    while True:
        time.sleep(15)
        reddit = q.get(block=True,timeout=None)
        try:
            for msg in list(reddit.get_unread(limit=None)):
                print('AUTHOR: %s - SUBJECT: %s - BODY: %s' % (msg.author, msg.subject, msg.body))
                msg.mark_as_read()
        except Exception as e:
            print('exception: ' + str(e))
        q.put(reddit)

if __name__ == '__main__':
    r = praw.Reddit(user_agent='testbr',handler=praw.handlers.MultiprocessHandler('localhost',10101))
    r.login(USER, PASSW)
    if r.is_logged_in():
        print('logged in')
    else:
        print('failed to log in')
        
    queue = multiprocessing.Queue()
    queue.put(r)
    
    p = multiprocessing.Process(target=proc,args=(queue,))
    p.start()
    
    p.join()
    
