from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
import os

url = 'https://colab.research.google.com/drive/1Ga2z2yIvOgJYy5auON27yfNaNqGny_Pg'

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

if __name__ == "__main__":
    
    with SB(uc=True) as sb:
        
        sb.open(url)


        sb.click('a[data-action="sign in"]')
        sb.type('input[type="email"]', USER)
        sb.save_screenshot('0000.png')

        sb.click('button:contains("Next")')
        sb.sleep(5)
        sb.save_screenshot('0001.png')


        sb.type('input[type="password"]', PASSWORD)
        sb.click('button:contains("Next")')
        sb.save_screenshot('0003.png')
        
        sb.sleep(60)
        sb.type('body', Keys.CONTROL + Keys.F9)
        sb.save_screenshot('0003.png')
        

        sb.sleep(3*60)