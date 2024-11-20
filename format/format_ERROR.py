

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    err_text = '\x20'.join( deepcopy( msg['PAR'] ) )


    # formatting

    verb = color(196) + 'ERROR:' + reset()


    # construct and print

    line   = [ date , verb , err_text ]

    print( '\x20'.join(line) )

