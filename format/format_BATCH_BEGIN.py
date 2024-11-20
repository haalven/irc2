

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import uline,reset


def format(client,msg):

    # format elements

    date      = pre( msg['DATE'] )

    batchtype = deepcopy( msg['PAR'][1] )

    batchargs = '\x20'.join(deepcopy(msg['PAR'][2:])) if len(msg['PAR'])>2 else ''


    # construct and print

    if batchargs:

        line   = [ date , 'begin of batch:' , batchtype , batchargs ]

    else:

        line   = [ date , 'begin of batch:' , batchtype ]


    line[1] = uline() + line[1]

    line[-1] += reset()

    print( '\x20'.join(line) )

