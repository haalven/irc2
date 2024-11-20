

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    whois  = deepcopy( msg['PAR'][1] )

    account= deepcopy( msg['PAR'][2] )


    # formatting

    whois  = color(32) + whois + reset()


    # construct and print

    line = [ date , whois , 'logged in as:' , account ]

    print( '\x20'.join(line) )
