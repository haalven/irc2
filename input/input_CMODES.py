

# handle user CMODES

from time_calc import now
from cmode_list import cmode_list
from cmode_type import cmode_type
from xterm_control import color, endcol


def handle(client, kb_args):

    date = now()

    # unknown ircd?
    if not client.ircd_family:
        print( date , 'Error:', 'ircd family unknown .' )
        return None


    # list all advertised modes

    if not kb_args[0]:
        if not ('CHANMODES' in client.isupport):
            print( date , 'Error:', 'channel modes not advertised .' )
            return None

        chanmodes = client.isupport['CHANMODES']

        mode_list = chanmodes.split(',')

        for mode_type in mode_list:

            for m in mode_type:

                if not m.isalpha(): continue

                print( date , '+' + color(76) + m + endcol() ,
                        '-', 'channel', cmode_list(client, m)[0])


        # hint to helpop

        if client.ircd_family in ['hybrid', 'plexus', 'oftc', 'ratbox',
                                  'charybdis', 'solanum', 'ergo']:
            print( date , 'see also:', '/HELP CMODE')

        elif client.ircd_family in ['inspircd', 'unreal']:
            print( date , 'see also:', '/HELP CHMODES')


    # display modes in arg

    else:

        if len(kb_args) > 1: # params
            par_list = kb_args[1:]
        else: par_list = []

        for m in kb_args[0]:
            if not m.isalpha(): continue

            mtype = cmode_type(client, m)
            if not mtype: p = '' 
            else: p = par_list.pop(0) if ((mtype in 'BC') and par_list) else ''

            info = [ date,
                    '+' + color(76) + m + endcol(),
                    '-', 'channel',
                    cmode_list(client, m)[0] ]

            if p: info.append( '-> ' + color(76) + p + endcol() )

            print( '\x20'.join(info) )
