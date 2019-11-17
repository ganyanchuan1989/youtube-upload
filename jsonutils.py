import json
import codecs


def getData():
    with open("./share-url.json", 'r') as load_f:
        data_dict = json.load(load_f)
        return data_dict
    return {}


def saveData(data):
    print(json.dumps(data))
    with codecs.open('./share-url.json', "w", "utf-8") as data_f:
        data_f.write(json.dumps(data))
