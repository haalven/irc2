

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import light,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    map    = '\x20'.join( deepcopy( msg['PAR'][1:] ) )


    # formatting

    verb  = light() + 'MAP' + reset()


    # construct and print

    line = [ date, verb, map ]

    print( '\x20'.join(line) )

