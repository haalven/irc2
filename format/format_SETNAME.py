

# display formatted messages

from is_active import is_active
from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # if hide_traffic, only show active users setname
    if client.hide_traffic:
        if not is_active(client, msg['NICK'], msg['DATE']):
            return None

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    newname = deepcopy( msg['PAR'][0] )


    # formatting

    verb    = 'changed realname to:'


    # construct and print

    line   = [ date , nick, '('+addr+')', verb , newname ]

    print( '\x20'.join(line) )

