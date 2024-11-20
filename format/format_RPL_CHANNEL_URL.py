

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    channel = deepcopy( msg['PAR'][1] )

    url     = deepcopy( msg['PAR'][2] )


    # formatting

    verb    = 'homepage is:'

    url     = color(94) + url + reset()


    # construct and print

    line   = [ date , channel , verb , url ]

    print( '\x20'.join(line) )

