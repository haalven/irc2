

# handle NICK

from is_active import is_active, update_active
from drop_item import drop_item


def handle(client,msg):


    # track your nickname

    if msg['KEY'] == 'YOU_NICK':

        client.mynick = msg['PAR'][0]


    # track active nicks

    active_dt = is_active(client, msg['NICK'], msg['DATE'])

    if active_dt:

        drop_item(client, client.active_nicks, msg['NICK'])

        update_active(client, msg['PAR'][0], active_dt)
