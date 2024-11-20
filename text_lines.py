
# read lines of a textfile


def text_lines(filepath):

    try:
        with open(filepath) as f:  lines = f.read().split('\n')


    except Exception: return []


    while '' in lines: lines.remove('')

    return lines
