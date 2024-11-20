

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    inviter= deepcopy( msg['NICK']   )

    inick  = deepcopy( msg['PAR'][0] )

    ichan  = deepcopy( msg['PAR'][1] )


    verb   = 'has invited'

    # construct and print

    line = [ date , inviter , verb , inick , 'to', ichan , '.' ]

    print( '\x20'.join(line) )

