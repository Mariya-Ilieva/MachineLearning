import sys


class ArgumentParser:
    def __init__(self):
        self.arguments = {}

    def add_argument(self, name, help_text):
        self.arguments[name] = help_text

    @staticmethod
    def parse_args(args=None):
        if args is None:
            args = sys.argv[1:]

        output = {}
        arg1 = None

        for arg in args:
            if arg.startswith('--'):
                arg1 = arg.lstrip('-')
            elif arg.startswith('-'):
                arg1 = arg.lstrip('-')
                output[arg1] = None
            elif arg1:
                output[arg1] = arg
                arg1 = None

        return output

    def print_help(self):
        print('Usage:')

        for arg, help_text in self.arguments.items():
            print(f'  -{arg}: {help_text}')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input', 'Input file')
    parser.add_argument('output', 'Output file')

    namespace = parser.parse_args(['-input', 'input.txt', '--output', 'output.txt'])
    print(namespace)

    parser.print_help()



# class ArgumentParser:
#     def __init__(self, description=None):
#         self.description = description
#         self.arguments = {}
#
#     def add_argument(self, name, type=None, help='', action=None):
#         self.arguments[name] = {'type': type, 'help': help, 'action': action, 'value': None}
#
#     def parse_args(self):
#         return self.arguments
#
#
# if __name__ == '__main__':
#     parser = ArgumentParser()
#     args = parser.parse_args()
#
#     print('Arguments:', args)
