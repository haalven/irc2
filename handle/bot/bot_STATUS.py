

# handle bot_STATUS


def handle(client,msg,bot_arg):

    if msg['SRC'] in client.masters:

        client.sock_send( ['NOTICE', msg['NICK'], ':'+str(client.masters)] )
