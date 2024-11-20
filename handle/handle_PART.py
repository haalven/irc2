

# handle PART

from drop_item import drop_item


def handle(client,msg):


    # YOU parted a channel
    if msg['KEY'] == 'YOU_PART':


        # track your channels
        drop_item(client, client.mychans, msg['PAR'][0] )
