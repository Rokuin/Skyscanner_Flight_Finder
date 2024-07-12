# modules/user_input.py

from datetime import datetime

def get_user_input():
    """
    Collect user input for flight search parameters.
    
    Returns:
    dict: A dictionary containing user input parameters.
    """
    print("Welcome to the Flight Finder!")
    
    # Get departure and arrival cities
    departure = input("Enter departure city/airport: ").strip()
    arrival = input("Enter arrival city/airport: ").strip()
    
    # Get date range
    while True:
        try:
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            if start_date > end_date:
                print("Start date must be before end date. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Get preferred time sections
    print("Preferred time sections (you can select multiple):")
    print("1. Morning (5am to 10am)")
    print("2. Noon (11am to 3pm)")
    print("3. Evening (4pm to 12pm)")
    time_sections = input("Enter your choices (e.g., 1,3 for Morning and Evening): ").strip()
    time_sections = [int(x) for x in time_sections.split(',') if x.isdigit()]
    
    return {
        "departure": departure,
        "arrival": arrival,
        "start_date": start_date,
        "end_date": end_date,
        "time_sections": time_sections
    }

if __name__ == "__main__":
    # Test the function
    user_preferences = get_user_input()
    print("\nUser preferences:")
    for key, value in user_preferences.items():
        print(f"{key}: {value}")