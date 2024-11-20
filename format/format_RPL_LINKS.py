

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    serv1  = deepcopy( msg['PAR'][1] )
    serv2  = deepcopy( msg['PAR'][2] )
    trail  = deepcopy( msg['PAR'][3] )

    # parse

    hops,_,info = trail.partition('\x20')


    # formatting

    serv1 = color(32) + serv1 + reset()

    info  = color(32) + light() + info + reset()


    # construct and print

    line = [date, 'LINK', serv1, '<->', serv2, '('+hops+')', info]

    print( '\x20'.join(line) )

