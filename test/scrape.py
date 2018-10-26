from bs4 import BeautifulSoup
from racquet import Racquet
import os

def scrape(patternFile, outputFile, manufacturer):
    """Scrape Racquet specs from patternfile and save them in outputFile"""
    
    #racquetDataFile = open("asics.txt", "w")
    racquetDataFile = open(outputFile, "w")

    #asics_html = open("asics-patterns.html", 'r')
    patternHTML = open(patternFile, 'r')

    soup = BeautifulSoup(patternHTML, 'html.parser')
    #myracquet = Racquet(1, 2, 3, 4, 5, 6, 7, 8)

    data = soup.find_all('td')
    racuqetDataArray = []
    racquetDataFile.write(str(manufacturer) + " = [[")
    for index in range(len(data)):
        # The first 2 elemenst of the data array contain information we don't want
        if(index > 19):
            spec = str(data[index]).split("/")
            spec = spec[1][1:-1]
            # print(spec)
            racquetDataFile.write("\"")
            racquetDataFile.write(spec)
            racquetDataFile.write("\"")
            if index > len(data) -2:
                # The last spec is a blank line and we don't want it
                break
            if (index - 19) % 8 == 0:
                # Separate the lists every eight elements
                # print("---")
                racquetDataFile.write("],[")
            else:
                racquetDataFile.write(", ")

    racquetDataFile.write("]]")

    racquetDataFile.close()

def test():
    """Test scrape() on asics data"""
    
    patterndir = "../patterns"
    outputdir = "../specs"

    for subdir, dirs, files in os.walk(patterndir):
        for file in files:
            #print(file)

            patternFile = "../patterns/Asics Tennis Stringing Patterns.html" #"Babolat Tennis Stringing Patterns.html"
            #outputFile = "babolat.txt" #"asics.txt"
            slug = file.split()[0:2]
            outputFileName = "-".join(slug).lower()
            #manufacturer = patternFile.split()[0].lower()
            outputFile = "../specs/" + outputFileName + ".txt"

            print("scraping: " + str(file))
            scrape(patternFile, outputFile, outputFileName)
    print("done!")

if __name__ == '__main__':
    test()