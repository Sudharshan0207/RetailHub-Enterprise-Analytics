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

    df.to_csv('Data sets/CustomersData.csv', index=False)

    print("Customers Data Generated and Saved to CustomersData.csv")

    return df 