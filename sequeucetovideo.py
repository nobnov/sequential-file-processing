import datetime
import glob

import cv2

f = open("dir.txt", "r")
files = sorted(glob.glob(f.read()))

split_file_name = ''
file_time_plus_one_seconds = ''

sequence_list = []
sequence_img = []

for file in files:
    split_name = file.split('-')

    file_time = datetime.datetime.strptime(split_name[2], '%Y%m%d%H%M%S')

    if not sequence_list:
        sequence_list.append(file)

        img = cv2.imread(file)
        sequence_img.append(img)
    elif split_file_name == file_time or file_time_plus_one_seconds == file_time:
        sequence_list.append(file)

        img = cv2.imread(file)
        sequence_img.append(img)
    else:
        first_file_split_name = sequence_list[0].split('.')
        first_file_split_name = first_file_split_name[0]
        first_file_split_name = first_file_split_name.split('/')
        first_file_split_name = first_file_split_name[-1]

        last_file_split_name = sequence_list[len(sequence_list) - 1].split('.')
        last_file_split_name = last_file_split_name[0]
        last_file_split_name = last_file_split_name.split('/')
        last_file_split_name = last_file_split_name[-1]

        height, width, layers = img.shape
        size = (width, height)

        name = 'video/' + first_file_split_name + '-to-' + last_file_split_name + '.mp4'
        out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'), 3.0, size)

        for i in range(len(sequence_list)):
            out.write(sequence_img[i])
        out.release()

        sequence_list.clear()
        sequence_list.append(file)

        sequence_img.clear()
        img = cv2.imread(file)
        sequence_img.append(img)

    split_file_name = file_time
    file_time_plus_one_seconds = file_time + datetime.timedelta(seconds=1)
