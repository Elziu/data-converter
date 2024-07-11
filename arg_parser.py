import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Data conversion tool")
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    return parser.parse_args()

args = parse_args()
print(f"Input File: {args.input_file}, Output File: {args.output_file}")