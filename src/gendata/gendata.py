import datetime
import json

#datetime_str = '09/19/18 13:55:26'
#datetime_str = '2021/06/01 00:00:00'

#datetime_object = datetime.datetime.strptime(datetime_str, '%Y/%m/%d %H:%M:%S')

def json_print(array_data):
    print("const jsonData = `")
    print(json.dumps(array_data, indent=4))
    print("`;")
    print("export const objData = JSON.parse(jsonData);")

def main():
    datetime_str = '2021/06/14 00:00:00'
    start_dt = datetime.datetime.strptime(datetime_str, '%Y/%m/%d %H:%M:%S')

    array_data = []

    id  = 1000000
    max = 30
    for x in range(max):
        #print(x)
        start_dt = start_dt + datetime.timedelta(days=1)
        end_dt = start_dt + datetime.timedelta(days=7)
        id += 1
        #print(start_dt.strftime("%Y/%m/%d %H:%M"))
        #print(end_dt.strftime("%Y/%m/%d %H:%M"))
        #print(id)
        bars = [
                {
                 "beginDate"      : start_dt.strftime("%Y/%m/%d %H:%M"), 
                 "endDate"        : end_dt.strftime("%Y/%m/%d %H:%M"), 
                 "ganttBarConfig" : {
                                       "id"    : id,
                                       "label" : "I'm in a bundle",
                                       "hasHandles": "true" , 
                                       "style" : {
                                         "background": "magenta"
                                       }
                                    }
                }
               ]
        record = {
                   "label" : "rows " + str(x),
                   "bars"  : bars
                }
        #print(record)
        #print(json.dumps(record, indent=4))
        array_data.append(record)

    json_print(array_data)


if __name__ == "__main__":
    main()
