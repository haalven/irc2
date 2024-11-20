

# handle bot_SAY


def handle(client,msg,bot_arg):
    
    if msg['SRC'] in client.masters:

        target, _, text = bot_arg.partition('\x20')

        if target and text:

            client.sock_send( ['PRIVMSG', target, ':' + text] )

            client.sock_send( ['NOTICE', msg['NICK'], 'OK.'] )
