def main():
    marks = []

    while True:
        print("\n----- MENU -----")
        print("1. Add Student Marks")
        print("2. Display Marks")
        print("3. Delete Marks")
        print("4. Find Highest & Lowest Marks")
        print("5. Find Average Marks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            n = int(input("How many marks you want to add? "))
            for i in range(n):
                mark = float(input(f"Enter mark {i+1}: "))
                marks.append(mark)
            print("Marks added successfully!")

        elif choice == "2":
            if len(marks) == 0:
                print("No marks available.")
            else:
                print("Student Marks:", marks)

        elif choice == "3":
            if len(marks) == 0:
                print("No marks to delete.")
            else:
                value = float(input("Enter mark to delete: "))
                if value in marks:
                    marks.remove(value)
                    print("Mark deleted successfully!")
                else:
                    print("Mark not found.")

        elif choice == "4":
            if len(marks) == 0:
                print("No marks available.")
            else:
                print("Highest Mark:", max(marks))
                print("Lowest Mark:", min(marks))

        elif choice == "5":
            if len(marks) == 0:
                print("No marks available.")
            else:
                average = sum(marks) / len(marks)
                print("Average Marks:", average)

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select between 1-6.")

main()
