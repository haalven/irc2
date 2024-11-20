

# handle 005 (RPL_ISUPPORT)

from is_myserv import is_myserv
from networks import net_urls
from text_lines import text_lines
from os.path import exists
from casemapping import set_casemap
from time_calc import pre
from xterm_control import bold, color, reset


def handle(client,msg):

    # remote info
    if not is_myserv(client, msg['SRC']): return None


    # add dict to client.isupport

    net, cm = False, False

    for tok in msg['PAR'][1:-1]:

        key, _, value = tok.partition('=')

        client.isupport[key] = value

        match key:
            case 'NETWORK':     net = True
            case 'CASEMAPPING': cm  = True


    # display network info

    if net:

        if client.isupport['NETWORK']:

            info = ['network:', bold() + str(client.isupport['NETWORK']) + reset(),
                str(net_urls(client.isupport['NETWORK']))]

            print(pre(msg['DATE']), '\x20'.join(info))

            # check badnets
            bad = False
            badfile = client.ircpath + '/badnets.txt'
            if exists(badfile):
                if client.isupport['NETWORK'].lower() in text_lines(badfile):
                    bad = True

            if bad: print(pre(msg['DATE']),
                          color(196) + '*** this network is blacklisted ***' + reset())


    # casemapping

    if cm: set_casemap(client)

