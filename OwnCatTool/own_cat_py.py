import os
import sys

os.chdir('/Users/nishantdev/Desktop/Stuff/CodingChallenges/OwnCatTool')
def extract_content(file):
    with open(file) as f:
        return f.read() 

# print(extract_content('test.txt'))

if __name__ == "__main__":
    filename = sys.argv[1]
    print(extract_content(filename))


