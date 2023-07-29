import os
import glob
import tqdm

#mp4Path= 'srt_2023_7月_7日禪_medium'
mp4Path= 'srt_2023_7月_7日禪_large'

#mp4Path= 'tmp000_校對'

#mp4Path= 'srt_六祖壇經'
mp4Path= 'srt_2023_7月_7日禪_large'

fList = glob.glob(f'{mp4Path}/*.srt')
fList+= glob.glob(f'{mp4Path}/*/*.srt')
fList+= glob.glob(f'{mp4Path}/*/*/*.srt')
fList+= glob.glob(f'{mp4Path}/*/*/*/*.srt')

# concat all srt files
# keep their filename as a independent line
# using \n\n to separate each file

numCh= 0
with (open(f'_{mp4Path}_.srt.txt', 'w', encoding='utf-8') as f,
      open(f'_{mp4Path}_.srt0.txt', 'w', encoding='utf-8') as f0):
    for n,i in tqdm.tqdm(enumerate(fList)):
        with open(i, 'r', encoding='utf-8') as f2:
            filename= os.path.basename(i)
            # extract the code enclosed in square bracket '[]'of filename
            # e.g.
            # input: "112年7月阿彌陀佛紐涅七日禪-0000-112年7月阿彌陀佛紐涅七日禪(第1集) [FaCLg4H0BU0].srt"
            # output: "FaCLg4H0BU0"
            code= filename[filename.find('[')+1:filename.find(']')]
            #url= 'https://www.youtube.com/watch?v='+code
            url= f'https://youtu.be/{code}'

            txtS= f2.read()
            # remove the all time stamps in txtS
            #txtS0= '\n'.join([i for i in txtS.split('\n') if not i.startswith('00:')])
            txtS0= '\n'.join([i for i in txtS.split('\n') if ' --> ' not in i])

            f.write(f'file{n:04d}: {os.path.basename(i)}\n')
            f.write(f'url{n:04d}: {url}\n')
            f.write(txtS)
            f.write('\n\n')

            f0.write(f'file{n:04d}: {os.path.basename(i)}\n')
            f0.write(f'url{n:04d}: {url}\n')
            f0.write(txtS0)
            f0.write('\n\n')

            # count the number of chinese characters in txtS
            #print(len([i for i in txtS if '\u4e00' <= i <= '\u9fff']))
            numCh += len([i for i in txtS if '\u4e00' <= i <= '\u9fff'])
 


print(f'{numCh= }')



