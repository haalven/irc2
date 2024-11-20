

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    new_id  = deepcopy( msg['PAR'][0] )

    new_host= deepcopy( msg['PAR'][1] )


    verb    = 'Your address has changed:'

    new_addr= color(34) + new_id + '@' + new_host + reset()


    # construct and print

    line   = [ date , verb , new_addr ]

    print( '\x20'.join(line) )

