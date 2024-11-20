
# translate the channel modes

from json import load


def cmode_list(client, cmodes):

    cmode_file = client.ircpath + '/cmode.json'

    with open(cmode_file) as f: mode_dic = load(f)


    mode_list = [] 

    for m in cmodes:

        if m in ['+', '-']: continue

        try: txt = mode_dic[client.ircd_family][m]

        except Exception:

            try: txt = mode_dic['*'][m]

            except Exception: txt = f'mode unknown ({m})'

        mode_list.append(txt)

    return mode_list
