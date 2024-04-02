import sys


def format_exc(Exception):
    type, value, tb = sys.exc_info()

    msg = 'Traceback (most recent call last):\n'

    while tb is not None:
        frame = tb.tb_frame

        filename = frame.f_code.co_filename
        lineno = tb.tb_lineno
        name = frame.f_code.co_name

        with open(filename, 'r') as f:
            lines = f.readlines()
            line = lines[lineno - 1].strip()

        msg += f'File "{filename}", line {lineno}, in {name}\n'
        msg += f'  {line}\n'
        tb = tb.tb_next

    msg += f'{type.__name__}: {value}\n'

    return msg

def a():
    raise TypeError('Oups!')

def b():
    a()

try:
    b()
except Exception as e:
    traceback_msg = format_exc(e)
    print(traceback_msg)
