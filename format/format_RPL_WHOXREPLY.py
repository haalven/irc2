

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, reset


def format(client, msg):

    # format elements

    date = pre( msg['DATE'] )

    info = deepcopy( msg['PAR'][1:] ) if len( msg['PAR'] )>1 else []

    if not info: return None


    # formatted

    verb   = '[WHOX]'

    if info[0] == '999': # /WHOX reply

        try:
            channel  = color(32) + info[1] + reset()
            username = color(32) + info[2] + reset()
            ipaddr   = color(32) + info[3] + reset()
            hostname = color(32) + info[4] + reset()
            svrname  = color(32) + info[5] + reset()
            nickname = color(32) + info[6] + reset()
            whoflags = color(32) + info[7] + reset()
            hopcount = color(32) + info[8] + reset()
            idlesecs = color(32) + info[9] + reset()
            account  = color(32) + info[10] + reset()
            chanpriv = color(32) + info[11] + reset()
            realname = color(32) + info[12] + reset()

        except Exception:
            print(date , 'error: malformed WHOX reply .')
            return None

        # mark opers
        whoflags = whoflags.replace('*', color(88) + '*' + color(32))

        # output
        text =  f'{nickname}!{username}@{hostname} ip: {ipaddr} rn: {realname} '
        text += f'acc: {account} flags: {whoflags} svr: {svrname} idle: {idlesecs}'


    else: text   = '\x20'.join(info)


    # construct and print

    line   = [ date , verb , text ]

    print( '\x20'.join(line) )

