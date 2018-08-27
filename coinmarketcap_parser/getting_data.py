import getting_links as gl


def get_page_data(url):
    soup = gl.BeautifulSoup(gl.get_html(url), 'html.parser')
    try:
        name = soup.find('h1', class_='details-panel-item--name').find('img').get('alt').strip()
    except:
        name = ''
    try:
        value = soup.find('span', id='quote_price').get('data-usd').strip()
    except:
        value = ''
    data = {'name': name,
            'value': value}
    return data