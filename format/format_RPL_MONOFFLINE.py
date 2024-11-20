

# format RPL_MONOFFLINE

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):


    off    = deepcopy( msg['PAR'][1] )


    offlist= off.split(',') if ',' in off else [off]


    # formatting

    verb   = '[MONITOR]'


    # iter

    for nick in offlist:

        nick   = color(92) + nick + reset()

        # construct and print

        line   = [ pre( msg['DATE'] ) , verb , nick , 'is offline' ]

        print( '\x20'.join(line) )

