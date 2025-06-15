def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I assist you?"
    elif "name" in user_input:
        return "I'm CodeAlpha Chatbot!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I didn't understand that."
