import requests
import json
# from bs4 import BeautifulSoup


def get_html(url, header):
    r = requests.get(url, headers=header)
    return r.text

def main():
    while True:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        url = input('http://localhost:8080/')
        url = 'http://localhost:8080/' + url
        try:
            html = get_html(url, header)
            my_collection = json.loads(html)
            if type(my_collection) is dict:
                for key in my_collection:
                    print(key, ': ', my_collection[key])
            else:
                for element in my_collection:
                    print(element)
        except:
            print('Wrong URL')
        # soup = BeautifulSoup(html, 'html.parser')
        # try:
        #     result = soup.find('pre')
        #     print(result)
        # except:
        #     print('Wrong URL')

main()