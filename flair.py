# coding=utf-8
import praw
import sqlite3
import time
import datetime

con = sqlite3.connect('estados_municipios.db')
cursor = con.cursor()

USER = ''
PASSWORD = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
USER_AGENT = ''

def dbLookup(msg):
    if len(msg.split(',')) != 2:
        # procura na lista de paises
        query = 'SELECT id FROM paises WHERE nome == ?;'
        cursor.execute(query, (msg,))
        if cursor.fetchone():
            return True
        else:
            return False
    else:
        cidade = msg.split(',')[0].strip()
        estado = msg.split(',')[1].strip()
        # check cidade pertence ao estado
        query = 'SELECT estados.id FROM municipios JOIN estados ON municipios.estados_id == estados.id WHERE municipios.nome == ? AND estados.uf == ?;'
        cursor.execute(query, (cidade, estado))
        if not cursor.fetchone():
            return False

    return True

def write_log(text):
    print(text)
    log = open('log_flairbot.txt', 'a')
    log.write('{} {}\n'.format(str(datetime.datetime.now()),text))
    log.close()


def main():
    r = praw.Reddit(client_id = CLIENT_ID,
                    client_secret = CLIENT_SECRET,
                    user_agent = USER_AGENT,
                    username = USER,
                    password = PASSWORD)

    print(r.user.me()) #forca exception se login falhou
    print('logged in')

    while True:
        time.sleep(0.5)
        try:
            for msg in r.inbox.unread():
                try:
                    write_log('AUTHOR: {} - SUBJECT: {} - BODY: {}'.format(msg.author, msg.subject, msg.body))
                except UnicodeEncodeError:
                    write_log('AUTHOR: {} - unprintable chars'.format(msg.author))
                sub = r.subreddit('brasil')
                if msg.subject and msg.subject.lower() == 'flair':
                    if dbLookup(msg.body):
                        estado = 'world' if len(
                            msg.body.split(',')) < 2 else msg.body.split(',')[1].strip()
                        sub.flair.set(msg.author, msg.body, estado)
                        msg.author.message('flair', 'Flair configurado.')
                        write_log('flair ok')
                    else:
                        msg.author.message('flair', 'Configuração de flair falhou.')
                        write_log('flair fail')
                if msg.subject and msg.subject.lower() == 'remover flair':
                    sub.flair.delete(msg.author)
                    msg.author.message('flair', 'Flair removido.')
                    write_log('remove flair ok')
                r.inbox.mark_read([msg])
        except Exception as e:
            print(e)
            pass

if __name__ == '__main__':
    main()
