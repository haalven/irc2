

# display formatted messages

from copy import deepcopy
from cmode_list import cmode_list
from time_calc import pre
from xterm_control import color, endcol


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    channel = deepcopy( msg['PAR'][1] )

    mode    = '\x20'.join( deepcopy( msg['PAR'][2:] ) )


    cmodes, _, margs = mode.partition('\x20')


    # cmodes_list

    cmodes_list = cmode_list(client,cmodes) if client.ircd_family else []


    # formatting

    verb    = 'mode:'

    mode    = color(76) + mode

    cm_list = color(28) + str(cmodes_list) + endcol()


    # construct and print

    line   = [ date , channel , verb , mode , cm_list ]

    print( '\x20'.join(line) )

