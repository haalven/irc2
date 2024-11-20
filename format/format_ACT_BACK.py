

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )


    # formatting

    verb    = color(76) + '+' + reset()


    # construct and print

    line   = [ date, verb, nick, '('+addr+')', 'is back' ]

    line[3]  = light() + line[3]

    line[-1] += reset()

    print( '\x20'.join(line) )

