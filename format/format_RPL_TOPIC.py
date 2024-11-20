

# display formatted messages

from copy import deepcopy
from time_calc import pre
from match_format import links_fmt
from xterm_control import uline, color, reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    channel= deepcopy( msg['PAR'][1] )

    text   = deepcopy( msg['PAR'][2] )


    # formatted

    verb   = 'topic is:'

    text   = uline() + text + reset()

    text   = links_fmt(text, color(94), reset() + uline())


    # construct and print

    line   = [ date , channel , verb , text ]

    print( '\x20'.join(line) )

