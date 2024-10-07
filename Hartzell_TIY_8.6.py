def get_city_info(city_name, city_country):
    """Print info on favorite city"""
    full_city = f"{city_name} {city_country}"
    return full_city.title()

while True:
    print("\nWhat is your favorite city name?")
    print("(enter 'q' to quit program)")

    c_name = input("City Name: ")
    if c_name == 'q':
        break

    c_ctry = input("City Country: ")
    if c_ctry == 'q':
        break

    city_info = get_city_info(c_name, c_ctry)
    print(f"\nYour city is {city_info}")