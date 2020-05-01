def parse_ini(file_path):
    d = {}
    section = None
    with open(file_path) as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if len(line):
                if line[0] == "[" and line[-1] == "]":
                    if "[" in section or "]" in section:
                        raise Exception("Not allowed char in section header at line {}".format(i + 1))
                    if section in d:
                        raise Exception("Duplicated section header at line {}".format(i + 1))
                    section = line[1:-1]
                    d[section] = {}
                else:
                    if section is None:
                        raise Exception("There is not section defined at line {}".format(i + 1))
                    parts = line.split("=")
                    if len(parts) != 2:
                        raise Exception("Ay mernem janit axr tenc chi kareli at line {}".format(i + 1))
                    key = parts[0].strip()
                    if key in d[section]:
                        raise Exception("Duplicated key for section at line {}".format(i + 1))
                    value = parts[1].strip()
                    if value[0] != "0" and value.isdecimal():
                        value = int(value)
                    d[section][key] = value
    return d


print(parse_ini("config.ini"))
