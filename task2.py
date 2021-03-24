import requests
import bs4

def get_data(debug = False):
    host = "https://ru.wikipedia.org/"
    counter = {}
    letter  = chr(1040)
    next_page = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"

    while (True):
        data = requests.get(url=next_page)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        next_page = host + soup.find(lambda tag:tag.name=="a" and "Следующая страница" in tag.text)['href']
        if debug:
            print(next_page)
        letter = soup.select(".mw-category-group h3")[0].text
        if debug:
            print(letter)
        if (ord(letter) == 65):
            break
        if letter not in counter:
            counter[letter] = 0
        animals = soup.select(".mw-category-group ul li")
        counter[letter] += len(animals)
        if debug:
            print(counter)
    return counter

def print_data(data):
    for k in data:
        print(f"{k}:{data[k]}")

def main():
    data = get_data()
    print_data(data)


main()
