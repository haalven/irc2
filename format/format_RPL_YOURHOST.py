

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = '\x20'.join( deepcopy( msg['PAR'][1:] ) )


    verb   = color(58) + chr(9654) + reset()


    # construct and print

    line   = [ date , verb , text ]

    print( '\x20'.join(line) )

