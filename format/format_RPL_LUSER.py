

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,bold,uline,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    serv   = deepcopy( msg['NICK'] )

    info   = '\x20'.join( deepcopy( msg['PAR'][1:] ) )

    match msg['KEY']:

        case 'RPL_LOCALUSERS':
            current = info.split('\x20')[0]
            maxuser = info.split('\x20')[1]
            try:
                _ = int(current)
                info = f'Current local users: {current}  Max: {maxuser}'
            except Exception: pass

        case 'RPL_GLOBALUSERS':
            current = info.split('\x20')[0]
            maxuser = info.split('\x20')[1]
            try:
                _ = int(current)
                info = f'Current global users: {current}  Max: {maxuser}'
            except Exception: pass


    # formatting

    serv   = color(58) + serv + reset()

    info   = '- ' + info


    # construct and print

    line   = [ date , serv , info ]

    print( '\x20'.join(line) )

