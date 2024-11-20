

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    clear_chan = deepcopy( msg['PAR'][0] )

    try:
        clear_nick = deepcopy( msg['PAR'][1] )
    except Exception:
        clear_nick = 'all messages'

    try:
        duration = deepcopy( msg['TAGS']['ban-duration'] )
    except Exception:
        duration = ''

    banmsg = f'banned: {duration} sec' if duration else '' 


    # construct and print

    line   = [ date , '[CLEAR]' , clear_chan , '->', clear_nick , banmsg ]

    print( '\x20'.join(line) )

