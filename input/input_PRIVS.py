

# handle user PRIVS

from time_calc import now
from chan_privs import priv_modes


def handle(client, kb_args):

    privs = []
    for c in priv_modes(client):
        match c:
            case 'Y': privs.append('+Y (!oper)')
            case 'q': privs.append('+q (~owner)')
            case 'a': privs.append('+a (&admin)')
            case 'o': privs.append('+o (@op)')
            case 'h': privs.append('+h (%halfop)')
            case 'v': privs.append('+v (+voice)')

    info = [ now() , '[PRIVS]' , str(privs) ]
    print( '\x20'.join(info) )

