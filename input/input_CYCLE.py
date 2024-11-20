

# handle user CYCLE

from input import input_HELP
from am_i_in import am_i_in


def handle(client, kb_args):

    chan = kb_args[0]

    if not chan: input_HELP.handle(client, ['CYCLE']); return None

    if not am_i_in(client, chan): return


    if client.ircd_family in ['unreal','inspircd']:
        client.sock_send( [ 'CYCLE' , chan ] )

    else:
        client.sock_send( [ 'PART' , chan , ':cycling' ] )
        client.sock_send( [ 'JOIN' , chan ] )
