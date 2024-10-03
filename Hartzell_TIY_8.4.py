def make_shirt(shirt_size='large', shirt_message='i love python'):
    """Display the information"""
    print(f"\nI want {shirt_size.title()} t-shirt with the message {shirt_message.title()}")

# Connecting the dots
make_shirt()

# Changing the shirt to medium
make_shirt(shirt_size='medium')

# A third random shirt
make_shirt(shirt_size='small', shirt_message='I love spam')
