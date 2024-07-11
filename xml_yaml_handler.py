import xml.etree.ElementTree as ET
import yaml

def read_xml(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

def write_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)