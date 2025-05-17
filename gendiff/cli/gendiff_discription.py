import argparse

def get_gendiff_help():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    args = parser.parse_args()
    print(f'Comparing {args.first_file} and {args.second_file}')