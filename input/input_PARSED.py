

# handle user PARSED

from input import input_HELP
from time_calc import now


def handle(client, kb_args):

    def showparsed_on(client):
        client.showparsed = True
        print( now() , 'OK: parsed enabled .' )

    def showparsed_off(client):
        client.showparsed = False
        print( now() , 'OK: parsed disabled .' )


    if kb_args[0]:

        if kb_args[0].lower() == 'on':
            showparsed_on(client)


        elif kb_args[0].lower() == 'off':
            showparsed_off(client)

        else:
            input_HELP.handle(client, ['PARSED']); return None


    elif not client.showparsed:
        showparsed_on(client)

    else:
        showparsed_off(client)

