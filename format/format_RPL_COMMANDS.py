

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import light, normal, color, endcol


def format(client, msg):

    # format elements

    date   = pre( msg['DATE'] )

    arg    = deepcopy( msg['PAR'][1] ) if (len(msg['PAR']) > 1) else ''


    if not arg: return None

    command, _, info = arg.partition('\x20')


    # formatting

    verb    = '[COMMAND]'

    command = color(45) + command + endcol()

    info    = light() + '('+ info +')' + normal()

    # construct and print

    line   = [ date , verb , command , info ]

    print( '\x20'.join(line) )

