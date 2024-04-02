def format(x, f):
    if isinstance(x, (int, float)):
        return format_numeric(x, f)
    elif isinstance(x, str):
        return format_string(x, f)

    raise TypeError(f'Unsupported type: {type(x)} for format')

def format_numeric(x, f):
    if not isinstance(f, str):
        raise TypeError(f'Format specification must be a string, you typed: {f}')

    width, precision, conversion_type = 0, 0, ''

    if '.' in f:
        width_part, precision_part = f.split('.')
        width = int(width_part)
        precision = int(precision_part[:-1])
    elif f.isdigit():
        width = int(f)
    elif f[-1] in ('d', 'x', 'b'):
        conversion_type = f[-1]
    elif f in ('f', 'e', '%'):
        conversion_type = f

    if conversion_type:
        if conversion_type == 'f':
            formatted_x = '{:0.{}f}'.format(x, precision)
        elif conversion_type == 'e':
            formatted_x = '{:0.{}e}'.format(x, precision)
        elif conversion_type == '%':
            formatted_x = '{:0.{}%}'.format(x, precision)
    else:
        formatted_x = '{:0}'.format(x)

    if isinstance(x, (int, float)):
        if conversion_type:
            formatted_x = '{:' + conversion_type + '}'
            formatted_x = formatted_x.format(x)
        else:
            formatted_x = '{:.' + str(precision) + 'f}'
            formatted_x = formatted_x.format(x)

        if width > 0:
            total_width = len(formatted_x)
            align = f[0] if f[0] in ('<', '>', '=', '^') else '>'
            formatted_x = '{:{}{}}'.format(formatted_x, align, width)

            if total_width < width:
                if x >= 0:
                    formatted_x = ' ' + formatted_x
                formatted_x = '{:>{}}'.format(formatted_x, width)

            return formatted_x

def format_string(x, f):
    if not isinstance(f, str):
        raise TypeError(f'Format specification must be a string, you typed: {f}')

    width = 0
    align = ''
    padding_char = ''

    if f.isdigit():
        width = int(f)
    elif f and f[0] in ('<', '>', '^', '='):
        align = f[0]

        if f[1:].isdigit():
            width = int(f[1:])
        elif f[1] == '*':
            padding_char = f[1]

    f = '{:' + padding_char + align + str(width) + '}'

    return f.format(x)


x = 123.456
print(format(x, '0.2f'))    # '123.46'
print(format(x, '10.4f'))   # '    123.4560'

name = 'Elwood'
print(format(name, '<10'))   # 'Elwood    '
print(format(name, '>10'))   # '    Elwood'
print(format(name, '^10'))   # '  Elwood  '
print(format(name, '*^10'))  # '**Elwood**'

x = 42
print(format(x, '10d'))  # '        42'
print(format(x, '10x'))  # '        2a'
print(format(x, '10b'))  # '    101010'
print(format(x, '010b')) # '0000101010'

y = 3.1415926
print(format(y, '10.2f'))   # r = '      3.14'
print(format(y, '10.2e'))   # r = '  3.14e+00'
print(format(y, '+10.2f'))  # r = '     +3.14'
print(format(y, '+010.2f')) # r = '+000003.14'
