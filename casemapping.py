
# casemapping

# some servers allowing non-ASCII chars in nicknames
# apply casefolding to some of these chars (like ä,ö,ü)


from time_calc import now
from xterm_control import color, endcol


def casemapped(client, string):

    if client.casemap:
        return string.translate(client.casemaps[client.casemap])
    else:
        return string.translate(client.casemaps['ascii']) # fallback


# see handle_005
def set_casemap(client):

    CASEMAPPING = client.isupport['CASEMAPPING'].lower()

    if CASEMAPPING == 'strict-rfc1459':
        CASEMAPPING = 'rfc1459'

    if not CASEMAPPING in ['ascii','rfc1459']:
        print( now(), color(196) + 'WARNING:', 'unknown casemapping.',
            'using "ascii" instead.' + endcol() )
        CASEMAPPING = 'ascii'

    client.casemap = CASEMAPPING


def load_casemaps(client):

# RFC 1459 casemapping
# uppercase: ABCDEFGHIJKLMNOPQRSTUVWXYZ{|}~
# lowercase: abcdefghijklmnopqrstuvwxyz[\]^

    client.casemaps = {
        'ascii': {
            65: 97,
            66: 98,
            67: 99,
            68: 100,
            69: 101,
            70: 102,
            71: 103,
            72: 104,
            73: 105,
            74: 106,
            75: 107,
            76: 108,
            77: 109,
            78: 110,
            79: 111,
            80: 112,
            81: 113,
            82: 114,
            83: 115,
            84: 116,
            85: 117,
            86: 118,
            87: 119,
            88: 120,
            89: 121,
            90: 122
        },
        'rfc1459': {
            65: 97,
            66: 98,
            67: 99,
            68: 100,
            69: 101,
            70: 102,
            71: 103,
            72: 104,
            73: 105,
            74: 106,
            75: 107,
            76: 108,
            77: 109,
            78: 110,
            79: 111,
            80: 112,
            81: 113,
            82: 114,
            83: 115,
            84: 116,
            85: 117,
            86: 118,
            87: 119,
            88: 120,
            89: 121,
            90: 122,
            91: 123,
            92: 124,
            93: 125,
            94: 126
        }
    }
