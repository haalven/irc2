

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import light, color, endcol, normal


def format(client, msg):

    if client.hide_traffic: return


    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    channel = deepcopy( msg['PAR'][0] )

    account = deepcopy( msg['TAGS']['account']) if 'account' in msg['TAGS'] else ''

    gecos   = ''


    # extended-join

    if len(msg['PAR']) == 3:

        account = deepcopy( msg['PAR'][1] )

        gecos   = deepcopy( msg['PAR'][2] )


    # formatting

    verb    = color(76) + chr(9656) + endcol()


    # member of blackset

    if msg['BLACK']:

        nick = chr(10071) + nick

        blmsg = color(196) + str(msg['BLACK']) + endcol()


    # construct and print

    line   = [ date , verb , nick , '('+addr+')' , 'joined:' , channel ]

    if account: line.append( 'a:'+account )

    if gecos: line.append( 'r:'+gecos )

    if msg['BLACK']: line.append( blmsg )

    line[2]  = light() + line[2]

    line[-1] += normal()

    print( '\x20'.join(line) )

