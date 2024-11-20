

# display formatted messages

from time_calc import pre
from xterm_control import uline,reset


def format(client,msg):

    # format elements

    date      = pre( msg['DATE'] )


    # construct and print

    line   = [ date , 'end of batch .' ]

    line[1] = uline() + line[1]

    line[-1] += reset()

    print( '\x20'.join(line) )

