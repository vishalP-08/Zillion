# Basic Computer Knowledge Quiz Game

questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Processor Utility", "Central Performance Unit"],
        "answer": "A"
    },
    {
        "question": "Which of the following is an output device?",
        "options": ["Keyboard", "Mouse", "Monitor", "Scanner"],
        "answer": "C"
    },
    {
        "question": "What is the full form of RAM?",
        "options": ["Random Access Memory", "Read Access Memory", "Rapid Action Machine", "Random Allocated Memory"],
        "answer": "A"
    },
    {
        "question": "Which of these is a web browser?",
        "options": ["Google", "Firefox", "Windows", "Linux"],
        "answer": "B"
    },
    {
        "question": "Which language is known as the 'Father of all programming languages'?",
        "options": ["Python", "C", "Assembly", "FORTRAN"],
        "answer": "D"
    },
    {
        "question": "What is the brain of the computer?",
        "options": ["RAM", "Hard Drive", "CPU", "GPU"],
        "answer": "C"
    },
    {
        "question": "Which one is an operating system?",
        "options": ["MS Word", "Windows", "Google Chrome", "Intel"],
        "answer": "B"
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["Hyper Text Transfer Protocol", "High Transfer Text Protocol", "Hyperlink Transfer Text Protocol", "Hyper Tool Text Processing"],
        "answer": "A"
    },
    {
        "question": "Which company developed the Windows operating system?",
        "options": ["Google", "Apple", "Microsoft", "IBM"],
        "answer": "C"
    },
    {
        "question": "What is the smallest unit of data in a computer?",
        "options": ["Byte", "Bit", "Kilobyte", "Megabyte"],
        "answer": "B"
    }
]

score = 0

print("Welcome to the Basic Computer Knowledge Quiz!\n")

for index, q in enumerate(questions, start=1):
    print(f"Q{index}: {q['question']}")
    for i, option in enumerate(q["options"], start=1):
        print(f"{chr(64+i)}) {option}")

    user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct! +2 points\n")
        score += 2
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}. -1 point\n")
        score -= 1

print(f"Game Over! Your total score is: {score}")
if score > 15:
    print("🎉 Excellent! You're a computer expert!")
elif score > 5:
    print("😊 Good job! Keep learning.")
else:
    print("😞 Try again to improve your score!")
