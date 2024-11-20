

# display formatted messages

from copy import deepcopy
from time_calc import pre,ts2dt,dt2ymd
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    par    = deepcopy( msg['PAR'] )


    # quiet-list: remove 'b'

    if msg['KEY'] == 'RPL_QUIETLIST': par.pop(2)


    # parse

    match msg['KEY']:
        case 'RPL_BANLIST':     ltype = '+b '
        case 'RPL_EXCEPTLIST':  ltype = '+e '
        case 'RPL_INVEXLIST':   ltype = '+I '
        case 'RPL_QUIETLIST':   ltype = '+q '
        case 'RPL_REOPLIST':    ltype = '+R '

    channel, mask, by, ts = par[1], par[2], '', ''

    if len(par) == 5:  by, ts = par[3], par[4]

    if ts: ts = dt2ymd( ts2dt(ts) )


    # formatting
    for c in '*?':
        mask  = mask.replace(c, color(23) + c + color(32))

    mask  = color(30) + ltype + color(32) + mask + reset()


    # construct and print

    if len(par) < 5:  line = [date, channel, mask]

    else:

        line = [date, channel, mask, 'by:', by, '('+ts+')']

        line[3]   = light() + line[3]

        line[-1] += reset()


    print( '\x20'.join(line) )

