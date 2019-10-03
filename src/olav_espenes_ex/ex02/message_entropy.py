from math import log2


def letter_freq(txt):
    """Find the frequent of every letter in a text.
    """
    counter = {}
    txt = txt.lower()
    for character in txt:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter


def entropy(message):
    counter = letter_freq(message)
    values_sum = sum(counter.values())
    freq = {ord(key): value / values_sum for key, value in counter.items()}
    entropy_calculated = 0
    for value in freq.values():
        entropy_calculated += -value * log2(value)
    return entropy_calculated


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
