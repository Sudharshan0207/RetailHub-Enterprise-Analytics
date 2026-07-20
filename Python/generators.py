import pandas as pd
import random

from faker import Faker

from config import *
from utils import *

fake = Faker('en_IN')

def generate_customers_data():
    CustomersData = []
    for i in range(NUM_CUSTOMERS):

        CustomersData.append({

            'CustomerCode': f'CUST{i+1:05}',

            'FirstName': fake.first_name(),

            'LastName': fake.last_name(),

            'Gender': random.choice(['Male', 'Female']),

            'DateOfBirth': fake.date_of_birth(minimum_age=18, maximum_age=60),

            'Email': fake.unique.email(),

            'Phone': fake.phone_number(),

            'City': fake.city(),

            'State': fake.state(),

            'Region': random.choice(Regions),

            'JoiningDate': fake.date_between(start_date='-5y', end_date='today'),
            
            'CustomerSegment': random.choice(Segments),

        })

    
    df = pd.DataFrame(CustomersData)

    df.to_csv('Dataset/CustomersData.csv', index=False)

    print("Customers Data Generated and Saved to CustomersData.csv")

    return df 


def generate_categories_data():

    CategoriesData = [
        ['Electronics', 'Electronics gadgets and devices'],
        ['Fashion', 'Clothing, footwear, and accessories'],
        ['Home & Kitchen', 'Home appliances, furniture, and kitchenware'],
        ['Sports', 'Sports equipment and outdoor gear'],
        [' Beauty', 'personal care and  beauty products'],
        ['Toys', 'Kids Toys and  games'],
        ['Books', 'Books, magazines, and media products'],
        ['Automotive', 'Automotive parts and accessories'],
        ['Grocery', 'Grocery items and gourmet food products'],
        ['Pet Supplies', 'Pet food, toys, and accessories'],
        ['Furniture', 'Furniture and home decor items']
    ]

    
    df1 = pd.DataFrame(
        CategoriesData
        , columns=['CategoryName', 'CategoryDescription']
        )

    df1.to_csv('Dataset/CategoriesData.csv', index=False)

    print("Categories Data Generated and Saved to CategoriesData.csv")

    return df1