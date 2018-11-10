from bs4 import BeautifulSoup
import os

def scrape(patternFile, outputFile, manufacturer):
    """Scrape Racquet specs from patternfile and save them in outputFile"""
    
    racquetDataFile = open(outputFile, "w")
    patternHTML = open(patternFile, 'r')

    soup = BeautifulSoup(patternHTML, 'html.parser')

    data = soup.find_all('td')
    
    #racquetDataFile.write(str(manufacturer) + " = [[")
    
    for index in range(len(data)):
        # The first 2 elemenst of the data array contain information we don't want
        if(index > 19):
            spec = str(data[index]).split("/")
            spec = spec[1][1:-1]
            #racquetDataFile.write("\"")
            racquetDataFile.write(spec)
            #racquetDataFile.write("\"")
            if index > len(data) -2:
                # The last spec is a blank line and we don't want it
                break
            if (index - 19) % 8 == 0:
                # Separate the lists every eight elements
                #racquetDataFile.write("],[")
                racquetDataFile.write("\n")
            else:
                racquetDataFile.write("#")

    #racquetDataFile.write("]]")

    racquetDataFile.close()

def test():
    """Test scrape() on asics data"""
    
    patterndir = "../patterns/"
    outputdir = "../specs/"

    for subdir, dirs, files in os.walk(patterndir):
        for file in files:
            patternFile = patterndir + str(file)
            slug = file.split()[0:2]
            outputFileName = "_".join(slug).lower()
            outputFile = outputdir + outputFileName + ".txt"
            
            print("scraping: " + str(file))
            scrape(patternFile, outputFile, outputFileName)
    print("done!")

if __name__ == '__main__':
    test()