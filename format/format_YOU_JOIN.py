

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    channel = deepcopy( msg['PAR'][0] )

    addr    = deepcopy( msg['SRC']    )

    account = deepcopy( msg['TAGS']['account']) if 'account' in msg['TAGS'] else ''

    gecos   = ''


    # extended-join

    if len(msg['PAR']) == 3:

        account = deepcopy( msg['PAR'][1] )

        gecos   = deepcopy( msg['PAR'][2] )


    # formatting

    verb    = color(76) + chr(9654) + ' You joined:'

    channel = channel + reset()

    addr    = addr.replace('!', color(28) + '!' + reset())
    addr    = addr.replace('@', color(28) + '@' + reset())


    # construct and print

    line   = [ date , verb , channel , addr ]

    if account: line.append( 'a:'+account )

    if gecos: line.append( 'r:'+gecos )

    print( '\x20'.join(line) )

