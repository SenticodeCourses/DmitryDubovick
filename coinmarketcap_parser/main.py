import getting_data as gd
import making_file as mk
from multiprocessing import Pool


def main():
    url = 'https://coinmarketcap.com/all/views/all'
    all_links = gd.gl.get_all_links(gd.gl.get_html(url))
    # with Pool(40) as po:
    #     po.map(get_page_data, all_links)
    for link in all_links:
        data = gd.get_page_data(link)
        mk.write_into_file(data)

main()