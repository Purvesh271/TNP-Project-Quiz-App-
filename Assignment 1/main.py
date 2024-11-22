print('-'*40)
print('Welcome to Quiz Game')
print('-'*40)

# Importing the questions from the questions.py file
from quizData import topics
print(topics[0]['data'][0])

# Creating a users dictionary for storing the username and password
users = {}

#Login User
def logIn():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if (username in users.keys() and users[username] == password):
        print("You have successfully Logged In")
        print("-"*40)
        startQuiz()
    else:
        print("Invalid username or password")
        main()

#Signup User
def signUp():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users[username] = password
    print("You have successfully Signed Up")
    print("-"*40)
    again()

#StartQuiz
def startQuiz():
    score = 0
    i = 1
    for topic in topics:
        print(f'Press {i} to choose {topic["topic"]}')
        i += 1
        
    choice = int(input("Enter your choice: "))
    questions = topics[choice - 1]["data"]
    
    for question in questions:
        print("-"*40)
        print(question["question"])
        
        for index, option in enumerate(question["options"]):
            print(f'{index + 1}. {option}')
            
        answer = int(input("Enter your answer: "))
        user_answer = question["options"][answer - 1]
        correct_answer = question["answer"]
        
        if user_answer == correct_answer:
            score += 1
            print("Correct answer")
        else:
            print("Wrong answer")
            print("Correct answer is", question["answer"])
            
    print(f'Your score is {score}/{len(questions)}')

#Ask User to Play Again
def again():
    startQuiz()
    playAgain = input("Do you want to play again? (yes/no): ")
    if (playAgain == "yes"):
        startQuiz()
    else:
        print("Thank you for playing")
        
#Ask User to Login or Signup
def main():
    print("Enter 1 to LogIn")
    print("Enter 2 to SignUp")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        logIn()
    else:
        signUp()
        
main()