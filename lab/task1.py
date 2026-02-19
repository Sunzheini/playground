"""
input 1
1, Jhon
2, Mike
input 2
1, 28

output:
1, Jhon, 28
2, Mike
"""
def function_1(file1, file2):
    """
    :param file1: scv file
    :param file2: scv file
    :return: combined scv file with merged data
    """
    ids_and_data_from_file_1 = dict()
    ids_and_data_from_file_2 = dict()

    with open(file1, 'r') as f1:
        list_of_lines_from_file_1 = f1.read().splitlines()

        for line in list_of_lines_from_file_1:
            id_and_data = line.split(',')
            id = id_and_data[0]
            data = id_and_data[1:]
            ids_and_data_from_file_1[id] = data

    with open(file2, 'r') as f2:
        list_of_lines_from_file_2 = f2.read().splitlines()

        for line in list_of_lines_from_file_2:
            id_and_data = line.split(',')
            id = id_and_data[0]
            data = id_and_data[1:]
            ids_and_data_from_file_2[id] = data

    combined_data = dict()

    # use case without using Union of sets
    for id, data in ids_and_data_from_file_1.items():
        if id in ids_and_data_from_file_2:
            combined_data[id] = data + ids_and_data_from_file_2[id]
        else:
            combined_data[id] = data

    for id, data in ids_and_data_from_file_2.items():
        if id not in combined_data:
            combined_data[id] = data

    # use case with using Union of sets

    #print the data
    for id, data in combined_data.items():
        print(f"{', '.join(data)}")
