
# xterm256 control codes


def reset():  return  '\x1B[m'

def bold():   return  '\x1B[1m'

def light():  return  '\x1B[2m'

def italic(): return  '\x1B[3m'

def uline():  return  '\x1B[4m'


def invers(): return  '\x1B[7m'


def normal(): return  '\x1B[22m' # reset bold() / light()

def endul():  return  '\x1B[24m' # reset uline()


def color(n): return f'\x1B[38;5;{n}m'

def endcol(): return f'\x1B[39m' # reset color()


def bgcol(n): return f'\x1B[48;5;{n}m'


def clear():  return  '\r\x1B[K'
