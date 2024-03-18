from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
import os, time

url = 'https://colab.research.google.com/drive/1Ga2z2yIvOgJYy5auON27yfNaNqGny_Pg'

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

if __name__ == "__main__":
    
    while 1:

        time.sleep(60*60*3) # sleep 3h
        # cookies test - logging in.
        with SB(uc=True) as sb: 
            
            sb.open(url)


            sb.type('input[type="email"]', USER+'\n')
            sb.save_screenshot('0000.png')

            sb.sleep(5)
            sb.save_screenshot('0001.png')


            sb.type('input[type="password"]', PASSWORD+'\n')
            sb.sleep(5)
            sb.save_screenshot('0003.png')
            
            sb.sleep(60)
            sb.type('body', Keys.CONTROL + Keys.ENTER)
            sb.save_screenshot('0004.png')
            
            sb.save_cookies('cookies')

            sb.sleep()
        
        with SB(uc=True) as sb: 

            sb.open(url)
            sb.load_cookies('cookies')
            sb.refresh()
            sb.sleep(5)

            sb.type('body', Keys.CONTROL + Keys.ENTER)
            sb.save_screenshot('0005.png')