

# display formatted messages

from copy import deepcopy
from time_calc import pre
from source_parse import source_expand
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    kchan  = deepcopy( msg['PAR'][1] )

    kuser  = deepcopy( msg['PAR'][2] )


    # formatting

    if '!' in kuser:
        knick, kaddr, _, __ = source_expand(kuser)
    else:
        knick = kuser

    knocker = knick
    if kaddr: knocker += ' ('+kaddr+')'

    verb   = color(28) + '[KNOCK]' + reset()


    # construct and print

    line = [ date , verb , knocker , 'has asked for an invite to' , kchan , '.' ]

    print( '\x20'.join(line) )

