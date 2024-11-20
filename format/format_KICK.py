

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    kicker_nick = deepcopy( msg['NICK'] )

    channel = deepcopy( msg['PAR'][0] )

    kicked  = deepcopy( msg['PAR'][1] )

    reason  = deepcopy( msg['PAR'][2] ) if len(msg['PAR'])>2 else ''


    # formatting

    symbol  = color(196) + chr(9666)

    kicked  += reset()

    verb    = 'has been kicked from'

    reason  = color(196) + reason + reset()

    # construct and print

    line   = [date, symbol, kicked, verb, channel, 'by:', kicker_nick, '"'+reason+'"']

    line[3]  = light() + line[3]

    line[-2] += reset()

    print( '\x20'.join(line) )

