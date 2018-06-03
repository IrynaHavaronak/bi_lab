import gzip
import json
import csv
import xml.etree.ElementTree as ET
import yaml


def parse_data(arc):
    with gzip.open(arc, 'rb')as f_gz:
        data = []
        for i in range(27):
            f_gz.readline()
        data.append(list(f_gz.readline().decode('ascii').split('  ')))
        for line in f_gz:
            tmp = list()
            tmp.append("")
            tmp.append(line[6:16].decode('ascii'))
            tmp.append(line[18:24].decode('ascii'))
            tmp.append(line[27:30].decode('ascii'))
            tmp.append(line[32:].decode("cp437"))
            data.append(tmp)
    return data


def data_dict(arc):
    with gzip.open(arc, 'rb')as f_gz:
        data = []
        for i in range(27):
            f_gz.readline()
        keys = list(f_gz.readline().decode('ascii').split('  '))
        for line in f_gz:
            tmp = {}
            for i in keys:
                tmp[i] = ""
            tmp[keys[1]] = line[6:16].decode('ascii')
            tmp[keys[2]] = line[18:24].decode('ascii')
            tmp[keys[3]] = line[27:31].decode('ascii')
            tmp[keys[4]] = line[32:].decode("cp437")
            data.append(tmp)
    return data


def save_as_csv(arc):
    data = parse_data(arc)
    with open(arc[:len(arc)-1-arc[::-1].index('.'):]+".csv", 'w',
              newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(data)


def save_as_json(arc):
    data = data_dict(arc)
    with open(arc[:len(arc)-1-arc[::-1].index('.'):]+".json", 'w') as \
            j_file:
        json.dump(data, j_file)


def save_as_xml(arc):
    data = parse_data(arc)
    root = ET.Element("root")
    j = 0
    for i in data[1:]:
        doc = ET.SubElement(root, "doc" + str(j))
        j += 1
        ET.SubElement(doc, "field1", name=data[0][0]).text = i[0]
        ET.SubElement(doc, "field2", name=data[0][1]).text = i[1]
        ET.SubElement(doc, "field3", name=data[0][2]).text = i[2]
        ET.SubElement(doc, "field4", name=data[0][3]).text = i[3]
        ET.SubElement(doc, "field5", name=data[0][4]).text = i[4]

    tree = ET.ElementTree(root)
    tree.write(arc[:len(arc)-1-arc[::-1].index('.'):]+".xml")


def save_as_yaml(arc):
    data = data_dict(arc)
    with open(arc[:len(arc) - 1 - arc[::-1].index('.'):] + ".yaml", 'w') as \
            y_file:
        yaml.dump(data, y_file)

