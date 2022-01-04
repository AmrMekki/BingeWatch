import json
import csv

for i in range(1980,2016): 
    with open("groundtruth//" + str(i) + ".txt", "r") as json_file:
            string = json_file.read()
            json_object = string.split('}')
            json_object[len(json_object) - 1] += "}"
            del json_object[-1]
            json_objects = []
            for x in json_object:
                x = x + "}"
                x = x.replace("ObjectId(", "")
                x = x.replace("\n", "")
                x = x.replace("),", ",")
                json_objects.append(x)
            json_list = []
            for x in json_objects:
                    json_list.append(json.loads(x))             
            data_file = open("csvData//"+str(i) + ".csv", 'w', newline='')
            csv_writer = csv.writer(data_file)
            count = 0
            for data in json_list:
                if count == 0:
                    header = data.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(data.values())
            data_file.close()