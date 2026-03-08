# grade_calculator.py

def calculate_grade(average):
    if average >= 75:
        return "A"
    elif 60 <= average < 75:
        return "B"
    elif 40 <= average < 60:
        return "C"
    else:
        return "Fail"

while True:
    print("\n--- Grade Calculator ---")
    name = input("Enter student name (or type 'Exit' to quit): ")
    
    if name.strip().lower() == "exit":
        print("Exiting the program...")
        break

    try:
        # Ask for 3 subject marks
        marks = []
        for i in range(1, 4):
            mark = float(input(f"Enter mark {i}: "))
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")
            marks.append(mark)

        # Calculate average
        average = sum(marks) / len(marks)

        # Determine grade
        grade = calculate_grade(average)

        # Print formatted output
        print("------------------------------")
        print(f"Name   : {name}")
        print(f"Average: {average:.2f}")
        print(f"Grade  : {grade}")
        print("------------------------------")

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")