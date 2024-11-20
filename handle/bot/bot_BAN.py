

# handle bot_BAN
# !ban #chat *!*@foobar


def handle(client,msg,bot_arg):
    
    if msg['SRC'] in client.masters:

        channel, _, mask = bot_arg.partition('\x20')


        client.sock_send( ['MODE', channel, '+b', mask] )

        client.sock_send( ['NOTICE', msg['NICK'], 'OK.'] )
