import os
import sys 
import argparse

os.chdir('/Users/nishantdev/Desktop/Stuff/CodingChallenges/OwnCatTool')

def extract_content(file_name, number_lines=False, number_non_blank_lines=False):
    if file_name is None or file_name == '-':
        content = sys.stdin.read()
        if content == '\n':
            raise ValueError("No input provided")
    else:
        try:
            with open(file_name, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            return (f"No such File {file_name} exists")
    
    if number_lines or file_name == '-':
        return '\n'.join(f'{i} {line}' for i, line in enumerate(content.splitlines(), start=1))
    elif number_non_blank_lines:
        line_number = 1
        numbered_lines = []
        for line in content.splitlines():
            if line.strip():
                numbered_lines.append(f'{line_number} {line}')
                line_number += 1
            else:
                numbered_lines.append(line)
        return '\n'.join(numbered_lines)
    else:
        return content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Own Cat Tool')
    parser.add_argument("files", nargs='*', help="the files to read")
    parser.add_argument("-n", action='store_true', help="number all output lines")
    parser.add_argument("-b", action='store_true', help="number non-blank output lines")
    args = parser.parse_args()

    for file in args.files or [None]:
        print(extract_content(file, args.n, args.b))