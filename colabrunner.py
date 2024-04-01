from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
import os, time

URL = os.getenv('URL2')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

if __name__ == "__main__":
    # Main logic
    with SB(uc=True) as sb: 
        
        sb.open('https://replit.com/login') # Login block
        sb.click('button[name="Continue with Google"]')
        sb.save_screenshot('0000.png')

        sb.type('input[type="email"]', USER+'\n')
        sb.save_screenshot('0001.png')

        sb.sleep(5)
        sb.save_screenshot('0002.png')

        sb.type('input[type="password"]', PASSWORD+'\n')
        sb.sleep(5)
        sb.save_screenshot('0003.png') # End login block
            
        while 1:
        # Looping logic
            sb.open(URL) # Url to replit
            sb.save_screenshot('0004.png') # Test how sb handles url

            sb.sleep(5)
            sb.find_element("//button[.//span[contains(text(), 'Stop')]]")
            sb.type('body', Keys.CONTROL + Keys.ENTER)
            sb.save_screenshot('0005.png')