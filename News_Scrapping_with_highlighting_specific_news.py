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

# Check network connectivity
if is_connected():
    print("Connected to the network......")
        

    # Initialize colorama
    init(autoreset=True)


    website_url_business_standards = 'https://www.business-standard.com/'
    

    chrome_driver_path = r"F:\\New Start\\Start Menu Customization\\chromedriver.exe"


    chrome_options = Options()
    #chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path), options=chrome_options)

    driver.get(website_url_business_standards)

    xpath_expression = '//div[@class="cardlist"]//p[@class="smallcard-title"]'

    wait = WebDriverWait(driver, 10)
    matching_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_expression)))

    # Extract text content from each matching element
    all_data = [element.text for element in matching_elements]

    # Print the extracted data with highlighting for important news
    print("___________________________________Todays Latest News__________________________________")
    for data in all_data:
        if any(keyword in data for keyword in ['Q2', 'Q3', 'result','up','rises']):
            print(Fore.RED + Style.BRIGHT + data)  # Print with red and bright text for important news
        else:
            print(data)
        print("---------------------------------------------------------------------------------------")

    driver.quit()

else:
    print("Not connected to the network.")







