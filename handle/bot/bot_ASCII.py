

# handle bot_ASCII

from os.path import exists
from os import listdir
from text_lines import text_lines
from time import sleep
from time_calc import now


def handle(client, msg, bot_arg):
    
    if msg['SRC'] in client.masters:

        bot_args = bot_arg.split('\x20')

        if len(bot_args) != 2: return None

        target, asciifile = bot_args[0], bot_args[1]

        if (not target) or (not asciifile): return None

        if not asciifile.endswith('.txt'):
            asciifile = asciifile + '.txt'

        asciidir  = client.ircpath + '/ascii/'
        asciipath = asciidir + asciifile

        if not exists(asciipath):

            asciilist, namelist = listdir(asciidir), []
            for f in asciilist:
                if f.endswith('.txt'):
                    namelist.append(f[:-4])

            client.sock_send( ['NOTICE', msg['NICK'], ':[ASCII]',
                               'files available:', str(sorted(namelist))] )

            return None

        asciilines = text_lines(asciipath)

        if asciilines:
            client.sock_send( ['NOTICE', msg['NICK'], 'OK.'] )
            timer = 1.5 # second per line (default)
            if client.isupport['NETWORK'].lower() == 'whale': timer = 0

            duration = len(asciilines) * timer
            if duration: print(now(), '[ASCII]', f'sending art to server ({duration} seconds) …')

            for line in asciilines:
                client.sock_send([ 'PRIVMSG', target, ':' + line])
                sleep(timer)
