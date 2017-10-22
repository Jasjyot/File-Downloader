import requests
file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
r = requests.get(file_url, stream = True)
 
with open("file1.pdf","wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        f.write(chunk)
        