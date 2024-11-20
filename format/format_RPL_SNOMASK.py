

# display formatted messages

from copy import deepcopy
from sno_list import sno_list
from time_calc import pre
from xterm_control import color, light, reset


def format(client, msg):

    # format elements

    date    = pre( msg['DATE'] )

    snomask = deepcopy( msg['PAR'][1] )

    # sno_list

    sn_list = sno_list(client, snomask) if client.ircd_family else []


    # formatting

    verb     = 'Your server notice masks:'

    snomask  = color(166) + snomask + light()

    mask_list  = str(sn_list) + reset()


    # construct and print

    line   = [ date , verb , snomask, mask_list ]

    print( '\x20'.join(line) )

