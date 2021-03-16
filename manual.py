import json
import csv

def main():
    arr = {}
    arr['id'] = ['id']
    arr['output'] = ['POI/street']
    with open("poi.json", 'r') as f:
        poi = json.load(f)
        with open("street.json", "r") as v:
            street = json.load(v)
            with open("test.csv", 'r') as u:
                test = csv.reader(u)
                for row in test:
                    # print(row)
                    # break
                    result = ""
                    if row[1] == 'raw_address':
                        continue
                    temp = row[1].split(" ")
                    flag = False
                    already = []
                    for word in temp:
                        if word in poi:
                            if flag != False:
                                result += " "
                            result += poi[word]
                            already.append(word)
                            flag = True
                        # else:
                        #     result += word
                        #     already.append(word)
                    result += "/"
                    flag = False
                    for word in temp:
                        if word not in already:
                            if flag != False:
                                result += " "
                            if word in street:
                                result += street[word]
                            else:
                                result += word
                            flag = True
                    arr['id'].append(row[0])
                    arr['output'].append(result)
                
                
        # for k,v in poi.items():
        #     print(k, v)
        #     break
    with open('result.csv', mode='w') as test_file:
        test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(arr['id'])):
            test_writer.writerow([arr['id'][i], arr['output'][i]])


if __name__ == "__main__":
    main()