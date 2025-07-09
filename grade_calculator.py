def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

def main():
    name = input("Enter Student Name: ")
    subjects = int(input("Enter number of subjects: "))
    marks = []

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / subjects
    grade = calculate_grade(average)

    print("\n--- Student Report ---")
    print(f"Name     : {name}")
    print(f"Total    : {total}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")

if __name__ == "__main__":
    main()
