#Creating a main function for the system
def main():
  # Prompt the user to enter a final mark
  final_mark = float(input("Enter final mark: "))
  # Check if input is a valid number between 0 and 100
  if final_mark <0 or final_mark >100:
      print("Invalid mark")
  else:
  # Determine the grade symbol based on the mark
      if final_mark >= 75:
          print("pass")
          print("Grade=A")
      elif final_mark >= 60 and final_mark < 75:
          print("pass")
          print("Grade=B")
      elif final_mark >= 50 and final_mark < 60:
          print("pass")
          print("Grade=C")
      elif final_mark >= 0 and final_mark < 50:
          print("fail")
          print("Grade=F")
  # Display the results
#Calling the main function properly so the program runs properly
if __name__=="__main__":
  main() 

