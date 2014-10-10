import praw

def main():
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    r = praw.Reddit(user_agent='flairbotbr')
    r.login('botbr', '***REMOVED***')
    while True:
        for msg in r.get_unread(limit=None):
            print type(msg.subject)
            print type(msg.author)
            print type(msg.body)
            #print "Subject: " + str(msg.subject)
            #print "author: " + str(msg.author)
            #print "body: " + str(msg.body)
            flairstr = msg.subject
            '''
            if len(flairstr.split(',')) == 2:
                sigla_estado = flairstr.split(',')[1].strip()
                if sigla_estado in estados:
                    sub = r.get_subreddit('brasil')
                    sub.set_flair(str(msg.author),flairstr,sigla_estado)
                    '''
            #msg.mark_as_read()
                
            
        '''
        if subj == 'crest':
            print msg
            auth = str(msg.author)
            body = str(msg.body)
            print "Author: " + auth
            print "Message content: " + body
            sub = r.get_subreddit('football')
            if body in teams:
                ftext = str(teams[body])
                sub.set_flair(auth, ftext, body)
                with open('log.txt', 'a') as logfile:
                    tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    lm = ' : ' + body + ' @ ' + tn
                    logfile.write('\n\rAdded: ' + auth + ' : ' + ftext + lm)
                print "Setting flair: " + auth + " : " + ftext + " : " + body
                msg.mark_as_read()
                '''

if __name__ == '__main__':
    main()