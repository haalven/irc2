

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import bold,color,reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    server   = deepcopy( msg['NICK']   )

    text     = deepcopy( msg['PAR'][1] )


    # formatting

    server   = bold() + '-'+server+'-' + reset()

    text     = color(110) + text  + reset()


    # construct and print

    line   = [ date , server , text ]

    print( '\x20'.join(line) )

