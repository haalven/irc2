
# colored re-match in text

import re


def match_fmt(text, pattern, FMT1, FMT2):

    p = re.compile(pattern, re.IGNORECASE)

    def color_str(match):

        return FMT1 + match.group() + FMT2

    return p.sub(color_str, text)



# matches channels and links

def links_fmt(text, FMT1, FMT2):

    pattern = r'(#{1,2}[\w\-\.]+|([a-z0-9][a-z0-9-]{1,63}\.){1,}[a-z]{2,63})'

    return match_fmt(text, pattern, FMT1, FMT2)
