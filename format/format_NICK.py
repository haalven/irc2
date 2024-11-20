

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import light, reset


def format(client,msg):

    if client.hide_traffic: return

    # format elements

    date    = pre( msg['DATE'] )

    old_nick= deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    new_nick= deepcopy( msg['PAR'][0] )

    account = deepcopy( msg['TAGS']['account']) if 'account' in msg['TAGS'] else ''


    # construct and print

    line   = [ date , old_nick, 'now known as:', new_nick, '('+addr+')' ]

    if account: line.append( 'a:'+account )

    line[1]  = light() + line[1]

    line[-1] += reset()

    print( '\x20'.join(line) )

