

# handle bot_DO


def handle(client,msg,bot_arg):
    
    if msg['SRC'] in client.masters:

        do_cmd, _, do_arg = bot_arg.partition('\x20')

        do_cmd = do_cmd.upper()

        do_arg = do_arg.replace('&me', client.mynick)


        client.sock_send( [do_cmd, do_arg] )

        client.sock_send( ['NOTICE', msg['NICK'], 'OK.'] )
