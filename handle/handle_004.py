

# handle 004 (RPL_MYINFO)

from is_myserv import is_myserv
from ircd_family import ircd_family, ircd_urls
from time_calc import pre
from xterm_control import bold, color, reset


def handle(client, msg):

    # skip remote server info  (/version servername)

    if not is_myserv(client, msg['SRC']): return None


    # fix arguments

    if (len(msg['PAR']) > 5) and ('.' in msg['PAR'][3]):

        msg['PAR'][2] += msg['PAR'][3]; msg['PAR'].pop(3)


    # save usermodes

    if len(msg['PAR']) >= 4: client.usermodes = msg['PAR'][3] 


    # save ircd version string

    if len(msg['PAR']) >= 3: client.svr_version = msg['PAR'][2]

    # calc ircd family

    client.ircd_family = ircd_family(client.svr_version)

    if client.myserv == 'tmi.twitch.tv': client.ircd_family = 'twitch'


    # display ircd info

    if client.ircd_family:
        info = ['ircd:', bold() + str(client.ircd_family) + reset(),
                str(ircd_urls(client.ircd_family))]

    else: info = [color(196) + 'unknown ircd family .' + reset()]

    print(pre(msg['DATE']), '\x20'.join(info))
