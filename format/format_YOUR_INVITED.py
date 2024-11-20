

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    inviter= deepcopy( msg['NICK']   )

    addr   = deepcopy( msg['ADDR']   )

    ichan  = deepcopy( msg['PAR'][1] )


    # formatting

    verb   = color(28) + '[INVITE]' + reset()


    # construct and print

    line = [ date, verb, 'you have been invited to', ichan, 'by', inviter]

    if addr: line.append( '(' + addr + ')' )

    line.append('.')

    print( '\x20'.join(line) )

