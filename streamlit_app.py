import requests
import streamlit as st

# Define the URL
url = 'https://api.dify.ai/v1/chat-messages'

# Define the headers
headers = {
    'Authorization': 'Bearer app-vZdvgJxtcq4BByR9mFqnSsQ6',
    'Content-Type': 'application/json'
}

# Chatbot
def chatbot(user_message, conversation_id, user):
    # Define the data
    data = {
        "inputs": {},
        "query": user_message,
        "response_mode": "streaming",
        "conversation_id": conversation_id,
        "user": user
    }

    # Make a POST request
    response = requests.post(url, headers=headers, json=data)
    
    # Return the response
    return response.json()

# Streamlit App
def main():
    st.title("Chatbot")
    
    # User Input
    user_message = st.text_input("Your Message")
    
    if st.button("Send"):
        # Get the chatbot response
        response = chatbot(user_message, "your_conversation_id", "your_username")

        # Display the chatbot response
        st.write(response)

# Run the app
if __name__ == "__main__":
    main()
