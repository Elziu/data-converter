import os
from arg_parser import parse_args
from json_handler import read_json, write_json
from xml_yaml_handler import read_xml, write_xml, read_yaml, write_yaml

def convert_file(input_file, output_file):
    _, input_ext = os.path.splitext(input_file)
    _, output_ext = os.path.splitext(output_file)

    if input_ext == '.json':
        data = read_json(input_file)
    elif input_ext == '.xml':
        data = read_xml(input_file)
    elif input_ext in ['.yaml', '.yml']:
        data = read_yaml(input_file)
    else:
        raise ValueError("Unsupported input file format")

    if output_ext == '.json':
        write_json(data, output_file)
    elif output_ext == '.xml':
        write_xml(data, output_file)
    elif output_ext in ['.yaml', '.yml']:
        write_yaml(data, output_file)
    else:
        raise ValueError("Unsupported output file format")

if __name__ == "__main__":
    args = parse_args()
    convert_file(args.input_file, args.output_file)