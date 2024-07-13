# modules/user_input.py

from datetime import datetime
import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def get_user_input(use_default=False):
    """
    Collect user input for flight search parameters.
    
    Args:
    use_default (bool): If True, use default values from config.yaml
    
    Returns:
    dict: A dictionary containing user input parameters.
    """
    config = load_config()
    default_search = config['default_search']

    if use_default:
        return {
            "departure": default_search['departure'],
            "arrival": default_search['arrival'],
            "start_date": datetime.strptime(default_search['start_date'], "%Y-%m-%d"),
            "end_date": datetime.strptime(default_search['end_date'], "%Y-%m-%d"),
            "time_sections": default_search['time_sections']
        }

    print("Welcome to the Flight Finder!")
    
    # Get departure and arrival cities
    departure = input(f"Enter departure city/airport [{default_search['departure']}]: ").strip() or default_search['departure']
    arrival = input(f"Enter arrival city/airport [{default_search['arrival']}]: ").strip() or default_search['arrival']
    
    # Get date range
    while True:
        try:
            start_date = input(f"Enter start date (YYYY-MM-DD) [{default_search['start_date']}]: ").strip() or default_search['start_date']
            end_date = input(f"Enter end date (YYYY-MM-DD) [{default_search['end_date']}]: ").strip() or default_search['end_date']
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
    time_sections = input(f"Enter your choices (e.g., 1,3 for Morning and Evening) [{','.join(map(str, default_search['time_sections']))}]: ").strip()
    time_sections = [int(x) for x in time_sections.split(',') if x.isdigit()] if time_sections else default_search['time_sections']
    
    return {
        "departure": departure,
        "arrival": arrival,
        "start_date": start_date,
        "end_date": end_date,
        "time_sections": time_sections
    }

if __name__ == "__main__":
    # Test the function
    user_preferences = get_user_input(use_default=True)
    print("\nUser preferences:")
    for key, value in user_preferences.items():
        print(f"{key}: {value}")