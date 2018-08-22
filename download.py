import argparse
import requests
import urllib
import os

from bs4 import BeautifulSoup


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download an issue on OpenEdition')
    parser.add_argument('-l', type=str, help='URL of an issue')
    parser.add_argument('-d', type=str, help='Download destination')
    args = parser.parse_args()

    data = requests.get(args.l)
    soup = BeautifulSoup(data.text, 'lxml')

    if os.path.isdir(args.d):
        try:
            # Retrieve magazine title
            title = soup.find('a', {'title': 'Accueil'}).text

            # Retrieve year and number issue
            issue = soup.find('span', {'class': 'number'}).text.split('|')
            n_issue = issue[0].strip()
            y_issue = issue[1].strip()

        except Exception:
            print('[ + ] Their might be something wrong with the issue\'s URL')
            exit()

        # Get all articles and authors
        articles = []
        ul = soup.find('ul', {'class': 'summary'})
        for li in ul.find_all('li'):
            if 'publications' not in li['class']:

                # Get article infos
                author = li.find('div', {'class': 'author'}).text.strip()
                title = li.find('div', {'class': 'title'})
                url = args.l + '/' + title.findChildren()[0]['href'].strip()

                # Clean url
                url = url.split('/')
                url[-2] = 'pdf'
                url = '/'.join(url)

                # Clean title
                title = title.text
                title = title[:title.find('[')].strip()

                articles.append({'title': title, 'author': author, 'url': url})

        # Dowload all articles of the issue
        for a in articles[1:]:
            print(a)
            filename = '[{y} - {a}] {t}.pdf'.format(y=y_issue,
                                                    a=a['author'],
                                                    t=a['title'])
            filename = args.d + '/' + filename

            # Dowload pdf file
            with open(filename, 'wb') as f:
                response = urllib.request.urlopen(a['url'])
                f.write(response.read())

    else:
        print('[ ! ] Enter correct directory path to store files')
        exit()
