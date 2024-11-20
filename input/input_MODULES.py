

# handle user MODULE(S)

from copy import deepcopy


def handle(client, arg):

    kb_cmd, kb_args = arg[0], arg[1]

    cmd = deepcopy(kb_cmd)

    match client.ircd_family:
        case 'inspircd': cmd = 'MODULES'
        case 'unreal':   cmd = 'MODULE'

    client.sock_send( [ cmd , '\x20'.join(kb_args) ] )

