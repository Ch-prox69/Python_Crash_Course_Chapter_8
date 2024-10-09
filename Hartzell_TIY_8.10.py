short_messages = ['hi', 'hello', 'welcome']
sent_messages = []

def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending messages")
        sent_messages.append(current_message)

# Calling Functions
send_messages(short_messages)

# Printing
print("\nShort Messages:", short_messages)
print("Sent Messages:", sent_messages)