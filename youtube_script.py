from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver instance
driver = webdriver.Chrome(executable_path='C:/Drivers/chromedriver.exe')

# Navigate to youtube
driver.get('https://www.youtube.com/')

# Find the search bar and enter the search term
search_bar = driver.find_element(By.XPATH,
                                 '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div['
                                 '1]/div[1]/input')
search_bar.send_keys('The Real Slim Shady')

# Find the search button and click it
search_button = driver.find_element(By.XPATH,
                                    '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div['
                                    '2]/ytd-searchbox/button/yt-icon')
search_button.click()

# Wait for the first video to load
wait = WebDriverWait(driver, 10)
video = wait.until(EC.presence_of_element_located((By.XPATH,
                                                   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div['
                                                   '1]/ytd-two-column-search-results-renderer/div/ytd-section-list'
                                                   '-renderer/div[2]/ytd-item-section-renderer/div['
                                                   '3]/ytd-video-renderer[1]/div[1]/div/div['
                                                   '1]/div/h3/a/yt-formatted-string')))

# Click on the first video
video.click()



