short_messages = ['hi', 'hello', 'welcome']
show_messages = []

while short_messages:
    doing_current_messages = short_messages.pop()
    print(f"Taking these messages: {short_messages} and putting them in the messages directory")
    show_messages.append(doing_current_messages)

# Display all completed messages
print("\nHere are the following messages: ")
for show_message in show_messages:
    print(show_messages)