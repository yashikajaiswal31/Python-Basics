import random

# Define responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good here!"],
    "what's your name": ["I'm just a simple chatbot.", "I don't really have a name, I'm just here to help."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"]
}

def get_response(message):
    # Convert the message to lowercase for easier matching
    message = message.lower()
    
    # Check if the message matches any predefined responses
    for key in responses:
        if message in key:
            return random.choice(responses[key])
    
    # If no predefined response is found, return a default response
    return "I'm sorry, I didn't understand that."

def main():
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if the user types 'bye'
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get and print the chatbot's response
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
