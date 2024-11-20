

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,uline,light,reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    src      = deepcopy( msg['SRC']    )

    target   = deepcopy( msg['PAR'][0] )

    text     = deepcopy( msg['PAR'][1] )


    # formatting

    verb     = color(201) + '[GLOBAL] ' + light() + target + reset()

    text     = uline() + text  + reset()


    # construct and print

    line   = [ date , verb , text , '('+src+')' ]

    print( '\x20'.join(line) )

