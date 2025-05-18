import argparse
import json

def generate_diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    keys = sorted(set(data1.keys()).union(set(data2.keys())))

    diff = []
    for key in keys:
        if key not in data2:
            diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")
        else:
            diff.append(f"    {key}: {data1[key]}")

    return "{\n" + "\n".join(diff) + "\n}"

def get_gendiff_help():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-f', '--format', help='set format of output', default='text')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)