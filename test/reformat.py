import os

def reformat():
    
    for subdir, dirs, files in os.walk("../specs/"):
        for file in files:
            manufacturer = {}
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
                print(data[0])
                racquet_obj = {
                    "name": data[0],
                    "tension": fix_tension_range(data[1]),
                    "length": fix_lengths(data[2]),
                    "pattern": fix_dimensions(data[3]),
                    "skip_m": data[4],
                    "tie_m": data[5],
                    "start_c": data[6],
                    "tie_c": data[7]
                }
                manufacturer[racquet_obj['name']] = racquet_obj
            fo.write(str(manufacturer) + "\n")
            f.close()
            fo.close()
    #print(manufacturer)

def fix_tension_range(trange):
    upper = trange[:2]
    lower = trange[-2:]
    
    tension_range = {
        "upper": upper,
        "lower": lower
    }

    return tension_range

def fix_lengths(lens):
    #print(lens)
    length_mains = lens[:2]
    length_crosses = lens[-4:-2]

    len_mains_crosses = {
        "length_mains": length_mains,
        "length_crosses": length_crosses
    }

    return len_mains_crosses

def fix_dimensions(dims):
    num_mains = dims[:2]
    num_crosses = dims[-3:-1]

    dims_mains_and_crosses = {
        "num_mains": num_mains,
        "num_crosses": num_crosses
    }

    return dims_mains_and_crosses


if __name__ == '__main__':
    reformat()