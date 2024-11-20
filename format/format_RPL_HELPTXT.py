

# display RPL_HELPTLR (Unreal)

from copy import deepcopy
from time_calc import pre
from xterm_control import light,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    text   = deepcopy( msg['PAR'][2] )


    # formatting

    text = light() + text + reset()


    # construct and print

    line   = [ date , '|' , text ]

    print( '\x20'.join(line) )

