

# handle NOTICE

from is_active import update_active


def handle(client,msg):


    # real notices:
    if msg['KEY'] == 'NOTICE':

        # update active nicks
        update_active(client, msg['NICK'], msg['DATE'])

