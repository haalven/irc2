

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import bold, reset


def format(client, msg):

    # format elements

    date   = pre( msg['DATE'] )


    lang   = deepcopy( msg['PAR'][1] )

    text   = deepcopy( msg['PAR'][2] )


    # construct and print

    line = [date, text + ':', lang]

    print( '\x20'.join(line) )

