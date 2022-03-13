import argparse
import random
import argparse


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--size', help='Amount of data', required=True, type=int)
    parser.add_argument('--characters_size', help='Length of the generated string', required=True, type=int)
    parser.add_argument('--excluded_size', help='Length of the generated excluded string', required=False, default=None, type=int)
    parser.add_argument('--output_path', help='Path to output file', required=False, default='./dataset.txt', type=str)
    return parser.parse_args()

def generate_characters(size):
    return str().join(
        [chr(random.randint(0, 127)) for n in range(size)])

def generate_excluded_characters(characters, size):
    return characters[0 : size] + characters[len(characters) - size : len(characters)]

def convert_to_ascii(characters, separator=' '):
    return str().join(
        [ str(ord(char)) + separator for char in characters ])


if __name__ == '__main__':
    args = parse_args()

    previous_characters = []
    previous_excluded = []

    for i in range(args.size):
        ascii_characters = None
        ascii_excluded = None

        while True:
            characters = generate_characters(args.characters_size)
            ascii_characters = convert_to_ascii(characters)

            excluded = generate_excluded_characters(characters, args.excluded_size) if args.excluded_size else ''
            ascii_excluded = convert_to_ascii(excluded) if args.excluded_size else ''

            if not ascii_characters in previous_characters and \
                (not ascii_excluded in previous_excluded or not args.excluded_size):
                previous_characters.append(ascii_characters)
                previous_excluded.append(ascii_excluded)
                break

        with open(args.output_path, 'a', encoding='utf8') as output:
            output.write(ascii_characters + '\n')
            output.write(ascii_excluded + '\n')
