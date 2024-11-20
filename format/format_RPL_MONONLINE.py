

# format RPL_MONONLINE

from copy import deepcopy
from time_calc import pre
from source_parse import source_expand
from xterm_control import color,reset


def format(client,msg):

    date   = pre( msg['DATE'] )

    on     = deepcopy( msg['PAR'][1] )

    onlist = on.split(',') if ',' in on else [on]


    # formatting

    verb   = '[MONITOR]'


    # iter

    for src in onlist:

        nick, addr, __, ___ = source_expand(src)

        nick   = color(34) + nick + reset()


        # construct and print

        if addr:

            line = [ date, verb, nick, '('+addr+')', 'is online' ]

        else:

            line = [ date, verb, nick, 'is online' ]

        print( '\x20'.join(line) )

