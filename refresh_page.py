from selenium import webdriver
import time


page = input('URL: ')
tempo = int(input('Time to refresh page: '))

chrome = webdriver.Chrome()
chrome.get('http://'+page)

while True:
    time.sleep(tempo)
    chrome.refresh()
