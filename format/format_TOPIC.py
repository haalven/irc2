

# display formatted messages

from copy import deepcopy
from source_parse import source_expand
from time_calc import pre
from match_format import links_fmt
from xterm_control import uline, color, reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    src    = deepcopy( msg['SRC']    )

    channel= deepcopy( msg['PAR'][0] )

    text   = deepcopy( msg['PAR'][1] )


    # formatted

    nick, addr, __, ___ = source_expand(src)

    text   = uline() + text + reset()

    text   = links_fmt(text, color(94), reset() + uline())


    # construct and print

    line   = [ date, nick, '('+addr+')', 'set', channel, 'topic:', text ]

    print( '\x20'.join(line) )

