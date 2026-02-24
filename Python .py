students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    students.append({"name": name, "roll": roll, "marks": marks})
    print("Student added successfully!")

def view_all():
    if not students:
        print("No records found.")
    else:
        print("All student records:")
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")

def search_student():
    roll = input("Enter roll number to search: ")
    found = [s for s in students if s['roll'] == roll]
    if found:
        print("Student found:")
        for s in found:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    else:
        print("No student with that roll number.")

def average_marks():
    if not students:
        return print("No records to calculate average.")
    avg = sum(s['marks'] for s in students) / len(students)
    print(f"Average marks: {avg:.2f}")

def display_topper():
    if not students:
        return print("No records to find topper.")
    topper = max(students, key=lambda s: s['marks'])
    print(f"Topper: {topper['name']} (Roll: {topper['roll']}) with marks {topper['marks']}")

def menu():
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll")
        print("4. Calculate Average Marks")
        print("5. Display Topper")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all()
        elif choice == '3':
            search_student()
        elif choice == '4':
            average_marks()
        elif choice == '5':
            display_topper()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()