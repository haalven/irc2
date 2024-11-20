

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    channel = deepcopy( msg['PAR'][0] )

    partmsg = deepcopy( msg['PAR'][1]) if len(msg['PAR'])>1 else ''


    # formatting

    verb    = color(92) + chr(9664) + ' You parted:'

    channel = channel + reset()

    partmsg    = partmsg.replace(chr(8203), '') # ZERO WIDTH SPACE


    # construct and print

    line   = [ date , verb , channel ]

    if partmsg: line.append('(' + partmsg + ')')

    print( '\x20'.join(line) )

