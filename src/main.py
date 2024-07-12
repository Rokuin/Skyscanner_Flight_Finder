# main.py

from modules.user_input import get_user_input

def main():
    user_preferences = get_user_input()
    print("\nFlight search parameters:")
    for key, value in user_preferences.items():
        print(f"{key}: {value}")
    print("\nThank you for using Flight Finder! We'll implement the search functionality in the next steps.")

if __name__ == "__main__":
    main()