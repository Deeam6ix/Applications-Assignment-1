# Import the built-in json module to handle reading and writing JSON files
import json

# Import the os module to check if the JSON file exists
import os

# Define the name of the file where grading records will be saved
DATA_FILE = "grading_records.json"


# Define a base class to store the student's final mark
class GradingSysInput: #Parent class
    def __init__(self, final_mark):
        # Store the final mark as an instance variable
        self.final_mark = final_mark


# Define a child class that inherits from GradingSysInput and processes the mark
class GradingSysProcess(GradingSysInput): #Child class
    def __init__(self, final_mark): #Child class Inheriting parent class characteristics
        # Inherit initialization from the parent class
        super().__init__(final_mark)

    # Method to evaluate the mark, display the grade, and save the result
    def output(self):
        try:
            # Ensure the input is a number (int or float)
            if not isinstance(self.final_mark, (int, float)):
                raise TypeError("Mark must be a number.")

            # Validate that the mark is within the range 0–100
            if self.final_mark < 0 or self.final_mark > 100:
                raise ValueError("Mark must be between 0 and 100.")

            # Determine grade and result based on mark
            if self.final_mark >= 75:
                grade = "A"
                result = "Passed"
            elif self.final_mark >= 60:
                grade = "B"
                result = "Passed"
            elif self.final_mark >= 50:
                grade = "C"
                result = "Passed"
            else:
                grade = "F"
                result = "Failed"

            # Display the result to the user
            print(f"{result}  |  Grade: {grade}")

            # Save the mark, grade, and result to the JSON file
            save_to_json(self.final_mark, grade, result)

        # Handle specific error if input is not a number
        except TypeError as te:
            print(f"Type Error: {te}")

        # Handle specific error if mark is out of range
        except ValueError as ve:
            print(f"Value Error: {ve}")

        # Catch any other unexpected errors
        except Exception as e:
            print(f"Unexpected error: {e}")


# Function to load existing grading records from the JSON file
def load_json_data():
    # Check if the data file already exists
    if os.path.exists(DATA_FILE):
        # Open the file in read mode and load the JSON data
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    # Return an empty list if file doesn't exist
    return []


# Function to save a new record (mark, grade, result) to the JSON file
def save_to_json(mark, grade, result):
    # Load existing records
    data = load_json_data()

    # Create a dictionary entry for the current record
    entry = {
        "mark": mark,
        "grade": grade,
        "result": result
    }

    # Append the new entry to the existing list
    data.append(entry)

    # Write the updated list back to the JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

    # Confirm to the user that the result was saved
    print("Result saved to grading_records.json\n")


# Main function to run the grading system
def main():
    try:
        # Prompt the user to enter a mark
        user_input = input("Please enter the individual's mark: ")

        # Convert the input to a float
        mark = float(user_input)

        # Create an instance of GradingSysProcess with the given mark
        grading_sys = GradingSysProcess(mark)

        # Call the output method to evaluate and save the grade
        grading_sys.output()

    # Handle case where the input is not a valid float
    except ValueError:
        print("Invalid input. Please enter a valid numeric mark (e.g., 75, 60.5).")

    # Handle if the user presses Ctrl+C to exit the program
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    # Handle any other unexpected error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# This ensures the main function only runs when this file is executed directly
if __name__ == "__main__":
    main()
