

# handle user LISTMODES

from input import input_HELP
from am_i_in import am_i_in
from listmodes import listmodes


def handle(client, kb_args):

    chan = kb_args[0]

    if not chan: input_HELP.handle(client, ['LISTMODES']); return None

    if not am_i_in(client, chan): return


    lmodes = listmodes(client)

    for lmode in lmodes:

        client.sock_send([ 'MODE' , chan , lmode ])

