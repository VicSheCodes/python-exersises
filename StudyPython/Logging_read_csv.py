# decorators

import csv
import time

with open("input_data.csv", 'w', newline='') as csv_file:
    csv_file.write("Name,Age,Height,Weight\n")


def log_message(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[LOG] {message}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMING] {func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@log_message("Reading data from CSV file")
@timing_decorator
def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data


@log_message("Processing data using generator")
@timing_decorator
def process_data(data):
    processed_data = (row[0].upper() for row in data)  # Example processing: converting to uppercase
    return list(processed_data)


@log_message("Writing processed data to a new CSV file")
@timing_decorator
def write_csv(processed_data, output_file_path):
    with open(output_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for item in processed_data:
            writer.writerow([item])


if __name__ == "__main__":
    input_file_path = "input_data.csv"
    output_file_path = "output_data.csv"

    # Read data from CSV
    data = read_csv(input_file_path)

    # Process data using generator
    processed_data = process_data(data)

    # Write processed data to a new CSV file
    write_csv(processed_data, output_file_path)
