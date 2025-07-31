# Define a base class to store the final mark
class GradingSysInput: #Parent class
    def __init__(self, final_mark):
        # Store the final mark as an instance variable
        self.final_mark = final_mark


# Define a class that processes the input and determines the grade
class GradingSysProcess(GradingSysInput): #Child Class 
    def __init__(self, final_mark): #Inheriting characteristic from the parent class
        # Call the constructor of the parent class
        super().__init__(final_mark)

    # Method to evaluate and display grade and pass/fail result
    def output(self):
        try:
            # Ensure the mark is a number
            if not isinstance(self.final_mark, (int, float)):
                raise TypeError("Mark must be a number.")

            # Check if the mark is within the valid range
            if self.final_mark < 0 or self.final_mark > 100:
                raise ValueError("Mark must be between 0 and 100.")

            # Determine and print grade based on mark
            if self.final_mark >= 75:
                print("Passed  |  Grade: A")
            elif self.final_mark >= 60:
                print("Passed  |  Grade: B")
            elif self.final_mark >= 50:
                print("Passed  |  Grade: C")
            else:
                print("Failed  |  Grade: F")

        except TypeError as te:
            print(f"Type Error: {te}")
        except ValueError as ve:
            print(f"Value Error: {ve}")
        except Exception as e:
            # Catch-all for any other unexpected exceptions
            print(f"Unexpected error: {e}")


# Define the main function to run the grading system
def main():
    try:
        # Prompt user for input
        user_input = input("Please enter the individual's mark: ")

        # Attempt to convert the input to a float
        mark = float(user_input)

        # Create a GradingSysProcess object with the numeric mark
        grading_sys = GradingSysProcess(mark)

        # Call the method to determine and display the grade
        grading_sys.output()

    except ValueError:
        # Handles input that cannot be converted to float (e.g., letters, symbols)
        print("Invalid input. Please enter a valid numeric mark (e.g., 75, 60.5).")
    except KeyboardInterrupt:
        # Handles if user abruptly stops the program (e.g., Ctrl + C)
        print("\nProgram interrupted by user.")
    except Exception as e:
        # General catch for unexpected errors
        print(f"An unexpected error occurred: {e}")


# Ensure the script runs only if executed directly (not imported)
if __name__ == "__main__":
    main()
