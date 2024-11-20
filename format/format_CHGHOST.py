

# display formatted messages

from is_active import is_active
from copy import deepcopy
from time_calc import pre
from xterm_control import light, reset


def format(client,msg):

    # if hide_traffic, only show active users chghost
    if client.hide_traffic:
        if not is_active(client, msg['NICK'], msg['DATE']):
            return None

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    old_addr= deepcopy( msg['ADDR']   )

    new_id  = deepcopy( msg['PAR'][0] )

    new_host= deepcopy( msg['PAR'][1] )


    verb    = 'changed hostname:'

    new_addr= new_id + '@' + new_host


    # construct and print

    line   = [ date , nick , verb , old_addr , '->' , new_addr ]

    line[1]  = light() + line[1]

    line[-1] += reset()

    print( '\x20'.join(line) )

