

# handle user PARTALL


def handle(client, kb_args):

    if not client.mychans: return None

    all_chans = ','.join(client.mychans)

    part_msg  = '\x20'.join(kb_args) if kb_args else ''

    client.sock_send([ 'PART' , all_chans , ':' + part_msg ])

    client.sock_send([ 'JOIN' , '0' ])
