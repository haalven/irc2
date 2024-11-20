

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = deepcopy( msg['PAR'][1] )


    verb   = chr(9888)+chr(65039)+'\x20'


    # construct and print

    line   = [ date , verb , text ]

    print( '\x20'.join(line) )

