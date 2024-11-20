

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import light,color,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK'] )

    addr    = deepcopy( msg['ADDR'] )

    channel = deepcopy( msg['PAR'][0] )

    mode    = '\x20'.join( deepcopy(msg['PAR'][1:]) )


    # formatting

    if not nick: nick = deepcopy( client.myserv )

    verb    = 'sets mode:'

    channel = color(88) + channel

    mode    = color(124) + mode + reset()


    # construct and print

    if addr: line = [ date , nick , '('+addr+')' , verb , channel , mode ]

    else:    line = [ date , nick , verb , channel , mode ]

    line[1]  = light() + line[1]

    line[-3] += reset()

    print( '\x20'.join(line) )

