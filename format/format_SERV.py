

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import bold,color,reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    serv     = deepcopy( msg['NICK']   )

    text     = deepcopy( msg['PAR'][1] )


    # formatting

    serv     = bold() + '-'+serv+'-' + reset()


    # nickserv collision
    if text.startswith('This nickname is registered') \
        or text.startswith('This nick is owned by someone else'):
        text = color(196) + text + reset()


    # construct and print

    line   = [ date , serv , text ]

    print( '\x20'.join(line) )

