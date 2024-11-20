

# handle bot_PARTALL


def handle(client,msg,bot_arg):

    if msg['SRC'] in client.masters:


        chans = ','.join( client.mychans )


        client.sock_send( [ 'PART' , chans , ':' ] )

        client.sock_send( [ 'JOIN' , '0' ] )

