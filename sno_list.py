
# translate the snomask

from json import load


def sno_list(client, snomask):

    sno_file = client.ircpath + '/snomasks.json'

    with open(sno_file) as f: sno_dic = load(f)

    sno_list = []

    for m in snomask:

        try: txt = sno_dic[client.ircd_family][m]

        except Exception:

            txt = f'unknown ({m})'

        sno_list.append(txt)

    return sno_list
