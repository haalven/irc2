

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import bold,reset


def format(client,msg):

    # elements

    date   = pre( msg['DATE'] )

    serv   = deepcopy( msg['PAR'][1] )

    info   = '\x20'.join( msg['PAR'][2:] )


    # formatting

    serv = bold() + serv + reset()


    # construct

    line = [ date , '[SERVICE]' , serv , info ]

    print( '\x20'.join(line) )

