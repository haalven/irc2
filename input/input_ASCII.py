

# handle user ASCII

from input import input_HELP
from os.path import exists
from os import listdir
from time_calc import now
from text_lines import text_lines
from message_echo import message_echo
from time import sleep


def handle(client, kb_args):

    if len(kb_args) != 2:
        input_HELP.handle(client, ['ASCII']); return None

    target, asciifile = kb_args[0], kb_args[1]

    if (not target) or (not asciifile):
        input_HELP.handle(client, ['ASCII']); return None

    if not asciifile.lower().endswith('.txt'):
        asciifile = asciifile + '.txt'

    asciidir  = client.ircpath + '/ascii/'
    asciipath = asciidir + asciifile

    if not exists(asciipath):
        print(now(), '[ASCII]', 'no file at', asciipath)

        asciilist, namelist = listdir(asciidir), []
        for f in asciilist:
            if f.endswith('.txt'):
                namelist.append(f[:-4])

        print(now(), '[ASCII]', 'files available:', sorted(namelist))
        return None

    asciilines = text_lines(asciipath)

    if asciilines:
        timer = 1.5 # second per line (default)
        if client.isupport['NETWORK'].lower() == 'whale': timer = 0

        duration = len(asciilines) * timer
        if duration: print(now(), '[ASCII]', f'sending art to server ({duration} seconds) …')

        for line in asciilines:
            emitter = [ 'PRIVMSG' , target , ':' + line ]
            client.sock_send( emitter )
            message_echo(client, emitter)
            sleep(timer)
