#!/usr/bin/env python3
import sys
import json
import csv

BASE_URL = 'https://link.springer.com/content/pdf'

def obj_from_row(row):
    obj = {'title': row[0]}
    obj.update(doi=row[5])
    obj.update(authors=row[6])
    obj.update(url='{}/{}.pdf'.format(BASE_URL, row[5]))
    return obj

def list_from_file(filename):
    objects = []
    file = open(filename)
    _csv = csv.reader(file)
    for line in _csv:
        obj = obj_from_row(line)
        objects.append(obj)
    file.close()
    return objects

def main(files, output):
    _json = {}
    for name in files:
        # Check if the category exists
        category = name.split('.')[0]
        if category not in _json:
            _json[category] = []
        _json[category] += list_from_file(name)
    file = open(output, 'w+')
    file.write(json.dumps(_json, indent=4))
    file.close()

if __name__ == '__main__':
    main(sys.argv[1:-1], sys.argv[-1])
