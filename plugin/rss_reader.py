

# RSS plugin

from am_i_in import am_i_in
from os import system
from xml.dom.minidom import parseString
from hashlib import md5
from os.path import exists
from json import dump, load
from html import unescape


def badcheck(rsstext):

    # badwords
    badwords = ['spacex','elon','musk','starship','falcon']

    for badword in badwords:
        if badword in rsstext.lower(): return True

    return False


def rss_reader(client, rss_channel):

    # the channel
    if not am_i_in(client, rss_channel): return None

    # load feeds
    feeds = client.profile['RSS_CHAN'][rss_channel]


    # process feeds -> fill stack

    stack  = []

    for feed in feeds:
        feedurl  = feeds[feed]
        rssfile  = client.ircpath + '/rss/' + 'rssfeed-' + feed + '.xml'
        digsfile = client.ircpath + '/rss/' + 'rssdigs-' + feed + '.json'

        # download
        system(f'curl -4 -s "{feedurl}" > "{rssfile}"')
        #decode
        try:
            with open(rssfile, encoding='utf-8') as f: xmldata = f.read()
        except UnicodeDecodeError:
            with open(rssfile, encoding='latin-1') as f: xmldata = f.read()
        # verify
        if not xmldata: continue
        # parse
        try: rssdom = parseString(xmldata)
        except Exception: continue
        # get items
        items = rssdom.getElementsByTagName('item')

        # collect data
        titles = {}
        for item in items:

            # title
            title_element = item.getElementsByTagName('title')
            if title_element:
                try: title = title_element[0].firstChild.nodeValue.strip()
                except Exception: continue
                title = unescape(title)

            # link
            link_element = item.getElementsByTagName('link')
            if link_element:
                try: link = link_element[0].firstChild.nodeValue.strip()
                except Exception: continue

            # hash/digest
            if title and link:
                hashed = md5(link.encode())
                digest = hashed.hexdigest()
                titles[digest] = (title, link)

        # load known hashes
        if not exists(digsfile):
            silent = True
            known  = []
        else:
            silent = False
            with open(digsfile) as f:
                known = load(f)

        # add new titles to stack
        for dig in titles:
            if not (dig in known):
                title, link = titles[dig]
                rsstext = f'{title} ({feed})'
                known.append(dig)
                if not (badcheck(rsstext) or silent):
                    stack.append(rsstext)

        # save known hashes
        with open(digsfile, 'w') as f:
            dump(known, f)


    # process stack
    if len(stack) > 5: stack = stack[:5]
    for rsstext in stack:
        client.sock_send([ 'PRIVMSG' , rss_channel , ':' + rsstext ])

