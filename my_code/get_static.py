import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm


class GetGlobalStatic:
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_data(self, url):
        res = requests.get(url)
        data = res.content.decode()
        return data

    def analysis_today(self, data):
        soup = BeautifulSoup(data, 'lxml')
        script = soup.find(id='getListByCountryTypeService2true')
        text = script.contents[0]
        json_str = re.findall(r'\[.+\]', text)[0]
        today_data = json.loads(json_str)
        return today_data

    def analysis_eight_mouth(self):
        lst = []
        with open('today_analysis_of_country.json', encoding='utf-8') as fp:
            data = json.load(fp)
        for i in tqdm(data, '采集八月以来各国疫情信息：'):
            url = i['statisticsData']
            day_data = json.loads(self.get_data(url))['data']
            for x in day_data:
                x['provinceName'] = i['provinceName']
        lst.append(day_data)
        self.save_to_file(lst, r'eight_of_country.json')

    def save_to_file(self, today_data, path):
        with open(path, 'w', encoding='utf-8') as fp:
            json.dump(today_data, fp, ensure_ascii=False)

    def start(self):
        data = self.get_data(self.home_url)
        today_data = self.analysis_today(data)
        self.save_to_file(today_data, r'today_analysis_of_country.json')


class GetAreaStatic:
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_data(self, url):
        res = requests.get(url)
        data = res.content.decode()
        return data

    def analysis_today(self, data):
        soup = BeautifulSoup(data, 'lxml')
        script = soup.find(id='getAreaStat')
        text = script.contents[0]
        json_str = re.findall(r'\[.+\]', text)[0]
        today_data = json.loads(json_str)
        return today_data

    def analysis_eight_mouth(self):
        lst = []
        with open('today_analysis_of_province.json', encoding='utf-8') as fp:
            data = json.load(fp)
        for i in tqdm(data, '采集八月以来各省疫情信息：'):
            url = i['statisticsData']
            day_data = json.loads(self.get_data(url))['data']
            for x in day_data:
                x['provinceName'] = i['provinceName']
        lst.append(day_data)
        self.save_to_file(lst, r'eight_of_province.json')

    def save_to_file(self, today_data, path):
        with open(path, 'w', encoding='utf-8') as fp:
            json.dump(today_data, fp, ensure_ascii=False)

    def start(self):
        data = self.get_data(self.home_url)
        today_data = self.analysis_today(data)
        self.save_to_file(today_data, r'today_analysis_of_province.json')

