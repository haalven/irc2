

# handle user CTCP

from input import input_HELP
from message_echo import message_echo


def handle(client, kb_args):

    if len(kb_args) < 2:
        input_HELP.handle(client, ['CTCP']); return

    target       = kb_args[0]

    ctcp_args    = []
    for arg in kb_args[1:]:
        if arg.strip(): ctcp_args.append(arg.strip())

    ctcp_args[0] = ctcp_args[0].upper() # the CTCP verb

    ctcp_cmd     = '\x20'.join( ctcp_args )

    if (not target) or (not ctcp_cmd): return None

    trailing     = '\x01' + ctcp_cmd + '\x01' 

    emitter      = [ 'PRIVMSG' , target , ':' + trailing ]

    client.sock_send( emitter )

    message_echo(client, emitter)
