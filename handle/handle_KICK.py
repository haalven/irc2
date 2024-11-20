

# handle KICK

from drop_item import drop_item


def handle(client,msg):


    # YOU have been kicked
    if msg['KEY'] == 'YOUR_KICKED':


        # track your channels
        drop_item(client, client.mychans, msg['PAR'][0] )
