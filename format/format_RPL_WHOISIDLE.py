

# display formatted messages

from copy import deepcopy
from time_calc import pre,ts2dt,dt2ymd,sec2td,td2str
from xterm_control import color,reset


def format(client,msg):

    # elements

    date   = pre( msg['DATE'] )
    whois  = deepcopy( msg['PAR'][1] )
    idlesec= deepcopy( msg['PAR'][2] )
    signon = deepcopy( msg['PAR'][3] )
    trail  = deepcopy( msg['PAR'][4] )


    # calculating

    signondt = ts2dt( signon )

    signonstr= dt2ymd( signondt )

    signontd = msg['DATE'] - signondt

    onlinefor= td2str( signontd )

    idledelta= sec2td( idlesec )

    idlestr  = td2str( idledelta )


    # formatting

    whois  = color(32) + whois + reset()


    # construct and print

    line = [ date , whois , 'signon time:' , signonstr ]
    print( '\x20'.join(line) )

    line = [ date , whois , 'connected for:' , onlinefor ]
    print( '\x20'.join(line) )

    line = [ date , whois , 'idle time:' , idlestr ]
    print( '\x20'.join(line) )
