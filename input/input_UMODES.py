
# handle user UMODES

from time_calc import now
from umode_list import umode_list
from xterm_control import color, reset


def handle(client, kb_args):

    date = now()

    # unknown ircd?
    if not client.ircd_family:
        print( date , 'Error:', 'ircd family unknown .' )
        return None


    # list all advertised modes

    if not kb_args[0]:
        if not client.usermodes:
            print( date , 'Error:', 'user modes unknown .' )
            return None

        for m in client.usermodes:

            if not m.isalpha(): continue

            print( date , '+' + color(166) + m + reset() ,
                    '-', 'user', umode_list(client, m)[0])


        # hint to helpop

        if client.ircd_family in ['hybrid', 'plexus', 'oftc', 'ratbox',
                                  'charybdis', 'solanum', 'ergo']:
            print( date , 'see also:', '/HELP UMODE')

        elif client.ircd_family in ['inspircd', 'unreal']:
            print( date , 'see also:', '/HELP UMODES')



    # display modes in arg

    else:
        for m in kb_args[0]:
            if not m.isalpha(): continue

            print( date , '+' + color(166) + m + reset() ,
                    '-', 'user', umode_list(client, m)[0])

