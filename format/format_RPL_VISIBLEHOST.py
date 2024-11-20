

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    host    = deepcopy( msg['PAR'][1] )


    verb    = 'Your visible host is now:'

    host    = color(34) + host + reset()


    # construct and print

    line   = [ date , verb , host ]

    print( '\x20'.join(line) )

