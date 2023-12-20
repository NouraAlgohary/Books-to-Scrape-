from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# A WebDriver instance
driver = webdriver.Chrome()

# Website url
url = "http://quotes.toscrape.com/"
driver.get(url)

quotes_list = []

# Class name for the class that contains quote information
class_name = '.quote'

page_number = 1

while True:
    print(f"Scraping page {page_number}")

    if page_number != 1:
        try:
            # Find the "Next" button and click it
            next_button = driver.find_element(By.XPATH, '//li[@class="next"]/a')
            next_button.click()
        except Exception as e:
            print(f"Exception: {type(e).__name__} - {e}. Refreshing the page and retrying click.")
            break

    # Get the updated list of books of the current page
    quotes = driver.find_elements(By.CSS_SELECTOR, class_name)


    for quote in quotes:
        text = quote.find_element(By.CSS_SELECTOR, '.text').text
        author = quote.find_element(By.CSS_SELECTOR, '.author').text
        tags = quote.find_elements(By.CSS_SELECTOR, '.tags')
        tags_list = [tag.text for tag in tags]

        quote_item = {
            "text": text,
            "author": author,
            "tags": tags_list
        }
        quotes_list.append(quote_item)

    page_number += 1

df = pd.DataFrame(quotes_list)

# Save the dataframe to a CSV file
df.to_csv('path-to-quotes/QuotesToScrape.csv', index=True)

# Close the browser
driver.quit()
