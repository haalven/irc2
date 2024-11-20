

# display formatted messages

from copy import deepcopy
from umode_list import umode_list
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    mode    = '\x20'.join( deepcopy(msg['PAR'][1:]) )


    # umodes_list

    umodes_list = umode_list(client,mode) if client.ircd_family else []


    # formatting

    verb    = 'Your current user mode:'

    mode    = color(166) + mode + light()

    um_list = str(umodes_list) + reset()


    # construct and print

    line   = [ date , verb , mode , um_list ]

    print( '\x20'.join(line) )

