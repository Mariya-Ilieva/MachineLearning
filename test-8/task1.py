class ConfigParser:
    def __init__(self):
        self.config = {}

    def read(self, filename):
        with open(filename, 'r') as f:
            section = None

            for line in f:
                line = line.strip()

                if not line or line.startswith(';') or line.startswith('#'):
                    continue

                if line.startswith('[') and line.endswith(']'):
                    section = line[1:-1]
                    self.config[section] = {}
                elif '=' in line:
                    k, v = line.split('=')
                    self.config[section][k.strip()] = v.strip()
                elif ':' in line:
                    k, v = line.split(':')
                    self.config[section][k.strip()] = v.strip()

    def sections(self):
        return list(self.config.keys())

    def items(self, section):
        return self.config.get(section, {}).items()

    def get(self, section, option, fallback=None):
        return self.config.get(section, {})


cfg = ConfigParser()
cfg.read('config.ini')

sections = cfg.sections()

a = cfg.get('section1', 'name1')
b = cfg.get('section2', 'name2', fallback='No such things')

print(a)
print(b)

########################################################################

parser = ConfigParser()
parser.read('sampleconfig.ini')

for sect in parser.sections():
    print('Section:', sect)

    for k, v in parser.items(sect):
        print(' {} = {}'.format(k, v))
    print()
