
# coding: utf-8

# In[ ]:



import numpy as np
import pandas as pd
import sys
import os
from subprocess import check_output
import time
import multiprocessing as mp

# sys.path.append('/homedtic/georgid/workspace/AlignmentMagix/src/align/')
# import doit

perfs_file = '/mnt/vmdata/camut/DAMP/perfs20.csv'

df = pd.read_csv(perfs_file, header=None)

lyrics_folder = '/mnt/vmdata/camut/DAMP/lyrics/'
wav_songs_folder = '/mnt/vmdata/camut/DAMP/DAMP_from_smule_website_wav/'
output_folder = '/mnt/vmdata/camut/DAMP/alignments_DNN/'


def check(item):
    s_name = os.path.join(wav_songs_folder, "{}.wav".format(item[1][1]))
    l_name = os.path.join(lyrics_folder, item[1][2])
    out = os.path.join(output_folder, "{}.txt".format(item[1][1]))
    
#     print(item[1][1], item[1][2])

    if os.path.isfile(out):
        return ('{} exist'.format(out).split('/')[-1])
    else:
        output = check_output(['python', '/homedtic/georgid/workspace/AlignmentMagix/src/align/doit.py', s_name, l_name, '0', out])    
        return ('{} == {}'.format(('{} exist'.format(out).split('/')[-1]), output))

def ite(rows, nrows=4):
    
    ls = []
    counter = 0
    for item in df.iterrows():
        ls.append(item)
        
        if counter == nrows:
            yield ls
            ls = []
            counter = 0
        else:
            counter = counter + 1
        
        
        
for item in df.iterrows():
    try:

        start = time.time()
        print(check(item))
        print(' time: {} '.format(time.time() - start ))
    except Exception as e:
        print('error')
        print(item)

	# print(song_name)
# print(lyrics_name)


# !python /homedtic/georgid/workspace/AlignmentMagix/src/align/doit.py /mnt/vmdata/camut/DAMP/DAMP_from_smule_website_wav/131698369_27844120.wav lyrics_data/_all_american_girl 0 output.lab



# In[41]:


