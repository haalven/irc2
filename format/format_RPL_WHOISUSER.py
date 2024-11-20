

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    par    = deepcopy( msg['PAR'][1:] )

    nick, ident, host, _, gecos = par


    # formatting

    whois  = color(32) + nick + reset()

    addr   = color(33) + ident + reset()

    addr  += '@' + color(33) + host + reset()


    # construct and print

    line = [ date , whois , addr, gecos ]

    print( '\x20'.join(line) )

