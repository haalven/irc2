

# handle PING

from plugin.rss_reader import rss_reader


def handle(client,msg):


    client.sock_send( ['PONG', msg['PAR'][0]] )


    # RSS

    if client.registered:

        if 'RSS_CHAN' in client.profile:

            for rss_channel in client.profile['RSS_CHAN']:

                rss_reader(client, rss_channel)
