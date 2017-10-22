import requests
img_url="https://www.cesarsway.com/sites/newcesarsway/files/styles/large_article_preview/public/Natural-Dog-Law-2-To-dogs%2C-energy-is-everything.jpg?itok=Z-ujUOUr"
r=requests.get(img_url)
with open("image.jpeg",'wb') as f:
    f.write(r.content)