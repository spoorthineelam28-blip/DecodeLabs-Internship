import csv
import os

users_file = "users.csv"
history_file = "history.csv"

recommendations = {
    "AI": ["Machine Learning", "Deep Learning", "Computer Vision"],
    "Programming": ["Python", "Java", "C++"],
    "Web Development": ["HTML", "CSS", "JavaScript"],
    "Data Science": ["Pandas", "NumPy", "Power BI"],
    "Cyber Security": ["Ethical Hacking", "Network Security", "Cryptography"]
}

def register():
    name = input("Enter Name: ")

    with open(users_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name])

    print("Registration Successful!")

def recommend():
    name = input("Enter User Name: ")

    print("\nAvailable Interests:")
    for interest in recommendations:
        print("-", interest)

    choice = input("\nEnter Interest: ")

    if choice in recommendations:
        print("\nRecommended Courses:")

        score = 100

        for item in recommendations[choice]:
            print("✔", item)

        with open(history_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, choice, score])

        print("\nRecommendation Score:", score)

    else:
        print("No Recommendations Found")

def view_history():

    if not os.path.exists(history_file):
        print("No History Available")
        return

    with open(history_file, "r") as file:
        reader = csv.reader(file)

        print("\nRecommendation History")
        print("-" * 40)

        for row in reader:
            print(row)

def analytics():

    count = 0

    if os.path.exists(history_file):

        with open(history_file, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                count += 1

    print("\nTotal Recommendations Generated:", count)

while True:

    print("\n")
    print("=" * 50)
    print(" AI PERSONALIZED RECOMMENDATION SYSTEM ")
    print("=" * 50)

    print("1. Register User")
    print("2. Get Recommendations")
    print("3. View History")
    print("4. Analytics")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        recommend()

    elif choice == "3":
        view_history()

    elif choice == "4":
        analytics()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")