

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    anick  = deepcopy( msg['PAR'][1] )

    amsg   = deepcopy( msg['PAR'][2] ) if len(msg['PAR'])>2 else ''


    # formatting

    anick  = color(32) + anick + reset()


    # construct and print

    line = [ date , anick , 'is away:' , amsg ]

    print( '\x20'.join(line) )

