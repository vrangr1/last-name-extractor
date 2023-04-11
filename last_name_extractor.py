import argparse

def contains_uppercase(word: str) -> bool:
    if '-' in word:
        return False
    if len(word) >= 4: return False
    return any(char.isupper() for char in word)

def last_name_extractor(input_file: str, output_file: str) -> None:
    """Extracts the last name from a file and writes it to a new file."""
    file = open(input_file, 'r')
    file_lines = file.readlines()
    file_write = open(output_file, 'w')
    for line in file_lines:
        line = line.strip()
        og = line
        if line == 'N/A':
            file_write.write("N/A\n")
            continue
        if len(line) < 2:
            file_write.write("\n")
            continue
        line = line.split()
        assert len(line) > 1, "Line must have at least two words. Current line: " + str(line)
        last_word = line[-1]
        
        while contains_uppercase(last_word[1:]):
            line = line[:-1]
            last_word = line[-1]
            assert len(line) > 0, "Name must have something other than designations! Name: " + str(og) + "; line: " + str(line)
        file_write.write(last_word + "\n")
    file.close()
    file_write.close()

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Extracts the last name from a file and writes it to a new file.')
    parser.add_argument('input_file', type=str, help='The input file.')
    parser.add_argument('output_file', type=str, help='The output file.')
    return parser.parse_args(args)

if __name__ == '__main__':
    args = parse_args()
    last_name_extractor(args.input_file, args.output_file)