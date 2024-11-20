

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    sclass = deepcopy( msg['PAR'][2] )

    more   = '\x20'.join(deepcopy( msg['PAR'][3:] ))


    # formatting

    verb   = '[TRACE]'

    ttype  = 'type=' + color(76) + 'Server' + reset()

    sclass = 'class=' + color(76) + sclass + reset()


    # construct and print

    line = [ date , verb , ttype, sclass , more ]

    print( '\x20'.join(line) )

