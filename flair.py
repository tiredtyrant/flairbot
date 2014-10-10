# coding=utf-8
import praw
import sqlite3

con = sqlite3.connect('estados_municipios.db')
cursor = con.cursor()

def dbLookup(msg):
    if len(msg.split(',')) != 2:
        return False
    cidade = msg.split(',')[0].strip()
    estado = msg.split(',')[1].strip()
    #check estado
    query = 'SELECT id FROM estados WHERE uf == \'%s\';' % (estado)
    cursor.execute(query)
    if not cursor.fetchone():
        return False
    #check cidade
    query = 'SELECT municipios.id FROM municipios WHERE nome = \'%s\''% (cidade)
    cursor.execute(query)
    if not cursor.fetchone():
        return False
    #check cidade pertence ao estado
    query = 'SELECT estados.id FROM municipios JOIN estados ON municipios.estados_id == estados.id WHERE municipios.nome == "%s" AND estados.uf == "%s";' % (cidade, estado)
    cursor.execute(query)
    if not cursor.fetchone():
        return False
        
    return True
    

def main():
    r = praw.Reddit(user_agent='flairbotbr')
    r.login('botbr', '***REMOVED***')
    while True:
        for msg in r.get_unread(limit=None):
            print msg.subject
            print msg.author
            print msg.body
            sub = r.get_subreddit('brasil')
            if msg.subject == 'flair' and dbLookup(msg.body):
                flairstr = msg.body
                estado = msg.body.split(',')[1].strip()
                sub.set_flair(msg.author,flairstr,estado)
            elif msg.subject == 'remover flair':
                sub.set_flair(msg.author,'','')
            else:
                pass
            msg.mark_as_read()
            #r.send_message(msg.author,'flair','hello!')
            '''
            if len(flairstr.split(',')) == 2:
                sigla_estado = flairstr.split(',')[1].strip()
                if sigla_estado in estados:
                    sub = r.get_subreddit('brasil')
                    sub.set_flair(str(msg.author),flairstr,sigla_estado)
                    '''
                
            
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