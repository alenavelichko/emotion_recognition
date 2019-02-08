import datetime
import os
import pandas as pd
import numpy as np
import subprocess


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
start_time_n = []
stop_time_n = []
difference_n = []
segments = []
k = 0


def to_fixed(numobj, digits=2):
    """ function to format floats (round off to 2 decimal places)  """
    return f"{numobj:.{digits}f}"


def to_format(chunk):
    """ function returns chunk in format HH:MM:SS.xxx  """
    temp = chunk.split('.')
    return str(datetime.timedelta(seconds=int(temp[0]), milliseconds=int(temp[1])))[:-3]


""" reading the data """
df = pd.read_csv(os.path.join(ROOT_DIR, 'data_Disgusted.csv'), sep=',')
file_names = np.array(df['File'])
start_time = np.array(df['Start'])
stop_time = np.array(df['End'])
difference = stop_time - start_time
difference = np.array(difference)

for s_time in start_time:
    start_time_n.append(to_fixed(s_time))
for sp_time in stop_time:
    stop_time_n.append(to_fixed(sp_time))
for diff_t in difference:
    difference_n.append(to_fixed(diff_t))

""" create new folder """

os.mkdir(os.path.join(ROOT_DIR, "Audio_dis"))

""" log the output and process files """

N = len(start_time_n)
with open("debug_info.txt", "w") as logfile:
    for index in range(N):
        input_file = os.path.join(ROOT_DIR, 'Audio', file_names[index] + '_mic' + '.wav')
        output_file = os.path.join(ROOT_DIR, 'Audio_dis', file_names[index] + '_' + str(k) + '.wav')

        """ to trim audio files with ffmpeg: 
        ffmpeg - i 10 dec_D11_1_mic.wav - acodec copy - ss 00:02:00 - t 00:04:00 trim_audio.wav """

        subprocess.call(["ffmpeg", "-i", str(input_file), "-ss", to_format(start_time_n[index]), "-t",
                         to_format(difference_n[index]), "-c", "copy", str(output_file)])
        logfile.write("ffmpeg -i " + str(input_file) + " -ss " + to_format(start_time_n[index]) + " -t " +
                      to_format(difference_n[index]) + " -c copy " + str(output_file) + "\n")
        k += 1
