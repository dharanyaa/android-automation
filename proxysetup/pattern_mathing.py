import re


# def beacon_check(file_path
#                  , reg='https://s-et-rc-w.inmobi.com/[a-zA-Z0-9./-]+/1/[a-zA-Z0-9~./-]+'):
def beacon_check(file_path):
    reg = 'https://s-et-rc-w.inmobi.com/[a-zA-Z0-9./-]+/1/[a-zA-Z0-9~./-]+'
    print '*******'
    print file_path
    with open(file_path, 'r') as file:
        log_file = file.read()
        pattern = re.compile(r'{0}'.format(reg))
        matches = pattern.finditer(log_file)
        list_matched_string = list()
        for match in matches:
            list_matched_string.append(match.group())
    return list_matched_string







