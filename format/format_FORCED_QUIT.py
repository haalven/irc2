

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    text    = deepcopy( msg['PAR'][0] ) if msg['PAR'] else ''

    account = deepcopy( msg['TAGS']['account']) if 'account' in msg['TAGS'] else ''


    # formatting

    verb    = color(196) + chr(9666)

    nick    += reset()

    text    = color(196) + text + reset()


    # construct and print

    if account:

        line = [ date , verb , nick , '('+addr+')' , 'a:'+account , 'left:' , text ]

    else:

        line = [ date , verb , nick , '('+addr+')' , 'left:' , text ]


    line[3]  = light() + line[3]

    line[-1] += reset()

    print( '\x20'.join(line) )

