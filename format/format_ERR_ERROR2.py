

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    verb   = deepcopy( msg['VERB']   )  # numeric

    # no errkey

    errinfo= '\x20'.join( deepcopy( msg['PAR'][1:] ) )


    # formatting

    symbol = chr(9888)+chr(65039)+'\x20'


    # construct and print

    line   = [ date, symbol, 'Error', '('+verb+'):', errinfo ]

    print( '\x20'.join(line) )

