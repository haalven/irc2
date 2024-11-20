

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    mask   = deepcopy( msg['PAR'][0] )

    more   = '\x20'.join( deepcopy( msg['PAR'][1:] ) ) if len(msg['PAR'])>1 else ''


    # formatting

    verb = '[SILENCE]'

    mask = color(92) + mask + reset()


    # construct and print

    line   = [ date , verb , mask , more ]

    print( '\x20'.join(line) )

