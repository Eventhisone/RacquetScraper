from bs4 import BeautifulSoup
from racquet import Racquet

asics_html = open("asics-patterns.html", 'r')

soup = BeautifulSoup(asics_html, 'html.parser')
myracquet = Racquet(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

data = soup.find_all('td')

print(data[20])
