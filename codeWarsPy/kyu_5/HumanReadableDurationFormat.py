def format_duration(seconds):
    ss = seconds % 60
    minutes = seconds / 60
    mm = minutes % 60
    hours = minutes / 60
    hh = hours % 24
    days = hours / 24
    dd = days % 365
    years = days / 24


def get_text(s, n):
    if not n:
        return ''
    if n == 1:
        return str(n) +
