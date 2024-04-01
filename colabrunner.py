from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
import os, time

URL = os.getenv('URL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

if __name__ == "__main__":
    # Main logic
    with SB(uc=True) as sb: 
        
        sb.open('https://replit.com/login') # Login block
        sb.click("//button[contains(., 'Continue with Google')]")

        sb.type('input[type="email"]', USER+'\n')

        sb.sleep(5)

        sb.type('input[type="password"]', PASSWORD+'\n')
        sb.sleep(5) # End login block
            
        while 1:
        # Looping logic
            sb.open(URL) # Url to replit

            sb.sleep(5)
            sb.find_element("//button[.//span[contains(text(), 'Stop')]]")
            sb.type('body', Keys.CONTROL + Keys.ENTER)