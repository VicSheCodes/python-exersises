def process_file(input_file, output_file, n):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            line = line.replace('*', '')  # Delete all asterisks
            if len(line) > n:
                while len(line) > n:
                    split_index = line.rfind(' ', 0, n)  # Find the last space within the first n characters
                    if split_index == -1:  # If no space found, split at n directly
                        split_index = n
                    f.write(line[:split_index].strip() + '\n')  # Write characters up to the space
                    line = line[split_index:].strip()  # Move the rest to the next line
                f.write(line.strip() + '\n')  # Write any remaining characters to a new line
            else:
                f.write(line)

if __name__ == '__main__':

    input_file = 'Switch_vs_Router'
    output_file = 'mb_Switch_vs_Router'
    n = 42  # Set your desired length
    process_file(input_file, output_file, n)
