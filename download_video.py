#We are going to download all the video lectures of GeeksforGeeks
import requests
from bs4 import BeautifulSoup

archive_url="http://www-personal.umich.edu/~csev/books/py4inf/media/"
#Archive url directory of 'GeeksforGeeks' 

def get_video_links():
    r=requests.get(archive_url)
    soup= BeautifulSoup(r.content,'html.parser')
    links=soup.findAll('a')
    video_links=[archive_url+link['href'] for link in links if link['href'].endswith('mp4')]
    return video_links

def download_video_series(video_links):
    for link in video_links:
        file_name=link.split('/')[-1]
        print ('Downloading File: ',file_name)
        r=requests.get(link,stream=True)
        with open(file_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
        #f.close
        print(file_name,'downloaded !\n')
    print('All videos downloaded!')
    return

if __name__=="__main__":
    video_links=get_video_links()
    download_video_series(video_links)