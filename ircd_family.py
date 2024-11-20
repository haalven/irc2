
# ircd taxonomy

from re import search


def ircd_family(version):

    ircd_families = {
        'nefarious': [r'\+Nefarious'],
        'snircd':    [r'\+snircd'],
        'oftc':      [r'\+oftc'],
        'ircd':      [r'^\d\.\d\d'],
        'ircu':      [r'^u\d\.'],
        'yeti':      [r'^yeti'],
        'hybrid':    [r'^hybrid'],
        'bahamut':   [r'^bahamut'],
        'plexus':    [r'^plexus'],
        'ratbox':    [r'^ircd-ratbox'],
        'linknet':   [r'^LinkNet'],
        'charybdis': [r'^charybdis', r'^ChatIRCd'],
        'solanum':   [r'^solanum'],
        'unreal':    [r'^Unreal', r'^Piss'],
        'inspircd':  [r'^InspIRCd'],
        'euircd':    [r'^euIRCd'],
        'ngircd':    [r'^ngircd'],
        'ergo':      [r'^ergo'],
        'bouncer':   [r'^prattle-']
    }


    for family in ircd_families:

        for pattern in ircd_families[family]:

            if search(pattern, version): return family

    return None


def ircd_urls(ircdfamily):

    ircd_urls = {

        'inspircd':  ['https://docs.inspircd.org',
                      'https://github.com/inspircd'],

        'unreal':    ['https://www.unrealircd.org/docs',
                      'https://github.com/unrealircd'],

        'solanum':   ['https://github.com/solanum-ircd'],

        'charybdis': ['https://github.com/charybdis-ircd'],

        'ircu':      ['https://coder-com.undernet.org',
                      'https://github.com/UndernetIRC'],

        'hybrid':    ['http://www.ircd-hybrid.org',
                      'https://github.com/ircd-hybrid'],

        'bahamut':   ['https://bahamut.dal.net',
                      'https://github.com/DALnet'],

        'plexus':    ['https://wiki.rizon.net',
                      'https://gitlab.com/rizon'],

        'ratbox':    ['https://www.ratbox.org'],

        'ngircd':    ['https://ngircd.barton.de',
                      'https://github.com/ngircd'],

        'ergo':      ['https://ergo.chat',
                      'https://github.com/ergochat'],

        'nefarious': ['https://github.com/evilnet'],

        'oftc':      ['https://github.com/oftc'],

        'twitch':    ['https://dev.twitch.tv/docs/irc/guide']

    }

    if ircdfamily in ircd_urls:

        return ircd_urls[ircdfamily]

    return []

