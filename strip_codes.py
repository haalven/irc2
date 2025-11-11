
# strip chars > 1FFFF,
# strip formatting codes,
# strip control chars

from re import sub


def strip_codes(text):


    # 1) remove chars > 1FFFF

    text = ''.join(c for c in text if ord(c) < 0x20000)

    # NEW whitelist range filter:

#    whitelist = r'[^' \
#                r'\s\n' \
#                r'\u0000-\u007e' \
#                r'\u00a0-\u200a' \
#                r'\u2010-\u22ff' \
#                r'\u2c00-\ufdff' \
#                r']'
#    text = sub(whitelist, '', text)


    # 2) remove formatting codes

    mirccodes = r'\x03(\d{1,2}(,\d{1,2})?)?'
    text = sub(mirccodes, '', text)

    hexccodes = r'\x04([0-9a-fA-F]{6}(,[0-9a-fA-F]{6})?)?'
    text = sub(hexccodes, '', text)

    ansicodes = r'\x1B\[[0-?]*[ -/]*[@-~]'
    text = sub(ansicodes, '', text)



    # 3) remove ascii control chars

    toremove = dict.fromkeys(range(32))

    toremove[127] = None  # delete key

    # pass \x01 and \x09

    toremove.pop(1)  # CTCP commands

    toremove.pop(9)  # horizontal tab

    # translate the dict

    text = text.translate(toremove)



    # return

    return text

