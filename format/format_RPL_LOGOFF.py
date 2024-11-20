

# format RPL_LOGOFF (601) Unreal

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    date   = pre( msg['DATE'] )

    nick   = deepcopy( msg['PAR'][1] )

 #  user   = deepcopy( msg['PAR'][2] )

 #  host   = deepcopy( msg['PAR'][3] )

 #  ts     = deepcopy( msg['PAR'][4] )


    # formatting

    verb   = '[WATCH]'

    nick   = color(92) + nick + reset()


    # construct and print

    line   = [ date , verb , nick , 'logged offline' ]

    print( '\x20'.join(line) )

