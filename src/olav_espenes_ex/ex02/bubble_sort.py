def bubble_sort(file):
    """Sort list with number in increasing order
    """
    data_list = list(file)
    length_list = len(file)

    for element in range(length_list):
        for sec_element in range(0, length_list - element - 1):
            if data_list[sec_element] > data_list[sec_element + 1]:
                data_list[sec_element], data_list[sec_element + 1] = data_list[sec_element + 1], data_list[sec_element]
    return data_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
