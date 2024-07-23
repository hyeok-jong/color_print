def color_print(text, color='red', bg_color=None, bold=False, underline=False, strikethrough=False):\
    # make all types to string.
    text = f'{text}'
    color_dict = {
        'black': '\033[30m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'orange': '\033[33m',
        'purple': '\033[35m',
        'pink': '\033[95m',
        'white': '\033[97m'
    }

    bg_color_dict = {
        'black': '\033[40m',
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
    }

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    STRIKETHROUGH = '\033[09m'
    ENDC = '\033[0m'

    if bold:
        text = BOLD + text
    if underline:
        text = UNDERLINE + text
    if strikethrough:
        text = STRIKETHROUGH + text
    if color:
        text = color_dict[color.lower()] + text
    if bg_color:
        text = bg_color_dict[bg_color.lower()] + text

    print(text + ENDC)


