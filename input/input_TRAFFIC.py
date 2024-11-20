

# handle user TRAFFIC

from input import input_HELP
from time_calc import now


def handle(client, kb_args):

    def traffic_on(client):
        client.hide_traffic = False
        print( now() , 'OK' , 'traffic is now shown .' )
        return

    def traffic_off(client):
        client.hide_traffic = True
        print( now() , 'OK' , 'traffic is now hidden .' )
        return

    match kb_args[0].lower():
        case 'on':  traffic_on(client); return
        case 'off': traffic_off(client); return
        case '':
            if client.hide_traffic:
                traffic_on(client); return
            else:
                traffic_off(client); return
            
    input_HELP.handle(client, ['TRAFFIC']); return None
