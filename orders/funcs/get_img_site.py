from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
}


def get_img(url):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        imgs = soup.findAll("img")

        for img in imgs:
            print(img["src"])
