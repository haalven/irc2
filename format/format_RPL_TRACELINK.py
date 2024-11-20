

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    more   = '\x20'.join(deepcopy( msg['PAR'][2:] ))


    # formatting

    verb   = '[TRACE]'

    ttype  = 'type=' + color(76) + 'Link' + reset()


    # construct and print

    line = [ date , verb , ttype, more ]

    print( '\x20'.join(line) )

