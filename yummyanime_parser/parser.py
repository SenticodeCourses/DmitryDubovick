import requests
from bs4 import BeautifulSoup


def get_html(url, header):
    r = requests.get(url, headers = header)
    return r.content


def get_all_categories_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    columns = soup.find_all('div', class_='category-col')
    uls = []
    for column in columns:
        uls.append(column.find('ul', class_='category-list'))
    lies = []
    for ul in uls:
        lies.extend(ul.find_all('li'))
        links = []
    for li in lies:
        link = 'https://yummyanime.com' + li.find('a').get('href')
        links.append(link)
    return links


def get_anime_links(url, header):
    html = get_html(url, header)
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find('ul', class_='pagination'):
        navigation_buttons = soup.find('ul', class_='pagination').find_all('li')
        number_of_pages = int(navigation_buttons[-2].find('a').get('href').split('=')[-1])
    else:
        number_of_pages = 1

    for page in range(1, number_of_pages + 1):
        active_url = url + '?page=' + str(page)
        html = get_html(active_url, header)
        soup = BeautifulSoup(html, 'html.parser')
        imgs = soup.find_all('div', class_='anime-column')
        anime_links = []
        for img in imgs:
            link = 'https://yummyanime.com' + img.find('a', class_='image-block').get('href')
            anime_links.append(link)
        return anime_links


def find_cool_anime(url, header):
    html = get_html(url, header)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        rating = float(soup.find('span', class_='main-rating').text)
    except:
        rating = 0
    if rating < 9:
        pass
    else:
        name = soup.find('h1').text
        return name, rating


def write_into_file(anime_name, anime_rating):
    my_file = open('best_anime_list.txt', 'a')
    my_file.write(anime_name + ' : ' + str(anime_rating)+'\n')
    my_file.close()


def main():
    url = 'https://yummyanime.com/catalog'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    all_categories_links = get_all_categories_links(get_html(url, header))
    print('find all categories')
    print(all_categories_links)
    all_anime = []
    for category in all_categories_links:
        anime_of_this_category = get_anime_links(category, header)
        print('find anime of 1 category',category)
        all_anime.extend(anime_of_this_category)
        print(anime_of_this_category)
    cool_anime = {}
    for anime in all_anime:
        if find_cool_anime(anime, header):
            name, rating = (find_cool_anime(anime, header))
            #cool_anime[name] = rating
            print('add anime to coolanime')
            write_into_file(name,rating)
    # for anime in sorted(cool_anime.items(), key=lambda item: item[1]):
    #     write_into_file(anime)



main()