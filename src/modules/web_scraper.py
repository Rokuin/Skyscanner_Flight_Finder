# modules/web_scraper.py

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time

class SkyscannerScraper:
    def __init__(self):
        edge_options = Options()
        edge_options.add_argument("--start-maximized")
        # Uncomment the next line if you want to run Edge in headless mode
        # edge_options.add_argument("--headless")
        
        service = Service('C:\\Program Files (x86)\\edgedriver_win64\\msedgedriver.exe')
        self.driver = webdriver.Edge(service=service, options=edge_options)
        self.base_url = "https://www.skyscanner.com"

    def search_flights(self, departure, arrival, depart_date, return_date):
        try:
            self.driver.get(self.base_url)
            
            # Wait for the search form to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "fsc-origin-search"))
            )

            # Input departure city
            self._input_location("fsc-origin-search", departure)

            # Input arrival city
            self._input_location("fsc-destination-search", arrival)

            # Select dates
            self._select_dates(depart_date, return_date)

            # Click search button
            search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            search_button.click()

            # Wait for results to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "FlightsResults_dayViewItems__ZWE3Y"))
            )

            print(f"Search completed for {departure} to {arrival} from {depart_date} to {return_date}")
            
            # Here you would implement the logic to extract flight data
            # For now, we'll just print a success message
            return "Flight data extraction not implemented yet"

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def _input_location(self, element_id, location):
        input_field = self.driver.find_element(By.ID, element_id)
        input_field.clear()
        input_field.send_keys(location)
        time.sleep(1)  # Wait for suggestions to appear
        input_field.send_keys(Keys.RETURN)

    def _select_dates(self, depart_date, return_date):
        # Click on the departure date button to open the date picker
        depart_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.DATA_TESTID, "depart-btn"))
        )
        depart_btn.click()

        # Select the departure date
        self._select_date(depart_date)

        # Select the return date
        self._select_date(return_date)

    def _select_date(self, date):
        date_obj = datetime.strptime(date, "%Y/%m/%d")
        month_year = date_obj.strftime("%B %Y")
        day = str(date_obj.day)

        while True:
            current_month_year = self.driver.find_element(By.CLASS_NAME, "BpkCalendarNav_bpk-calendar-nav__MDg0Z").text
            if month_year in current_month_year:
                day_elements = self.driver.find_elements(By.CSS_SELECTOR, f"[aria-label*='{date_obj.strftime('%A, %B %-d, %Y')}']")
                for element in day_elements:
                    if element.text == day:
                        element.click()
                        return
                raise Exception(f"Day {day} not found in {month_year}")
            else:
                next_month_btn = self.driver.find_element(By.XPATH, "//button[@aria-label='Next Month']")
                next_month_btn.click()

    def close(self):
        self.driver.quit()