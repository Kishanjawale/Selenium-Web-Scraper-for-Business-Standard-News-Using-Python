from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init
import socket

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def extract_and_print_data(driver, xpath_expression, important_keywords):
    wait = WebDriverWait(driver, 10)
    matching_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_expression)))

    # Extract text content from each matching element
    all_data = [element.text for element in matching_elements]

    # Print the extracted data with highlighting for important news
    print("___________________________________Todays Latest News__________________________________")
    for data in all_data:
        if any(keyword in data.lower() for keyword in important_keywords):
            print(Fore.GREEN + Style.BRIGHT + data)  # Print with green and bright text for important news
        else:
            print(data)
        print("---------------------------------------------------------------------------------------")

def main():
    # Check network connectivity
    if is_connected():
        print("Connected to the network......")

        # Initialize colorama
        init(autoreset=True)

        # List of websites to visit
        #Moneycontrol news link : https://www.moneycontrol.com/news/business/stocks/
        #Moneycontrol Xpaths  //section[@class="mid-contener contener clearfix"]//li[@class ="clearfix"]//a[1]
        websites = [
            {'url': 'https://www.business-standard.com/', 'xpath': '//div[@class="cardlist"]//p[@class="smallcard-title"]'},
            {'url': 'https://www.moneycontrol.com/news/business/stocks/', 'xpath': '//section[@class="mid-contener contener clearfix"]//li[@class ="clearfix"]//h2[1]'},
        ]

        chrome_driver_path = r"F:\\New Start\\Start Menu Customization\\chromedriver.exe"

        chrome_options = Options()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--ignore-certificate-errors')

        for website in websites:
            driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path), options=chrome_options)
            driver.get(website['url'])
            WebDriverWait(driver, 20)
            extract_and_print_data(driver, website['xpath'], ['Q2', 'Q3', 'result', 'up', 'rises','buy'])
            driver.quit()

    else:
        print("Not connected to the network.")

if __name__ == "__main__":
    main()
