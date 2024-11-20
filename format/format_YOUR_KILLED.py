

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    killer_nick = deepcopy( msg['NICK'] )

    killer_addr = deepcopy( msg['ADDR'] )

    reason  = deepcopy( msg['PAR'][1] ) if len(msg['PAR'])>1 else ''


    # formatting

    verb    = color(196) + chr(9664) + ' You have been killed' + reset()

    reason  = color(196) + reason + reset()


    # construct and print

    line   = [date, verb, 'by:', killer_nick, '('+killer_addr+')', '"'+reason+'"']

    print( '\x20'.join(line) )

