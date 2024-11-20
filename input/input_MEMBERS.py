

# handle user MEMBERS

from input import input_HELP
from am_i_in import am_i_in


def handle(client, kb_args):

    chan = kb_args[0]

    if not chan: input_HELP.handle(client, ['MEMBERS']); return None

    if not am_i_in(client, chan): return


    client.member_save = kb_args[0]

    client.sock_send([ 'WHO' , kb_args[0] ])
