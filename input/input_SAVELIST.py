

# handle user SAVELIST


def handle(client, kb_args):

    client.save_list = True

    client.sock_send('LIST')
