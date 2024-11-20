

# format RPL_NOWOFF (605) Unreal

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    date   = pre( msg['DATE'] )

    nick   = deepcopy( msg['PAR'][1] )


    # formatting

    verb   = '[WATCH]'

    nick   = color(92) + nick + reset()


    # construct and print

    line   = [ date , verb , nick , 'is offline' ]

    print( '\x20'.join(line) )

