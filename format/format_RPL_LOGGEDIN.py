

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    account = deepcopy( msg['PAR'][2] )


    verb    = 'You are now logged in as:'

    account = color(34) + account + reset()


    # construct and print

    line   = [ date , verb , account ]

    print( '\x20'.join(line) )

