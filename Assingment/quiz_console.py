questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which language is primarily used for creating web pages?",
        "options": ["A. HTML", "B. Python", "C. C++", "D. Java"],
        "answer": "A"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["A. Yuan", "B. Yen", "C. Won", "D. Ringgit"],
        "answer": "B"
    },
    {
        "question": "Who discovered gravity when he saw a falling apple?",
        "options": ["A. Albert Einstein", "B. Nikola Tesla", "C. Isaac Newton", "D. Galileo Galilei"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Oxide"],
        "answer": "B"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["A. 1939", "B. 1942", "C. 1945", "D. 1950"],
        "answer": "C"
    },
    {
        "question": "Which organ in the human body is responsible for pumping blood?",
        "options": ["A. Lungs", "B. Brain", "C. Kidney", "D. Heart"],
        "answer": "D"
    }
]

def question_render(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ")
        if user_answer.upper() == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
            correct_Ans(question)
        print("-------------------------")
        print(f"Your current score is: {score}")
    print(f"Your Final score is {score}")    
    
def correct_Ans(question):
            print(question["question"])
            print(f"Correct Answer is {question["answer"]}")
question_render(questions)
