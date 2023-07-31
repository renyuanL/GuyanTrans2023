import os
import glob
import tqdm


mp4Path= 'srt_維摩詰所說經'
mp4Path= 'srt_六祖壇經'
mp4Path= 'srt_112年7月阿彌陀佛紐涅七日禪'

# get mp4Path from command line
import sys
if len(sys.argv) > 1:
    mp4Path= sys.argv[1]


fList = glob.glob(f'{mp4Path}/*.srt')
fList+= glob.glob(f'{mp4Path}/*/*.srt')
fList+= glob.glob(f'{mp4Path}/*/*/*.srt')
fList+= glob.glob(f'{mp4Path}/*/*/*/*.srt')

# concat all srt files
# keep their filename as a independent line
# using \n\n to separate each file

numCh= 0
nL= []
tL= []
with (open(f'_{mp4Path}_.srt.txt', 'w', encoding='utf-8') as f,
      open(f'_{mp4Path}_.srt0.txt', 'w', encoding='utf-8') as f0):
    for n,i in tqdm.tqdm(enumerate(fList)):
        with open(i, 'r', encoding='utf-8') as f2:
            filename= os.path.basename(i)
            nL += [(n, filename)]
            
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

            # get the last time stamp in txtS
            lastTS= txtS.split('\n')[-4].split(' --> ')[-1]
            #print(f'{lastTS= }')
            lastTS= lastTS.split(':')
            hr= int(lastTS[0])
            min= int(lastTS[1])
            sec= int(lastTS[2].split(',')[0]) + int(lastTS[2].split(',')[1])*.001
            t = hr*3600 + min*60 + sec
            tL += [t]


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
 

#print(f'{nL= }')
for n,f in nL:
    print(f'{n= }, {f= }')

print(f'{len(nL)= } files')

#print(f'{tL= }')
#print(f'{sum(tL)= :.3f} seconds')
print(f'{sum(tL)/3600= :.3f} hours')

#print(f'{numCh= } chars')
# print numCh using large number format
print(f'{numCh= :,} chars')




