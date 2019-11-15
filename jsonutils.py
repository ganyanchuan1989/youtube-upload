import json
import codecs

def getData():
    with open("./share-url.json", 'r') as load_f:
      data_dict = json.load(load_f)
      return data_dict
    return {}
