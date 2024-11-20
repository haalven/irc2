

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import light,color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    addr    = deepcopy( msg['ADDR']   )

    new_nick= deepcopy( msg['PAR'][0] )

    account = deepcopy( msg['TAGS']['account']) if 'account' in msg['TAGS'] else ''


    # formatting

    verb    = 'You are now known as:'

    new_nick= color(166) + new_nick + reset()


    # construct and print

    line   = [ date , verb , new_nick , '('+addr+')' ]

    if account: line.append( 'a:'+account )

    line[3]  = light() + line[3]

    line[-1] += reset()

    print( '\x20'.join(line) )

