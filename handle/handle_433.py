

# handle 433 (ERR_NICKNAMEINUSE)


def handle(client,msg):

    if not client.registered:

        if not msg['PAR'][1].endswith('-'):

            client.sock_send(['NICK', msg['PAR'][1]+'-'])
