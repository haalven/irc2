

# handle user RSS

from time_calc import now


def handle(client, rss_arg):

    date = now()

    rss = False

    if 'RSS_CHAN' in client.profile:

        for rss_channel in client.profile['RSS_CHAN']:

            print(date, '[RSS]', rss_channel, '<-', client.profile['RSS_CHAN'][rss_channel])

            rss = True

    if not rss:

        print(date, '[RSS]', 'no active RSS feeds .')
