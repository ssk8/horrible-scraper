from os import listdir
import bs4
resolutions = ['360p', '480p','720p', '1080p']
path = '/home/curt/Downloads/'


def open_page(page):
    with open(path + page + '.html', 'rt', encoding='latin1') as page:
        raw_site_page = page.read()
    return raw_site_page


def scrape(site, res):
    magnet_list = []
    soup = bs4.BeautifulSoup(site, 'html.parser')
    release_links_list = soup.select(".rls-link")

    for headers in reversed(release_links_list):
        if res in headers.getText():
            magnet_list.append(headers.find_all('a', href=True)[0]['href'].replace('&amp;', '&'))
    return magnet_list


def create_mag_file(page):
    site = open_page(page)
    with open(path + page + ".txt", "w") as text_file:
        for resolution in resolutions:
            magnets = scrape(site, resolution)
            text_file.write(f'\n{20*"-"} {resolution} {20*"-"}\n \n')
            for magnet in magnets:
                text_file.write('   ' + magnet + '\n')
                print(magnet)


def main():
    for page in [page[:-5] for page in listdir(path) if page.endswith('html')]:
        create_mag_file(page)


if __name__ == "__main__":
    main()