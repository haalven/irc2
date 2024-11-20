

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = deepcopy( msg['PAR'][1] )


    verb   = color(76) + chr(10004) + reset()


    # construct and print

    line   = [ date , verb , text ]

    print( '\x20'.join(line) )

