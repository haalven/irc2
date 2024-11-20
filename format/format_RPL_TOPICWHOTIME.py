

# display formatted messages

from copy import deepcopy
from source_parse import source_expand
from time_calc import pre,ts2dt,dt2ymd,dt_now,td2str


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    channel= deepcopy( msg['PAR'][1] )

    user   = deepcopy( msg['PAR'][2] )

    ts     = deepcopy( msg['PAR'][3] )


    # formatted

    verb   = 'topic by:'

    nick,addr,__,___ = source_expand(user)

    dt = ts2dt( ts )

    topic_date = dt2ymd( dt )

    ago = dt_now() - dt


    # construct and print

    if addr: line = [ date, channel, verb, nick, '('+addr+')', 'at:', topic_date ]

    else:    line = [ date, channel, verb, nick, 'at:', topic_date ]

    line.append( '(' + td2str(ago) + ' ago)' )

    print( '\x20'.join(line) )

