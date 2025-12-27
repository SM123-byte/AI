name = input("Hello! I'm an AI Chatbot! What's your name?: ")
print(f"Nice to meet you {name}!")

print("Hello how are you feeling (good/bad)?: ")

mood = input().lower()

if mood == "good":
    print("Happy to hear that!")
elif mood == "bad":
    print("Sorry to hear that - hope things get better soon!")
else:
    print("Sometimes it's hard to put feelings into words")

print(f"It was nice chatting with you {name}! Goodbye!")