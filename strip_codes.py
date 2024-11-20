
# strip chars > 1FFFF,
# strip formatting codes,
# strip control chars

from re import sub


def strip_codes(text):


    # 1) remove chars > 1FFFF

    text = ''.join(c for c in text if ord(c) < 0x20000)



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

