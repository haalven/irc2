

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    awaymsg = deepcopy( msg['PAR'][0] )


    # formatting

    verb    = color(92) + chr(215) + reset()


    # construct and print

    line   = [ date, verb, nick, '('+addr+')', 'is gone:', awaymsg ]

    line[3]  = light() + line[3]

    line[-1] += reset()

    print( '\x20'.join(line) )

