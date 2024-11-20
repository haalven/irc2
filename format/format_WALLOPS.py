

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,uline,reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    src      = deepcopy( msg['SRC']    )

    text     = deepcopy( msg['PAR'][0] )


    # formatting

    verb     = color(201) + '[WALLOPS]' + reset()

    text     = uline() + text  + reset()


    # construct and print

    line   = [ date , verb , text , '('+src+')' ]

    print( '\x20'.join(line) )

