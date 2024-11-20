

# handle bot_CYCLE


def handle(client,msg,bot_arg):

    if msg['SRC'] in client.masters:

        if not bot_arg: return None

        chan, _, __ = bot_arg.partition('\x20')

        if client.ircd_family in ['unreal','inspircd']:
            client.sock_send( [ 'CYCLE' , chan ] )
    
        else:
            client.sock_send( [ 'PART' , chan , ':cycling' ] )
            client.sock_send( [ 'JOIN' , chan ] )

