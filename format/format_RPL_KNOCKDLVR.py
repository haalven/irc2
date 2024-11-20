

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    kchan  = deepcopy( msg['PAR'][1] )

    # format

    text   = f'OK : your knock has been delivered to {kchan} ops .'

    # construct and print

    line = [ date , text ]

    print( '\x20'.join(line) )

