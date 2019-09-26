def char_counts(textfilename):
    """Counts characters in a text.
    """

    with open(textfilename, 'r') as myfile:
        data = myfile.read()
        counter = {}
        for element in data:
            if ord(element) in counter:
                counter[ord(element)] += 1
            else:
                counter[ord(element)] = 1
        dict_a = {key: 0 for key in range(256)}
        dict_a.update(counter)
        list_a = list(dict_a.values())
    return list_a


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
