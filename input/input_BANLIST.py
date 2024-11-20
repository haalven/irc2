

# handle user BANLIST

from input import input_HELP
from is_channel import is_channel
from listmodes import listmodes


def handle(client, kb_args):

    chan = kb_args[0]

    if not chan: input_HELP.handle(client, ['BANLIST']); return None

    if not is_channel(client, chan): return


    lmodes = listmodes(client)

    for lmode in lmodes:

        if lmode in ['b','q']:
            client.sock_send([ 'MODE' , chan , lmode ])

