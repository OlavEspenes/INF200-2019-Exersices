def letter_freq(txt):
    dictionary = {}
    txt = txt.lower()
    for k in txt:
        if k in dictionary:
            dictionary[k] += 1
        else:
            dictionary[k] = 1
    return dictionary

if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))