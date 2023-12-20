# Toscrape

🛠️ Web Scraping Exploration with Selenium

Take a gentle dive into the basics of web scraping with this repository! Using Selenium, the project walks you through extracting data from books and quotes websites. 
It's a simple yet effective exercise to get hands-on experience with web scraping techniques. The data collected is neatly organized into a CSV file, offering a practical glimpse into data processing. 
Whether you're new to web scraping or just looking for a straightforward example, this repository provides a humble starting point for your exploration. Happy coding!



## [1. Books to Scrape](http://books.toscrape.com/)
![image](https://github.com/NouraAlgohary/Web-Scraping/assets/103903785/7a5c0b19-e620-4531-8714-6cc1c8b9fe55)

## [2. Quotes to Scrape](https://quotes.toscrape.com/)
![image](https://github.com/NouraAlgohary/Web-Scraping/assets/103903785/d34bbf5d-5799-47ec-8309-2f2f3911e199)

## Steps
### Setting Up Liberaries
Selenium is a powerful web automation library for Python, widely used for web scraping and testing.</br>
```pip install selenium```</br>
Pandas is a versatile data manipulation library in Python, commonly employed for data analysis and storage, such as saving data to CSV files.</br>
```pip install pandas```

### Getting Started
Create a webdriver instance</br>
```
driver = webdriver.Chrome()
url = "http://books.toscrape.com/"
driver.get(url)
```
Chrome must be loaded with the message</br>
```Chrome is being controlled by automated test software.```
### Explicit Waits
```
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
            # Explicitly wait for the next page button to be present
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(next_page_button_locator))

            # Explicitly wait for the next page button to be clickable
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(next_page_button_locator))

            # Find the next page button and click it
            next_page_button = driver.find_element(*next_page_button_locator)
            next_page_button.click()


        except Exception as e:
            print(f"Exception: {type(e).__name__} - {e}. Refreshing the page and retrying click.")
            driver.refresh()
```

### Data Extraction
Locaters using 
``` By.```
```from selenium.webdriver.common.by import By```
- ```find_element(By.CSS_SELECTOR, some_string)``` Finds element using CSS selector. It performs the same tasks as the old one. ```find_element_by_css_selector```
- ```find_element(By.XPATH, some_string)``` Finds elment by XPATH instead of ```find_element_by_xpath```
- ```find_element(By.CLASS_NAME, some_string)``` Finds element by Class Name as the old one did ```find_element_by_class_name```
  These methods return an instance of ```WebElement```
#### WebElement
- ```element.text``` Accessing text element
- ```element.click()``` Clicking on the element
- ```element.get_attribute(‘class’)``` Accessing attribute class, title...etc

### Finally
Close the browser
```driver.quit()```
