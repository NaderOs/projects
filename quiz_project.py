name = input("Please enter your name: ")
grade = input("Please enter your grade and class: ")

intro = f"Welcome {name} from {grade}! This is a short quiz to test your knowledge on a few different subjects. These subjects are: Math, Science, ICT, Literature, and Social Studies. At the end of the quiz, you will receive your marks as well as a final report card. Good Luck!"

math_counter = 0
science_counter = 0
ict_counter = 0
lit_counter = 0
ss_counter = 0

check_mark = u'\u2713'
cross_mark = u'\u274C'


def start_quiz():
    print(intro)

    global math_counter
    global science_counter
    global ict_counter
    global lit_counter
    global ss_counter

    math_1 = input('What is the square root of 144? ')
    if math_1 == "12":
        print(f"Correct! {check_mark}")
        math_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Math mark is {math_counter}")

    math_2 = input('What is the mathematical constant 3.14... known as? ')
    if math_2 == "pi":
        print(f"Correct! {check_mark}")
        math_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Math mark is {math_counter}")

    science_1 = input("What is the name of the process which turns liquids into gases? ")
    if science_1.lower() == 'evaporation':
        print(f"Correct! {check_mark}")
        science_counter =+ 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Science score is {science_counter}")

    science_2 = input("What is the boiling point of pure water? (in degrees celsius) ")
    if science_2 == "100":
        print(f"Correct! {check_mark}")
        science_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Science score is {science_counter}")

    ict_1 = input("What function is used to  get a user's input in Python? ")
    if ict_1 == 'input()':
        print(f"Correct! {check_mark}")
        ict_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current ICT score is {ict_counter}")

    ict_2 = input("What is anything with quotation marks around it called in Python? ")
    if ict_2.lower() == "strings":
        print(f"Correct! {check_mark}")
        ict_counter += 1
    elif ict_2.lower() == "string":
        print(f"Correct! {check_mark}")
        ict_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current ICT score is {ict_counter}")

    lit_1 = input("Who wrote Hamlet? ")
    if lit_1.lower() == "shakespeare":
        print(f"Correct! {check_mark}")
        lit_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Literature score is {lit_counter}")

    lit_2 = input("Who is the main character of Harry Potter? ")
    if lit_2.lower() == "harry potter":
        print(f"Correct! {check_mark}")
        lit_counter += 1
    elif lit_2.lower() == "harry":
        print(f"Correct! {check_mark}")
        lit_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Literature score is {lit_counter}")

    ss_1 = input("What is the capital of the UAE? ")
    if ss_1.lower() == "abu dhabi":
        print(f"Correct! {check_mark}")
        ss_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Social Studies score is {ss_counter}")

    ss_2 = input(f"Where is the Burj Khalifa? ")
    if ss_2.lower() == "dubai":
        print(f"Correct! {check_mark}")
        ss_counter += 1
    else:
        print(f"Incorrect {cross_mark}")
    print(f"Your current Social Studies score is {ss_counter}")


def make_report_card():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"Name: {name}              Grade: {grade}")

    math_mark = int((math_counter / 2) * 100)
    science_mark = int((science_counter / 2) * 100)
    ict_mark = int((ict_counter / 2) * 100)
    lit_mark = int((lit_counter / 2) * 100)
    ss_mark = int((ss_counter / 2) * 100)

    print(f"Math: {math_mark}%")
    print(f"Science: {science_mark}%")
    print(f"ICT: {ict_mark}%")
    print(f"Literature: {lit_mark}%")
    print(f"Social Studies: {ss_mark}%")

    failed_subjects = 0
    if math_mark <= 50:
        failed_subjects += 1
    if science_mark <= 50:
        failed_subjects += 1
    if ict_mark <= 50:
        failed_subjects += 1
    if lit_mark <= 50:
        failed_subjects += 1
    if ss_mark <= 50:
        failed_subjects += 1

    if failed_subjects >= 3:
        print(f"You FAILED your grade {cross_mark}")
    else:
        print(f"You PASSED your grade! {check_mark}")


start_quiz()
make_report_card()
