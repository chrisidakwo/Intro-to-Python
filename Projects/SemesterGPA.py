"""

Create a Semester GPA Calculator using functions only.

"""

# FIXME: Add docstrings to the functions explaining what they do and how they execute


def convert_grade(grade):
    """"""
    if grade == "F":
        return 0
    else:
        return 4 - (ord(grade) - ord("A"))


def get_grades():
    """"""
    semester_info = []
    more_grades = True
    exit = "X"

    while more_grades:
        course_grade = input("Enter grade (Enter X if done): ")
        while course_grade not in ("A", "B", "C", "D", "E", "F", "X"):
            course_grade = input("Enter letter grade received: ")
            if course_grade == exit:
                more_grades = False
        else:
            if course_grade == exit:
                break
            num_credits = int(input("Enter number of credits: "))
            semester_info.append([num_credits, course_grade])

    return semester_info


def calculate_gpa(sem_grades_info, cumm_gpa_info):
    """"""
    sem_quality_pts = 0
    sem_credits = 0
    current_cumm_gpa, total_credits = cumm_gpa_info

    for k, v in enumerate(sem_grades_info):
        num_credits, letter_grade = sem_grades_info[k]
        sem_quality_pts += (num_credits * convert_grade(letter_grade))
        sem_credits += num_credits

    sem_gpa = sem_quality_pts / sem_credits
    new_cumm_gpa = (current_cumm_gpa * total_credits + sem_gpa *
                    sem_credits) / (total_credits + sem_credits)

    return sem_gpa, new_cumm_gpa


# -------------------- main
def main():
    print("This program calculates new semester and cumulative GPAs\n")

    # Get current GPA info
    total_credits = int(input("Enter total number of earned credits: "))
    cumm_gpa = float(input("Enter your current cumulative GPA: "))
    cumm_gpa_info = cumm_gpa, total_credits

    # Get current semester grade info
    print()
    semester_grades = get_grades()

    # Calculate semester GPA and new cumulative GPA
    semester_gpa, cumm_gpa = calculate_gpa(semester_grades, cumm_gpa_info)

    # Display semester GPA and new cumulative GPA
    print("\nYour semester GPA is", format(semester_gpa, ".2f"))
    print("Your cumulative GPA is", format(cumm_gpa, ".2f"))


if __name__ == '__main__':
    main()
