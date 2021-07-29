def determent_grade(score: float) -> str:
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'B'
    else:
        return 'F'


def compute_score(midterm: float, final: float) -> float:
    return 0.4 * midterm + 0.6 * final


def input_score(exam: str) -> float:
    score = 0
    lower_bound = 0
    upper_bound = 100
    while True:
        score_str = input(f'Please enter the student\'s {exam} exam mark ({lower_bound}, {upper_bound}): ')
        if score_str.isalpha():
            print('Please enter a score as a decimal number')
            continue
        score = float(score_str)
        if score > 100 or score < 0:
            print(f'Please enter a score in the range [{lower_bound}, {upper_bound}]')
            continue
        break
    return score


def main() -> None:
    student_id = input('Please enter your student ID: ')
    midterm = input_score('midterm')
    final = input_score('final')
    total_score = compute_score(midterm, final)
    grade = determent_grade(total_score)
    print(f'Student ID {student_id} has the total mark as {total_score} and has a grade as {grade}')


if __name__ == '__main__':
    main()
