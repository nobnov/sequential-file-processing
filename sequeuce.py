import datetime
import glob

f = open("dir.txt", "r")
files = sorted(glob.glob(f.read()))

split_file_name = ''
file_time_plus_one_seconds = ''

sequence_list = []

for file in files:
    split_name = file.split('-')

    file_time = datetime.datetime.strptime(split_name[2], '%Y%m%d%H%M%S')

    if not sequence_list:
        sequence_list.append(file)

    elif split_file_name == file_time or file_time_plus_one_seconds == file_time:
        sequence_list.append(file)

    else:
        print(sequence_list)

        sequence_list.clear()
        sequence_list.append(file)

    split_file_name = file_time
    file_time_plus_one_seconds = file_time + datetime.timedelta(seconds=1)
