

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,reset


def format(client,msg):


    # format elements

    date    = pre( msg['DATE'] )

    newname = deepcopy( msg['PAR'][0] )


    # formatting

    verb    = 'Your realname changed to:'

    newname = color(34) + newname + reset()


    # construct and print

    line   = [ date , verb , newname ]

    print( '\x20'.join(line) )

