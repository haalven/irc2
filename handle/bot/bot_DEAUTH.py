

# handle bot_DEAUTH


def handle(client,msg,bot_arg):

    if msg['SRC'] in client.masters:

        master = bot_arg if bot_arg else msg['SRC']

        while master in client.masters:

            client.masters.remove(master)


        client.sock_send( ['NOTICE', msg['NICK'], 'OK.'] )
