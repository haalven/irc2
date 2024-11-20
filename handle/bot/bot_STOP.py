

# handle bot_STOP


def handle(client,msg,bot_arg):

    if msg['SRC'] in client.masters:

        client.remotebot = False

        client.sock_send( ['NOTICE', msg['NICK'], 'OK.'] )
