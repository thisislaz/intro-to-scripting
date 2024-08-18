import csv

fname = input()

with open(fname, 'r') as file:
    csv_reader = file.readlines()
    line_list = [
        [int(line.strip()) for line in csv_reader if line.strip().isnumeric()],
        [line.strip() for line in csv_reader if not line.strip().isnumeric()]
    ]
    new_object = {}
    for key,value in zip(line_list[0],line_list[1]):
        if key in new_object:
            new_object[key] += "; "+value
        else:
            new_object[key] = value

with open('output_keys.txt', 'w') as new_file:
    sorted_obj = dict(sorted(new_object.items()))
    for key,value in sorted_obj.items():
        new_file.write("{}: {}\n".format(key,value))

with open('output_titles.txt', 'w') as title_file:
    for titles in sorted(line_list[1]):
        title_file.write(f"{titles}\n")