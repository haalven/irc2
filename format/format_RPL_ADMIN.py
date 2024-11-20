

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client, msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = '\x20'.join( deepcopy( msg['PAR'][1:] ) )

    verb   = '[ADMIN]'


    # construct and print

    line = [ date , verb , text ]

    print( '\x20'.join(line) )

