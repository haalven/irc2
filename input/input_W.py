

# handle user W(HOIS)


def handle(client, kb_args):

    if not kb_args[0]: return None

    client.sock_send([ 'WHOIS' , kb_args[0] , kb_args[0] ])
