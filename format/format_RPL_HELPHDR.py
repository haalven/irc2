

# display RPL_HELPHDR (Unreal)

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = deepcopy( msg['PAR'][1] )


    # construct and print

    line   = [ date , '|' , text ]

    print( '\x20'.join(line) )

