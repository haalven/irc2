

# handle user TOP10


def handle(client, kb_args):

    client.top_list = True

    client.sock_send('LIST')
