import csv
import json

def main():
    with open("train.csv", 'r') as f:
        train = csv.reader(f)
        count = 0
        output = {}
        output['id'] = ['id']
        output['raw_address'] = ['raw_address']
        output['POI'] = ['POI']
        output['street'] = ['street']
        added = {}
        add = {}
        result = []
        res = []
        direct = {}
        direct['tokens'] = []
        direct['labels'] = []
        arr = {}
        arr['tokens'] = []
        arr['labels'] = []
        output['tokens'] = ['tokens']
        output['labels'] = ['labels']
        for row in train:
            if row[2] == "POI/street":
                continue
            addr = row[1].split(" ")
            temp = row[2].split("/")
            if temp[0] != "":
                tmp = temp[0].split(" ")
                poi = {}
                poi['tokens'] = []
                poi['labels'] = []
                for word in addr:
                    for char in tmp:
                        if word in char and word not in added:
                            added[word] = char
                            direct['tokens'].append(word)
                            direct['labels'].append(char)
                            poi['tokens'].append(word)
                            poi['labels'].append(char)
                if len(poi['tokens']) > 0:
                    result.append(poi)
            output['POI'].append(temp[0])
            if temp[1] != "":
                tmp = temp[1].split(" ")
                street = {}
                street['tokens'] = []
                street['labels'] = []
                for word in addr:
                    for char in tmp:
                        if len(word) > 1 and word in char and word not in add:
                            add[word] = char
                            arr['tokens'].append(word)
                            arr['labels'].append(char)
                            street['tokens'].append(word)
                            street['labels'].append(char)
                if len(street['tokens']) > 0:
                    res.append(street)
            output['street'].append(temp[1])
            output['id'].append(row[0])
            output['raw_address'].append(row[1])
            # if count == 10:
            #     break
            # print(row)
            # count += 1
    # with open('split.csv', mode='w') as test_file:
    #     test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #     for i in range(len(output['id'])):
    #         test_writer.writerow([output['id'][i], output['raw_address'][i], output['POI'][i], output['street'][i]])        
    with open('poi.json', 'w') as fp:
        json.dump(added, fp)
    with open('street.json', 'w') as fp:
        json.dump(add, fp)

if __name__ == "__main__":
    main()