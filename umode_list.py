
# translate the user modes

from json import load


def umode_list(client, umodes):

    umode_file = client.ircpath + '/umode.json'

    with open(umode_file) as f: mode_dic = load(f)

    mode_list = [] 

    for m in umodes:

        if m in ['+','-']: continue

        try: txt = mode_dic[client.ircd_family][m]

        except Exception:

            try: txt = mode_dic['*'][m]

            except Exception: txt = f'mode unknown ({m})'

        mode_list.append(txt)

    return mode_list
