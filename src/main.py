# main.py

import sys
from modules.user_input import get_user_input
from modules.web_scraper import SkyscannerScraper

def main():
    use_default = '--use-default' in sys.argv
    user_preferences = get_user_input(use_default)
    
    scraper = SkyscannerScraper()
    result = scraper.search_flights(
        departure=user_preferences['departure'],
        arrival=user_preferences['arrival'],
        depart_date=user_preferences['start_date'].strftime("%Y/%m/%d"),
        return_date=user_preferences['end_date'].strftime("%Y/%m/%d")
    )
    
    if result:
        print("Search results:", result)
    else:
        print("Failed to retrieve search results.")
    
    scraper.close()

if __name__ == "__main__":
    main()