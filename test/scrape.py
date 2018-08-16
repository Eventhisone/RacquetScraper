from bs4 import BeautifulSoup
from racquet import Racquet

racquetDataFile = open("asics.txt", "w")

asics_html = open("asics-patterns.html", 'r')

soup = BeautifulSoup(asics_html, 'html.parser')
myracquet = Racquet(1, 2, 3, 4, 5, 6, 7, 8)

# All the data we want is in a between <basefont></basefont> tags
data = soup.find_all('basefont')
racuqetDataArray = []
for index in range(len(data)):
    # The first 2 elemenst of the data array contain information we don't want
    if(index > 1):
        racuqetDataArray.append(data[index].contents[0])

print(len(racuqetDataArray))

racquetArray = []
index = 0
while index <= len(racuqetDataArray):
    currRacquet = Racquet(racuqetDataArray[index], racuqetDataArray[index + 1], racuqetDataArray[index + 2], racuqetDataArray[index + 3], racuqetDataArray[index + 4], racuqetDataArray[index + 5], racuqetDataArray[index + 6], racuqetDataArray[index + 7])
    racquetArray.append(currRacquet)
    index += 8

print(racquetArray)
#racquetDataFile.close()