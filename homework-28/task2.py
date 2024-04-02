def format_value(value, template):
    try:
        if template:
            return format(value, template)
        else:
            return str(value)

    except ValueError:
        return '{{' + str(value) + '}}'

def process_placeholder(placeholder, *args, **kwargs):
    if ':' in placeholder:
        field_name, format_template = placeholder.split(':')
    else:
        field_name, format_template = placeholder, None

    if field_name.isdigit():
        return format_value(args[int(field_name)], format_template)
    elif field_name.isalpha():
        return format_value(kwargs.get(field_name, '{{' + placeholder + '}}'), format_template)
    else:
        return '{{' + placeholder + '}}'

def strformat(template, *args, **kwargs):
    if not (args or kwargs):
        return template

    result = ''
    arg_idx = 0

    while arg_idx < len(template):
        if template[arg_idx] == '{':
            closing = template.find('}', arg_idx)

            if closing != -1:
                placeholder = template[arg_idx + 1:closing]
                result += process_placeholder(placeholder, *args, **kwargs)
                arg_idx = closing + 1
            else:
                result += template[arg_idx:]

        else:
            result += template[arg_idx]

        arg_idx += 1

    return result

x = 123.456
print(strformat('Value is {0:10.2f}', x))
print(strformat('Value is {val:<*10.2f}', val=x))

name = 'IBM'
shares = 50
price = 490.1
print(strformat('{:>10s} {:10d} {:10.2f}', name, shares, price))

print(strformat('<{tag}>{text}</{tag}>', tag='p', text='hello world'))
