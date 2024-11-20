

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )


    isupport = []

    for tok in deepcopy ( msg['PAR'][1:-1] ):

        key, _, value = tok.partition('=')

        value = value.replace(',', color(94)+','+color(138))

        isupport.append( key + color(94) + '=' + color(138) + value + reset() )


    verb    = '[' + msg['KEY'].replace('RPL_','') + ']'

    verb    = color(58) + verb + reset()


    # construct and print

    line   = [ date , verb , '\x20'.join( isupport ) , 'are supported by this server' ]

    print( '\x20'.join(line) )

