# -*- coding: utf-8 -*-
import re
import sys

emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "]+", flags=re.UNICODE)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)

def main():
    if len(sys.argv) != 3:
        return -1

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    with open(in_path, 'r') as in_file, open(out_path, 'w') as out_file:
        for line in in_file:
            out_file.write(remove_emoji(line.decode('utf-8')).encode('utf-8'))

if __name__ == '__main__':
    main()

