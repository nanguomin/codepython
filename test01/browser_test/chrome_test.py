from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    # browser = webdriver.chrome(executable_path ="C:\soft\python\chromedriver.exe")
    browser = webdriver.Chrome(
        executable_path=('D:\softapp\idea\chrome\chromedriver_win32\chromedriver.exe'))
    browser.get('https://kyfw.12306.cn/otn/resources/login.html')
    # browser.find_element_by_id("uh-signin").click()
    pass