# Advanced Rule-Based AI Chatbot

from datetime import datetime

print("=" * 50)
print("🤖 Welcome to Smart Rule-Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'exit' to end the chat.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower()

    # Exit
    if user == "exit":
        print("🤖 Chatbot: Goodbye! Have a nice day.")
        choice=input("DO YOU WANT TO RESTART ?(yes/no): ").lower()
        if choice=="yes":
            print("chatbot:REASTARING chatbot.....")
            continue
        else:
            print("chatbot closed")
            break

    # Help Menu
    elif user == "help":
        print("""
Available Topics:
1. Greetings (hi, hello)
2. About chatbot (your name)
3. Date and Time
4. Python
5. AI
6. Weather
7. Education
8. Programming Languages
9. Internship
10. Motivation
11. Calculator
12. Thank You
13. Exit
        """)

    # Greetings
    elif user in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hello! How can I assist you today?")

    # Name
    elif "your name" in user:
        print("🤖 Chatbot: My name is SmartBot.")

    # How are you
    elif "how are you" in user:
        print("🤖 Chatbot: I'm doing great. Thanks for asking!")

    # Date
    elif "date" in user:
        print("🤖 Chatbot:", datetime.now().strftime("Today's date is %d-%m-%Y"))

    # Time
    elif "time" in user:
        print("🤖 Chatbot:", datetime.now().strftime("Current time is %H:%M:%S"))

    # Python
    elif "python" in user:
        print("🤖 Chatbot: Python is a popular high-level programming language.")

    # AI
    elif "artificial intelligence" in user or user == "ai":
        print("🤖 Chatbot: AI enables machines to mimic human intelligence.")

    # Weather
    elif "weather" in user:
        print("🤖 Chatbot: I cannot access live weather, but it looks like a good day to learn Python!")

    # Education
    elif "education" in user:
        print("🤖 Chatbot: Education helps develop knowledge, skills, and critical thinking.")

    # Internship
    elif "internship" in user:
        print("🤖 Chatbot: Internships provide practical experience and improve professional skills.")

    # Programming Languages
    elif "java" in user:
        print("🤖 Chatbot: Java is an object-oriented programming language.")

    elif "c++" in user:
        print("🤖 Chatbot: C++ is widely used for system and application development.")

    elif "c language" in user or user == "c":
        print("🤖 Chatbot: C is a powerful procedural programming language.")

    # Motivation
    elif "motivate me" in user or "motivation" in user:
        print("🤖 Chatbot: Success comes from continuous learning and practice. Keep going!")

    # Thank You
    elif "thank you" in user or "thanks" in user:
        print("🤖 Chatbot: You're welcome!")

    # Simple Calculator
    elif user == "calculator":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+,-,*,/): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Result =", num1 + num2)
            elif op == "-":
                print("Result =", num1 - num2)
            elif op == "*":
                print("Result =", num1 * num2)
            elif op == "/":
                print("Result =", num1 / num2)
            else:
                print("Invalid operator!")
        except:
            print("Invalid input!")

    # College Information
    elif "college" in user:
        print("🤖 Chatbot: College education helps students gain professional knowledge and skills.")

    # Skills
    elif "skills" in user:
        print("🤖 Chatbot: Important skills include communication, teamwork, problem-solving, and programming.")

    # Career
    elif "career" in user:
        print("🤖 Chatbot: Focus on learning, projects, internships, and certifications to build a strong career.")

    # Default Response
    else:
        print("🤖 Chatbot: Sorry, I don't understand that. Type 'help' to see available commands.")