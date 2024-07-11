import json
from arg_parser import parse_args

def read_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
            return None
    return data

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    args = parse_args()
    data = read_json(args.input_file)
    if data is not None:
        print(f"Data: {data}")