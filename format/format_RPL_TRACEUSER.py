

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    uclass = deepcopy( msg['PAR'][2] )

    nick   = deepcopy( msg['PAR'][3] )

    more   = '\x20'.join(deepcopy( msg['PAR'][4:] )) if len(msg['PAR'])>4 else ''


    # formatting

    verb   = '[TRACE]'

    ttype  = 'type=' + color(64) + 'User' + reset()

    uclass = 'class=' + color(64) + uclass + reset()

    nick   = 'nick=' + color(64) + nick + reset()


    # construct and print

    line = [ date , verb , ttype, uclass , nick , more ]

    print( '\x20'.join(line) )

