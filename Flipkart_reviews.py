import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initializing the empty list
data_list = []

# Creating a function
def get_page():
    # Setting the base page URL and total pages to scrape.
    number_of_pages = 400
    base_url = "https://www.flipkart.com/motorola-edge-40-neo-peach-fuzz-128-gb/product-reviews/itm6fb5c2c795a3d?pid=MOBGW6JJ4ZJHVGXE&lid=LSTMOBGW6JJ4ZJHVGXE5ZQ3A2&marketplace=FLIPKART&page=1"
    
    # Loop
    for page in range(1, number_of_pages + 1):
        url = f'https://www.flipkart.com/motorola-edge-40-neo-peach-fuzz-128-gb/product-reviews/itm6fb5c2c795a3d?pid=MOBGW6JJ4ZJHVGXE&lid=LSTMOBGW6JJ4ZJHVGXE5ZQ3A2&marketplace=FLIPKART&page={page}'
        
        response = requests.get(url)
        page_status = response.status_code
        print(f"For Page number {page} :-  Checking the status code which is: {page_status}")
        
        if page_status == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Navigate to the class which has the information we need.
            main_review_boxes = soup.find_all('div', {'class': 'col _2wzgFH K0kLPL'})
            
            # Extracting information from each container
            for element in main_review_boxes:
                title = element.find('p', {'class': '_2-N8zT'}).text.strip()
                rating_element = element.find('div', {'class': ''})
                rating = rating_element.text.strip() if rating_element else 'N/A'
                
                # Use a partial match for the class attribute
                reviews_element = element.find('div', class_=lambda x: x and '_3LWZlK' in x and '_1BLPMq' in x)
                reviews = reviews_element.text.strip() if reviews_element else 'N/A'
                
                # Creating a dictionary for each review
                data = {
                    'Title': title,
                    'Rating': rating,
                    'Reviews': reviews
                }
                
                # Appending the dictionary to the data_list
                data_list.append(data)

# Calling the function
get_page()

# Converting the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(data_list)

# Print the DataFrame
print(df)

# Save the results to csv
df.to_csv(r"C:\Users\Amit\Desktop/Filpkart_reviews.csv" , index=False)
