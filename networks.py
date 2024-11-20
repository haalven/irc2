
# IRC networks


def net_urls(netstring):


    net_urls = {

        'ircnet':       ['https://www.ircnet.com/',
                         'https://www.ircnet.info/',
                         'http://www.ircnet.net/'],

        'efnet':        ['http://www.efnet.org/'],

        'undernet':     ['https://www.undernet.org/'],

        'dalnet':       ['https://www.dal.net/'],

        'quakenet':     ['https://www.quakenet.org/'],

        'oftc':         ['https://www.oftc.net/'],

        'libera.chat':  ['https://libera.chat/'],

        'espernet':     ['https://www.esper.net/'],

        'hackint':      ['https://hackint.org/'],

        'tilde.chat':   ['https://tilde.chat/'],

        'gimpnet':      ['https://www.gimp.org/'],

        'alphachat':    ['https://www.alphachat.net/'],

        'geekshed':     ['http://www.geekshed.net/'],

        'ergo':         ['https://ergo.chat/about-network'],

        'synirc':       ['https://www.synirc.net/'],

        'fishnet':      ['https://wetfish.net/'],

        'mindforge':    ['https://mindforge.org/'],

        'stardustnetwork': ['https://stardust.cx/'],

        'german-elite': ['https://www.german-elite.net/'],

        'atrum':        ['http://atrum.org/'],

        'irchighway':   ['https://irchighway.net/'],

        'furnet':       ['http://www.furnet.org/wiki'],

        'austnet':      ['https://www.austnet.org/'],

        '2600net':      ['https://scuttled.net/'],

        'sdf':          ['https://sdf.org/'],

        'chatlounge':   ['https://www.chatlounge.net/'],

        'linknet':      ['https://www.link-net.org/']

    }


    netstring = netstring.lower()

    if netstring in net_urls:

        return net_urls[netstring]

    return []
