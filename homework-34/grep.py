import sys
import os
from pathlib import Path
import re


class ArgumentParser:
    def __init__(self):
        self.arguments = {}

    def add_argument(self, name, help_text):
        self.arguments[name] = help_text

    @staticmethod
    def parse_args(args=None):
        if args is None:
            args = sys.argv[1:]

        output = {'pattern': None, 'files': []}
        arg1 = None

        for arg in args:
            if arg == '--help':
                output['help'] = True
                return output

            elif arg.startswith('--'):
                arg1 = arg.lstrip('-')
            elif arg.startswith('-'):
                arg1 = arg.lstrip('-')
                output[arg1] = None
            elif arg1:
                output[arg1] = arg
                arg1 = None
            elif output['pattern'] is None:
                output['pattern'] = arg
            else:
                output['files'].append(arg)

        return output

    def print_help(self):
        print('Usage:')

        for arg, help_text in self.arguments.items():
            print(f'  -{arg}: {help_text}')


def process_file(file, pattern, show_filenames, show_line_numbers, whole_words_only):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                if whole_words_only and not re.search(fr'\b{pattern}\b', line):
                    continue

                if re.search(pattern, line):
                    print_result(file, line, line_number, show_filenames, show_line_numbers)

    except FileNotFoundError:
        print(f'grep: file: No such file or directory')

def search_files_recursively(directory, pattern, show_filenames, show_line_numbers, whole_words_only):
    for file in Path(directory).rglob('*'): # Path object that represents a path in the file system
        if file.is_file():
            process_file(file, pattern, show_filenames, show_line_numbers, whole_words_only)

def grep(args):
    pattern = args.get('pattern')
    if not pattern or not isinstance(pattern, str):
        print('Please provide a valid pattern.')
        return

    files = args.get('files', [])
    ignore_case = args.get('ignore-case', False)
    show_filenames = args.get('show-filenames', False)
    show_line_numbers = args.get('show-line-numbers', False)
    whole_words_only = args.get('whole-words-only', False)
    search_recursively = args.get('search-recursively', False)

    flags = re.IGNORECASE if ignore_case else 0
    compiled_pattern = re.compile(pattern, flags)

    def internal_grep(files):
        for file in files:
            if '*' in file or '?' in file:
                matching_files = [str(path) for path in Path().rglob(file)]
                internal_grep(matching_files)
            else:
                if os.path.isdir(file):
                    if search_recursively:
                        search_files_recursively(file, compiled_pattern, show_filenames,
                                                 show_line_numbers, whole_words_only)
                    else:
                        print(f'{file} is a directory. Use -r to search in directories recursively.')
                else:
                    process_file(file, compiled_pattern, show_filenames, show_line_numbers, whole_words_only)

    internal_grep(files)

def print_result(file, line, line_number, show_filenames, show_line_numbers):
    if show_filenames and show_line_numbers:
        print(f'{file}:{line_number}:{line.strip()}')
    elif show_filenames:
        print(f'{file}:{line.strip()}')
    elif show_line_numbers:
        print(f'{file}:{line_number}:{line.strip()}')
    else:
        print(line.strip())

def main():
    parser = ArgumentParser()

    parser.add_argument('--help', 'Show help message and exit.')
    parser.add_argument('pattern', 'Pattern to search.')
    parser.add_argument('files', 'File(s) to search.')
    parser.add_argument('-i', '--ignore-case')
    parser.add_argument('-l', '--show-filenames')
    parser.add_argument('-n', '--show-line-numbers')
    parser.add_argument('-w', '--whole-words-only')
    parser.add_argument('-r', '--search-recursively')

    args = parser.parse_args()

    if args.get('help') is not None:
        parser.print_help()
        sys.exit()

    grep(args)

if __name__ == '__main__':
    main()
