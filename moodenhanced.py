name = input("Hello! I'm an AI Chatbot! What's your name?: ")
print(f"Nice to meet you {name}!")

print("Hello how are you feeling (good/bad)?: ")

mood = input().lower()

if mood == "good":
    print("Happy to hear that!")
elif mood == "bad":
    print("Sorry to hear that!")
    
    joke = input("Wanna hear a joke(yes/no)?: ").lower()
    if joke == "yes":
        print("Why are spiders so smart? - They can find everything on the web!")
    else:
        print("I'll leave you on your own - sometimes it's good to let the feelings to youself for a while so you can reflect")
else:
    print("Sometimes it's hard to put feelings into words")

print(f"It was nice chatting with you {name}! Goodbye!")