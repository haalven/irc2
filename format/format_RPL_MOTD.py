

# display formatted messages

from copy import deepcopy
from time_calc import pre
from match_format import links_fmt
from xterm_control import light, color, reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = deepcopy( msg['PAR'][1] )


    # links

    text = links_fmt(text, color(94), reset() + light())

    # light

    text = light() + text + reset()


    # construct and print

    line   = [ date , '|' , text ]

    print( '\x20'.join(line) )

