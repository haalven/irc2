

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client, msg):

    # format elements

    date    = pre( msg['DATE'] )

    server  = deepcopy( msg['NICK'] )

    cap_verb= deepcopy( msg['PAR'][1] ).upper()

    cap_str = deepcopy( msg['PAR'][3] ) if msg['PAR'][2]=='*' else deepcopy( msg['PAR'][2] )

    cap_str = cap_str.strip()

    cap_list= cap_str.split('\x20') if ('\x20' in cap_str) else [cap_str]


    capfmt = []

    for cap in cap_list:

        capkey, _, capval = cap.partition('=')

        if '/' in capkey:

            prefix, _, realcap = capkey.partition('/')

            capkey = light() + prefix + '/' + reset() + realcap

        if cap_verb == 'ACK':

            capkey = color(76) + chr(10004) + reset() + capkey

        capval = capval.replace(',', color(94)+','+color(138))

        capfmt.append( capkey + color(94) + '=' + color(138) + capval + reset() )


    verb    = color(58) + f'[CAP/{cap_verb}]' + reset()


    # construct and print

    line   = [ date , verb ,  '\x20'.join( capfmt ) ]

    print( '\x20'.join(line) )

