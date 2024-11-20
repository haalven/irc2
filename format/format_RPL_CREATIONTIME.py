

# display formatted messages

from copy import deepcopy
from time_calc import pre,ts2dt,dt2ymd,dt_now,td2str


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    channel= deepcopy( msg['PAR'][1] )

    ts     = deepcopy( msg['PAR'][2] )


    # formatted

    verb   = 'was created at:'

    dt = ts2dt( ts )

    topic_date = dt2ymd( dt )

    ago = dt_now() - dt



    # construct and print

    line   = [ date , channel , verb , topic_date ]

    line.append( '(' + td2str(ago) + ' ago)' )

    print( '\x20'.join(line) )

