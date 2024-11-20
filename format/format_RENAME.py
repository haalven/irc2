

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, reset


def format(client, msg):


    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    channel = deepcopy( msg['PAR'][0] )

    newname = deepcopy( msg['PAR'][1] )

    reason  = deepcopy( msg['PAR'][2] ) if len(msg['PAR']) > 2 else ''


    # formatting

    verb = color(76) + chr(9654) + reset()

    newname = color(76) + newname + reset()


    # construct and print

    line = [ date, verb, channel, 'has been renamed to:', newname, 'by', nick ]

    if reason: line.append('('+reason+')')

    print( '\x20'.join(line) )

