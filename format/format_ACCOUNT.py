

# display formatted messages

from is_active import is_active
from copy import deepcopy
from time_calc import pre
from xterm_control import light,reset


def format(client,msg):

    # if hide_traffic, only show active users account
    if client.hide_traffic:
        if not is_active(client, msg['NICK'], msg['DATE']):
            return None

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    account = deepcopy( msg['PAR'][0] )


    if msg['PAR'][0] == '*':

        verb    = 'is now'

        account = '-logged out-'

    else:

        verb    = 'is now logged in as:'


    # construct and print

    line   = [ date , nick , '('+addr+')' , verb , account ]

    line[1]  = light() + line[1]

    line[-1] += reset()

    print( '\x20'.join(line) )

