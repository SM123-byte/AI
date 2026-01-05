import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.CYAN} Welcome to Sentiment Spy!🕵️ {Style.RESET_ALL}")
user = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()

if not user:
    user = "Mystery Agent"

conversation_history = []

print(f"\n {Fore.CYAN}Hello Agent {user}! \nType a sentence and I will show you sentiment using TextBlob!")
print(f"Type{Fore.YELLOW}'Reset', 'History' or 'Exit'{Fore.CYAN} to view options and quit. {Style.RESET_ALL} \n")

while True:
    user = input(f"{Fore.GREEN}->> {Style.RESET_ALL}").strip()

    if not user:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
    
    if user.lower() == "exit":
        print(f"\n {Fore.BLUE}Exiting Sentiment Spy... Farewell Agent {user}! {Style.RESET_ALL}")
        break

    elif user.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}All Conversation History Cleared 🎉!{Style.RESET_ALL}")
        continue

    elif user.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet! {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            
            for idx, (text, polarity, sentiment_type)in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😀"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😢"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}.{color} {emoji} {text},(Polarity: {polarity: .2f}, {sentiment_type}){Style.RESET_ALL}")
            
        continue
    
    polarity = TextBlob(user).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😀"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😢"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"
    
    conversation_history.append((user, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} Sentiment Detected! (Polarity:{polarity:.2f}) {Style.RESET_ALL}\n")