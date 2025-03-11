# Lory Rubio Programming Assignment 8
# This program uses the csv module to write each record into the grades.csv file and have a header of First Name, Last Name, Exam 1, Exam 2 and Exam3.
# A separate program  reads the grades.csv file and displays the data in tabular format. Implements the with keyword

# We need to import the csv module since we are going to use cvs files and do logic.
import csv

# The first program which is getting student data and writing into CSV
def cvs_examstudentinfo():

    # Create a grades csv file in the mode write 'w'
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # CSV file needs to have a specific header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Obtain teacher input regarding students' exam info
        numofstudents = int(input("Enter the number of students: "))

        # Gather input, looping for each of the students that the teacher needs
        for _ in range(numofstudents):
            first_name = input("Enter the student's first name: ")  # Get first name
            last_name = input("Enter the student's last name: ")  # Get last name
            exam1 = int(input("Enter grade for Exam 1: "))  # Get grade for Exam 1
            exam2 = int(input("Enter grade for Exam 2: "))  # Get grade for Exam 2
            exam3 = int(input("Enter grade for Exam 3: "))  # Get grade for Exam 3

            # Now we need to commit or write this data into the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    # Let the user know that the data has been stored
    print('Your data has been saved into grades.csv')

    # Call the function to read and display the CSV content
    read_gradescsv()

# The second program that reads the grade file and displays the data in tabular form
def read_gradescsv():

    # Open the file in read mode ('r')
    with open('grades.csv', mode='r') as file:

        # To do this, we need to create an object of it
        reader = csv.reader(file)

        # Read the header row we created previously
        header = next(reader)

        # Print the header in tabular format
        print(f"{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")

        # Loop through the rows in the CSV file and print the student data
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")

# Run the program
cvs_examstudentinfo()