from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin
from datetime import date

url = "http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016.html"

today = date.today()

folder_location = f'./PDFs/{today}/{url.split(".")[1]}'

if not os.path.exists(folder_location):
    os.makedirs(folder_location)

res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")     

for link in soup.select("a[href$='.pdf']"):
    file = link['href'].split('/')[-1]
    filename = os.path.join(folder_location,file)
    print("Downloading " + file)
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)
    print("Downloaded " + file)