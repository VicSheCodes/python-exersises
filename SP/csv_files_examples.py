'''Certainly! Here are some exercises to help you further practice using the `csv` library in Python:

1. **Read from CSV File:**
   - Write a function that reads data from a CSV file and prints it.
   - The function should take the CSV file path as an argument.
   - Use the `csv.reader` object to iterate over the rows.

2. **Filtering and Display:**
   - Read a CSV file containing information about employees (columns: Name, Department, Salary, etc.).
   - Write a function that reads the CSV file, filters employees based on a specified department, and displays their information.

3. **Data Modification:**
   - Read a CSV file containing student information (columns: Name, Grade, Subject, etc.).
   - Write a function that increases the grades of all students in a specified subject by a certain percentage and writes the updated data back to the CSV file.

4. **Appending Data Dynamically:**
   - Write a function that appends a new row of data to an existing CSV file.
   - The function should take the CSV file path and a list of data as arguments.
   - Append the new data to the existing file.

5. **CSV to Dictionary:**
   - Read a CSV file containing information about products (columns: ProductID, ProductName, Price, etc.).
   - Write a function that converts the CSV data into a list of dictionaries, where each dictionary represents a product.

6. **Export to CSV from Dictionary:**
   - Create a dictionary containing information about books (keys: Title, Author, Genre, etc.).
   - Write a function that exports this dictionary to a CSV file.
   - Each key in the dictionary should correspond to a column in the CSV file.

7. **Handling Missing Data:**
   - Modify the function from exercise 1 to handle CSV files with missing or incomplete data gracefully.
   - Print a message for each row where data is missing or incomplete.

8. **CSV with Headers:**
   - Create a CSV file with headers (first row) and some data.
   - Write a function that reads the CSV file and prints the headers and the total number of rows.

9. **Interactive CSV Editor:**
   - Create a simple interactive CSV editor where the user can add, update, or delete rows in a CSV file.
   - Use a menu system to let the user choose the operation they want to perform.

10. **CSV Sorting:**
   - Read a CSV file containing data about cities (columns: City, Population, Country, etc.).
   - Write a function that sorts the data based on a specified column (e.g., Population) and writes the sorted data
   back to the CSV file.

These exercises cover a range of scenarios and will help you gain a better understanding of how to work with CSV files
 using the `csv` library in Python.'''

import csv
import os

csv_file_path_1 = os.path.join(os.getcwd(), "Data_files", "example1.csv")
csv_file_path_2 = os.path.join(os.getcwd(), "Data_files", "example2.csv")

data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'Los Angeles'],
    ['Bob', 22, 'Chicago']
]

data_to_append = [
    ['Diana', 28, 'San Francisco'],
    ['Charlie', 35, 'Seattle']
]

def create_csv_file(csv_file_path_1):
    with open(csv_file_path_1, 'w') as file:
        file.write("Name,Age,City\nJohn,20,NY\nMary,30,TA\n")
        file.close()


def read_csv(csv_file_path_1):
    with open(csv_file_path_1, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
    return csv_reader


def write_csv(data, csv_file_path_2):
    with open(csv_file_path_2, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerows(data)
    return csv_file

def append_csv(data, csv_file_path_2):
    with open(csv_file_path_2, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerows(data)
    return csv_file


def test_csv_functions():
    create_csv_file(csv_file_path_1)

    read_csv(csv_file_path_1)

    write_csv(data_to_write, csv_file_path_2)

    read_csv(csv_file_path_2)

    append_csv(data_to_append, csv_file_path_2)