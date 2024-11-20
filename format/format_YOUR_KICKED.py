

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    kicker_nick = deepcopy( msg['NICK'] )

    kicker_addr = deepcopy( msg['ADDR'] )

    channel = deepcopy( msg['PAR'][0] )

    reason  = deepcopy( msg['PAR'][2] ) if len(msg['PAR'])>2 else ''


    # formatting

    verb    = color(196) + chr(9664) + ' You have been kicked from'

    channel = channel + reset()

    reason  = color(196) + reason + reset()

    # construct and print

    line   = [date, verb, channel, 'by:', kicker_nick, '('+kicker_addr+')', '"'+reason+'"']

    print( '\x20'.join(line) )

