# Amazon AI Apprentice Chatbot Project
print("--- Welcome to Amazon AI Support ---")

# Asking the user for their name (Communication)
name = input("What is your name? ")
print(f"Hello Zak! I am the Amazon AI Assistant.")

# Asking for a command
command = input("How can I help you today? (Type: Order, Refund Site, or Support): ").lower()

# Using Logic (If/Else) to decide what to say back
if command == "order":
    print("Checking your Amazon packages... they are on the way to London!")
elif command == "ai":
    print("AI is the future. You're on the right path to Success")
elif command == "car":
    print("The best cars at the moment are the 2026 model cars!")
else:
    print("I'm not sure about that, but keep working hard on your goals!")

print("--- Session Ended. Goodbye! ---")
