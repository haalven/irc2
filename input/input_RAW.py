

# handle user RAW

from input import input_HELP
from time_calc import now


def handle(client, kb_args):

    def raw_on(client):
        client.showraw = True
        print( now() , 'OK: raw messages enabled .' )

    def raw_off(client):
        client.showraw = False
        print( now() , 'OK: raw messages disabled .' )


    if kb_args[0]:

        if kb_args[0].lower() == 'on':
            raw_on(client)


        elif kb_args[0].lower() == 'off':
            raw_off(client)

        else:
            input_HELP.handle(client, ['RAW']); return None


    elif not client.showraw:
        raw_on(client)

    else:
        raw_off(client)

