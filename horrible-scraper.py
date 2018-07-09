from os import listdir
import bs4
resolutions = ['360p', '480p','720p', '1080p']
path = '/home/curt/Downloads/'
horrible_pages = [page[:-5] for page in listdir(path) if page.endswith('html')]


def pull_site(page):
    with open(path + page + '.html', 'rt', encoding='latin1') as page:
        raw_site_page = page.read()
    return raw_site_page


def scrape(site, res):
    magnet_list = []
    soup = bs4.BeautifulSoup(site, 'html.parser')
    release_links_list = soup.select(".rls-link")

    for headers in reversed(release_links_list):
        print(headers)
        if res in headers.getText():
            for mag in headers.find_all('a', href=True):
                magnet = mag['href'].replace('&amp;', '&')
                magnet_list.append(magnet)
                break
    return magnet_list


if __name__ == "__main__":

    for page in horrible_pages:
        site = pull_site(page)

        with open(path + page + ".txt", "w") as text_file:
            for resolution in resolutions:
                magnets = scrape(site, resolution)
                text_file.write(resolution + '\n')
                for magnet in magnets:
                    text_file.write(magnet + '\n')
                    print(magnet)