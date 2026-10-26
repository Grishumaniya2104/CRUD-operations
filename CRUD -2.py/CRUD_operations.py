print("Welcome to the Student Data Organizer!")

students = [
    {"ID":1 , "Name":"Alice", "Age":20, "Grade":"B+", "Date of Birth":2002-5-14, "Subjects":"Maths, Science, English"},
    {"ID":2 , "Name":"Bilu", "Age":20, "Grade":"B", "Date of Birth":2002-5-30, "Subjects":"chemistry, History, biology"}
]

while True:
    ("select an option")
    print("1.Add student")
    print("2. Display all student")
    print("3. Update student information")
    print("4. Delate student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice=int(input("Enter your choice above options:-"))

    if choice == 1:
        student_id=int(input("Enter student id:-"))
        name=input("Enter student name:-")
        Age=int(input("Enter student age:-"))
        Grade=input("Enter student grade:-")
        Dob=input("Enter student's DOB (YYYY-MM-DD):-")
        sub=input("Enter subjets:-")

        new_student = {
        "ID":student_id,
        "Name":name,
        "Age":Age,
        "Grade":Grade,
        "Date of Birth":Dob,
        "Subjects":sub
        }

        students.append(new_student)
        print("Student added successfully!")
        print("Updated list:",students)


    elif choice == 2:
        for student in students:
            print("ID :",student["ID"] ,"Name :",student["Name"],"Age :",student["Age"],"Grade :",student["Grade"],"Date of Birth :",student["Date of Birth"],"Subjects :",student["Subjects"],sep=" |")

    elif choice == 3:
        student_id=int(input("Enter student ID:-"))
        found = False

        for student in students:
            if student["ID"]== student_id:
                student["Age"]==int(input("Enter new age:-"))
                student["Subjects"]==input("Enter new subjects:-")
                found = True
                print("List updated successfully!")
                break

        if not found:
            print("student id not found")


    elif choice == 4:
        student_id=int(input("Enter student id to Delated"))
        found=False

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                print("student remove successfully")
                found=True
                break

        if not found:
            print("Student not found")

    elif choice == 5:
        new_subjects={"maths","science","english","chemistry","history","biology"}
        print("These are the subjects you can selected:", new_subjects)


    elif choice == 6:
        print("Thank you for using the programme!")
        break


    else:
        print("invalid choice! please enter a number 1 to 6.")
        



















