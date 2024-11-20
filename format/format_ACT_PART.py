

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK']   )

    addr    = deepcopy( msg['ADDR']   )

    channel = deepcopy( msg['PAR'][0] )

    partmsg = deepcopy( msg['PAR'][1]) if len(msg['PAR'])>1 else ''


    # formatting

    verb    = color(92) + chr(9666) + reset()

    partmsg    = partmsg.replace(chr(8203), '') # ZERO WIDTH SPACE


    # construct and print

    line   = [ date, verb, nick, '('+addr+')', 'parted', channel ]

    if partmsg: line.append('(' + partmsg + ')')

    line[3]  = light() + line[3]

    line[-1] += reset()

    print( '\x20'.join(line) )

