

# display formatted messages

from copy import deepcopy
from time_calc import pre
from is_mynick import is_mynick
from xterm_control import light, color, reset


def format(client, msg):

    # format elements

    date   = pre( msg['DATE'] )

    target = deepcopy( msg['PAR'][0] )

    text   = deepcopy( msg['PAR'][1] )



    # target

    if is_mynick(client, msg['PAR'][0]):

        target = color(136) + '[private]' + reset()  # private msg

    else:

        target = light() + '['+ target +']' + reset()  # other msg



    # nick format

    nick = light() + '-History-' + reset()



    # link format

    text = light() + text + reset()



    # construct and print

    line   = [ date , target , nick , text ]

    print( '\x20'.join(line) )

