

# format RPL_ISON

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    date   = pre( msg['DATE'] )

    on     = deepcopy( msg['PAR'][1] ).strip()

    onlist = on.split('\x20') if '\x20' in on else [on]


    # formatting

    verb   = '[ISON]'


    # iter

    for nick in onlist:

        if not nick: continue

        nick   = color(34) + nick + reset()

        # construct and print

        line = [ date, verb, nick, 'is online' ]

        print( '\x20'.join(line) )

