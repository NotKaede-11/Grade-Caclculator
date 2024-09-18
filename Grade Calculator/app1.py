

print("Welcome to the Grade Calculator!")
while True:
    try:
        prelim_grade = float(input("Enter your Prelim grade: "))
        if 0 <= prelim_grade <= 100:
            break
        else:
            print("Prelim grade must be between 0 and 100. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical grade.")
        
prelim_contribution = 0.20 * prelim_grade
max_midterm_final = 0.30 + 0.50


if prelim_contribution + max_midterm_final * 100 < 75:
    print("Sorry, but it is impossible for you to pass the course with your current Prelim grade.")
else:
    remaining_for_midterm_final = 75 - prelim_contribution
    required_midterm = remaining_for_midterm_final / max_midterm_final
    required_final = required_midterm 
    
    print("To pass the course with an overall grade of 75, you need at least:")
    print(f"Midterm grade: {required_midterm:.2f}")
    print(f"Final grade: {required_final:.2f}")
    
    if prelim_contribution + max_midterm_final * 100 >= 90:
        print("Congratulations! You've qualified for Dean's lister.")
    else:
        remaining_for_midterm_final1 = 90 - prelim_contribution
        required_midterm1 = remaining_for_midterm_final1 / max_midterm_final
        required_final1 = required_midterm1 
        
        print("If you want to become a Dean's lister, you need at least:")
        print(f"Midterm grade: {required_midterm1:.2f}")
        print(f"Final grade: {required_final1:.2f}")

            