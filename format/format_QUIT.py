

# display formatted messages

from copy import deepcopy
from is_netsplit import is_netsplit
from time_calc import pre
from xterm_control import light,color,reset


def format(client,msg):

    if client.hide_traffic: return

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    text    = deepcopy( msg['PAR'][0] ) if msg['PAR'] else ''


    # formatting

    symbol  = color(92) + chr(9666) + reset()

    text    = text.replace(chr(8203), '') # ZERO WIDTH SPACE

    verb    = 'left:' if text else 'left'

    # netsplit?

    text    = is_netsplit(text)


    # construct and print

    line     = [ date , symbol , nick , '('+addr+')' , verb , text ]

    line[2]  = light() + line[2]

    line[-1] += reset()

    print( '\x20'.join(line) )

