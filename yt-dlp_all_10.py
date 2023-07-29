#%%
import os
import glob
import tqdm

cmd00=   'yt-dlp '

## 把下行 unmark 即可正式 下載 影片，
cmd00 += '--no-simulate '

tgt=  'tgt'

'''
六祖壇經 台語 常照法師 全183集，大慈山彌勒菩薩道場
'''
#url=  'https://youtube.com/playlist?list=PLhArlNBYwwRHaclJmGVPDUtrFkm9BwbJp' #


# 法王講堂/禪宗類 -- 六祖壇經
# url=  'https://youtube.com/playlist?list=PLOuYmXIKxWpZkoHasJApVARfDVHAH7FIH'  

'''
【機器學習 2023】(生成式 AI)
Hung-yi Lee
'''
#url= 'https://youtube.com/playlist?list=PLJV_el3uVTsOePyfmkfivYZ7Rqr2nMk3W'
#url= 'https://www.youtube.com/@HungyiLeeNTU/playlists'


'''
09~110年慧度法師講解《六祖壇經》
古嚴寺
70 部影片
'''
#url= 'https://youtube.com/playlist?list=PLwEV3aNvNd3wcdDQOTmhkCIkEQSSZarng'

url= 'https://youtu.be/BZmvw8KbyzA' #打禪七、佛七的意義

'''
柯文哲 
@Team__KP72.4萬位訂閱者760 部影片
改變成真，持續發生
'''
url= 'https://www.youtube.com/@Team__KP/videos'
#url= 'https://www.youtube.com/@Team__KP/playlists'


'''
賴清德 
@Chingte_Taiwan6.04萬位訂閱者96 部影片
'''
url= 'https://www.youtube.com/@Chingte_Taiwan/videos'
#url= 'https://www.youtube.com/@Chingte_Taiwan/playlists'

'''
侯友宜 houyuih@houyuih9850位訂閱者809 部影片
站在第一線，打造安居樂業新北市
'''
url= 'https://www.youtube.com/@houyuih/videos'
#url= 'https://www.youtube.com/@houyuih/playlists'


'''
蔡英文 
@ingwen83142.8萬位訂閱者493 部影片
我是蔡英文，這裡是我放影片的地方，歡迎大家一起來看！
'''
url= 'https://www.youtube.com/@ingwen831/videos'
#url= 'https://www.youtube.com/@ingwen831/playlists'

urlList= [
    'https://www.youtube.com/@ingwen831/videos',
    'https://www.youtube.com/@Team__KP/videos',
    'https://www.youtube.com/@Chingte_Taiwan/videos',
    'https://www.youtube.com/@houyuih/videos'
]

#url= urlList[0]

'''
09~110年慧度法師講解《六祖壇經》
古嚴寺
70 部影片
'''
#url= 'https://youtube.com/playlist?list=PLwEV3aNvNd3wcdDQOTmhkCIkEQSSZarng'

urlList= [
    'https://youtube.com/playlist?list=PLwEV3aNvNd3wcdDQOTmhkCIkEQSSZarng'
]

for url in urlList:

    print(f'{url= }')

    items= '1:1000:1'

    cmd00 += f'--paths {tgt} '
    cmd00 += f'--playlist-items {items} '

    cmd00 += '--format wv[ext=mp4]+ba[ext=m4a] '
    cmd00 += '--print "%(n_entries)04d, %(playlist_index-1)04d, %(duration)05d, [%(id)s], <%(filename)s>"  '
    cmd00 += '-o "%(playlist)s/%(playlist)s-%(playlist_index-1)04d-%(title)s [%(id)s].%(ext)s" '

    cmd00 += '--write-srt --convert-subs srt '
    cmd00 += '--write-auto-sub '
    #cmd00 += '--sub-lang zh-Hant '

    cmd00 += f'{url} '
    cmd00 += f'1>{tgt}.1.txt 2>{tgt}.2.txt '

    print(cmd00)

    import subprocess
    subprocess.run(
        cmd00,
        encoding='utf-8', 
        shell=  True,
        stdout= True
        )
