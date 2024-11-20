

# handle user CAPS

from json import load
from is_cap import real_cap
from time_calc import now
from xterm_control import color, endcol, light, normal


def handle(client, kb_args):

    date = now()

    if client.active_caps:

        caps_file = client.ircpath + '/caps.json'

        with open(caps_file) as f: caps_dic = load(f)

        realcaps = []

        for acap in client.active_caps:

            realcaps.append(real_cap(acap))

        for cap in caps_dic['enabled']:

            cap_descr = caps_dic['enabled'][cap] if cap in caps_dic['enabled'] else 'unknown'

            if 'twitch.tv/' in cap_descr: continue

            if cap in realcaps:

                print( date , color(76) + chr(10004) , color(100) + cap + endcol() , '(' + cap_descr + ')' )

            else: # inactive

                print( date , chr(215) , light() + color(100) + cap + endcol() , '(' + cap_descr + ')' + normal())

    else:

        print( date , '[CAPS]' , 'there are no active capabilities .')
