import os

def reformat():
    manufacturer = {}
    for subdir, dirs, files in os.walk("../specs/"):
        for file in files:
            fname = "../specs/" + str(file)
            foname = "../specs_json/" + str(file)[:-4] + ".json"
            f = open(fname, "r")
            fo = open(foname, "w")
            for line in f:
                data = line.split("#")
                #print('Name: {0}, Tension: {1}, Length: {2}, Pattern: {3}, Skip M: {4}, Tie M: {5}, Start C: {6}, Tie C: {7}'.format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
                #name = data[0]
                #tension = data[1]
                #length = data[2]
                #pattern = data[3]
                #skip_m = data[4]
                #tie_m = data[5]
                #start_c = data[6]
                #tie_c = data[7]
                racquet_obj = {
                    "name": data[0],
                    "tension": data[1],
                    "length": data[2],
                    "pattern": data[3],
                    "skip_m": data[4],
                    "tie_m": data[5],
                    "start_c": data[6],
                    "tie_c": data[7]
                }
                manufacturer[racquet_obj['name']] = racquet_obj
            fo.write(str(manufacturer) + "\n")
            f.close()
            fo.close()
    print(manufacturer)