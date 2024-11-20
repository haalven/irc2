

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    chan   = deepcopy( msg['PAR'][1] )


    verb   = 'You have been invited to:'


    # construct and print

    line = [ date , verb , chan  ]

    print( '\x20'.join(line) )

