import re
import random
from colorama import Fore, init
from datetime import datetime
import pytz


# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "London", "New York", "Shen Zen"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

city_times = {
    "tokyo": "Asia/Tokyo",
    "london": "Europe/London",
    "new york": "America/New York",
    "shen zen": "Asia/Shanghai",
    "bali": "Asia/Makassar",
    "maldives": "Indian/Maldives",
    "phuket": "Asia/Bangkok"
}

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def tell_time():
    print(Fore.CYAN + "Which city's time would you like to know?")
    print(Fore.LIGHTBLUE_EX + f"Options: {', '.join(city_times.keys()).title()}")
    city = normalize_input(input(Fore.YELLOW + "You: "))

    if city in city_times:
        timezone = pytz.timezone(city_times[city])
        city_now = datetime.now(timezone)
        time_str = city_now.strftime("%I:%M %p (%Z)")
        print(Fore.GREEN + f"Travel Bot: The current time in {city.title()} is {time_str}")
    else:
        print(Fore.RED + "Sorry! I don't quite understand! I don't think I have the time for that location yet!")

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
    
    show_help()

# Offer packing tips based on user’s destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Tell the city times for the travel destination (say 'time')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    
    show_help()
    
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "time" in user_input or "clock" in user_input:
            tell_time()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!\n")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?\n")

# Run the chatbot
if __name__ == "__main__":
    chat()
