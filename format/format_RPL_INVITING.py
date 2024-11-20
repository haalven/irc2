

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    inick  = deepcopy( msg['PAR'][1] )

    ichan  = deepcopy( msg['PAR'][2] )


    verb   = 'has been invited to'

    # construct and print

    line = [ date , 'OK :' , inick , verb , ichan , '.' ]

    print( '\x20'.join(line) )

