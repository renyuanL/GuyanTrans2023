#%%
# using openAI whisper to transcrbie the mp4 files in current directory
# and save the transcription in a text file

import os
import glob
import tqdm

#cmd0= 'yt-dlp --format worstvideo[ext=mp4]+bestaudio[ext=m4a] --playlist-items 101-500 https://www.youtube.com/@ksguyan/videos'
#print(cmd0)
#os.system(cmd0)

'''
cmd00=   'yt-dlp --no-simulate '
cmd00 += '--format wv[ext=mp4]+ba[ext=m4a] '
cmd00 += '--print "%(n_entries)04d, %(playlist_index)04d, %(duration)05d, [%(id)s], <%(filename)s>"  '
#cmd00 += '-o "%(playlist)s/%(n_entries-playlist_index)04d-%(title)s [%(id)s].%(ext)s" '
cmd00 += '-o "%(playlist)s/%(playlist_index)04d-%(title)s [%(id)s].%(ext)s" '
cmd00 += 'https://youtube.com/playlist?list=PLwEV3aNvNd3w-5LP4OCnQoFJGZ1sxoDep '
cmd00 += '1>fList.1.txt 2>fList.2.txt'

os.system(cmd00)
'''


#mp4Path= '..\\ex003_0001-1000\\'
#mp4Path= 'ex004_1000_2000'
#mp4Path= '112年6月 阿彌陀佛紐涅二日禪'
#mp4Path= '2023_7月_7日禪'
#mp4Path= 'tgt'


mp4Path= 'tgt02_楞伽經'
mp4Path= 'tgt'

fList=  glob.glob(f'{mp4Path}/*.mp4')
fList+= glob.glob(f'{mp4Path}/*/*.mp4')
fList+= glob.glob(f'{mp4Path}/*/*/*.mp4')
fList+= glob.glob(f'{mp4Path}/*/*/*/*.mp4')

# print(f'{fList= }')

model_size= 'tiny'
device=     'cuda' # 'cpu'

cmd0=   'whisper  --output_format srt '
cmd0 += '--language zh --initial_prompt "台灣 繁體 中文 佛經 楞嚴經 圓覺經 法句經。" '

cmd0 += f'--model {model_size} '
cmd0 += f'--device {device} '

cmd0 += f'--output_dir "srt_{mp4Path}_{model_size}_{device}" '

    
for f in tqdm.tqdm(fList): 
    #print(f'{f= } ')
    # check if the srt file exists

    cmd= cmd0 + f'"{f}"'
    print(cmd)
    os.system(cmd)




# %%
