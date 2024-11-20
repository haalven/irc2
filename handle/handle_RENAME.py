

# handle RENAME

from drop_item import drop_item


def handle(client, msg):

    if len(msg['PAR']) < 2: return None

    old_name = msg['PAR'][0]
    new_name = msg['PAR'][1]

    # track your channels
    drop_item(client, client.mychans, old_name)

    client.mychans.append(new_name)

