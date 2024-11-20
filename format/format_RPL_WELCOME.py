

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import invers,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = deepcopy( msg['PAR'][1] )


    # invert

    text = invers() + text + reset()


    # construct and print

    line   = [ date , text ]

    print( '\x20'.join(line) )

