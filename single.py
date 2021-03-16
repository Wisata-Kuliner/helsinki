import csv
import coremltools

def main():
    # print("test")
    with open("test.csv", 'r') as f:
        test = csv.reader(f)
        model = coremltools.models.MLModel('POITagger.mlmodel')
        # print(model)
        count = 0
        for row in test:
            if row[1] == 'raw_address':
                continue
            # print(row)
            # count += 1
            # if count == 10:
            #     break
            temp = row[1].split(" ")
            for word in temp:
                # print(word)
                result = model.predict({"text": word})
                print(result)
                # if len(result['labels']) == 0:
                #     print(word)

if __name__ == "__main__":
    main()