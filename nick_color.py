
# nick color

from hashlib import md5
from source_parse import source_expand
from xterm_control import color


# uniq str
def uniq_name(src):

    nick, _, user, host = source_expand(src)

    if user in ['DC']:
        uniq = host if host else nick.lower()
    elif user in ['~u', '~haha']:
        uniq = nick.lower()
    else:
        uniq = user.replace('~','') if user else nick.lower()

    return uniq


# colored nicks
def nick_color(src):

    uniq = uniq_name(src)

    colors  = [24,25,26,27,31,32,33,37,38,39,60,61,62,63,66,67,68,69,73,74,75]

    default = 31

    try:
        hashed = md5(uniq.encode())
        digest = int(hashed.hexdigest(), 16)
        factor = float('0.' + str(digest)[-3:])
        index  = int(factor * len(colors))
        ccode  = colors[index]

        return color(ccode)

    except Exception: return color(default)

