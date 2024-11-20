

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    key     = deepcopy( msg['KEY'] )


    match key:
        case 'RPL_NOWAWAY': verb = 'You have been marked as being away .'
        case 'RPL_UNAWAY':  verb = 'You are no longer marked as being away .'


    # construct and print

    line   = [ date , verb ]
    print( '\x20'.join(line) )

