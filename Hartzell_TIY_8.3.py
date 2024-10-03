def make_shirt(shirt_size, shirt_message):
    """Print message on the shirt requirements"""
    print(f"\nI need a size {shirt_size.title()} t-shirt.")
    print(f"I want my {shirt_size.title()} t-shirt to have the message {shirt_message.title()} on it.")


make_shirt('large', 'just do it')
make_shirt(shirt_size='3xl', shirt_message='Nike')
