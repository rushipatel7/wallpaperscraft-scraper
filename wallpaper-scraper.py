import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

class wallicraftScrape(object):
    def __init__(self, baseUrl, category, resolution):
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }
        self.baseUrl = baseUrl
        self.category = category
        self.resolution = resolution
    
    def initlization(self):
        self.count = 0
        self.sub_count = 0
        self.img_link_list = []
        self.img_original_list = []

    def export_CSV(self):
        df = pd.DataFrame(self.img_original_list, columns=['Image Links'])
        df.to_csv(self.category + '-' + self.resolution + '.csv', encoding='utf-8', header=True, index=False)

    def scrapeData(self):
        self.initlization()
        try:
            for i in  tqdm(range(1,5), desc='Loading...'):
                r = requests.get(f"https://wallpaperscraft.com/catalog/{self.category}/{self.resolution}/page{i}", headers=self.headers)
                soup = BeautifulSoup(r.content, 'lxml')
                self.img_link = soup.find_all('a', {'class' : 'wallpapers__link'})
                for i in self.img_link:
                    self.count +=1
                    self.img_link_list.append(self.baseUrl + i['href'])
                for i in self.img_link_list:
                    r = requests.get(url=i, headers=self.headers)
                    soup = BeautifulSoup(r.content, 'lxml')
                    self.img = soup.find_all('img', {'class' : 'wallpaper__image'})
                    for i in self.img:
                        format_img_last_links = i['src']
                        self.img_original_list.append(format_img_last_links)
                        self.export_CSV()
        except Exception as e:
            print("There is error occured ...!", e)

if __name__ == '__main__':
    baseUrl = "https://wallpaperscraft.com"
    category = "cars"
    resolution = "1280x1024"
    class_wallicraftScrape = wallicraftScrape(baseUrl=baseUrl, category=category, resolution=resolution)
    class_wallicraftScrape.scrapeData()
