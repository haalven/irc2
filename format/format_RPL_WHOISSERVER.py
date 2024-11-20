

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )
    whois  = deepcopy( msg['PAR'][1] )
    serv   = deepcopy( msg['PAR'][2] )
    trail  = deepcopy( msg['PAR'][3] ) if len(msg['PAR'])>3 else ''


    # formatting

    whois  = color(32) + whois + reset()


    # construct and print

    line = [ date , whois , 'connected to:' , serv , '('+trail+')' ]

    print( '\x20'.join(line) )

