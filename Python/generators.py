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

    
    df = pd.DataFrame(
        CategoriesData
        , columns=['CategoryName', 'CategoryDescription']
        )

    df.to_csv('Dataset/CategoriesData.csv', index=False)

    print("Categories Data Generated and Saved to CategoriesData.csv")

    return df


def generate_products_data():

    ProductsData=[]

    Product_Id=1

    Category_names=['Electronics', 'Fashion', 'Home & Kitchen', 'Sports', 'Beauty', 'Grocery', 'Books', 'Toys', 'Furniture', 'Automotive', 'Pet Supplies']

    for Category_Id,category in enumerate(Category_names,start=1):

        for _ in range(20):

            Brand=random.choice(Brands[category])

            Product=random.choice(Products[category])

            Cost=random.randint(100,50000)
            
            Selling=round(Cost * random.uniform(1.1, 1.6), 2)

            ProductsData.append({

                'ProductId': f'PROD{Product_Id:05}',

                'ProductName': f" Brand: {Brand}  {Product}",

                'CategoryId':Category_Id,

                'Brand': Brand,

                'CostPrice': Cost,

                'SellingPrice': Selling,

                'LaunchDate': fake.date_between(start_date='-3y', end_date='today'),

                'IsActive': 1
            })

            Product_Id+=1
    
    df = pd.DataFrame(ProductsData)

    df.to_csv('Dataset/ProductsData.csv', index=False)

    print("Products Data Generated and Saved to ProductsData.csv")

    return df


def generate_stores_data():

    StoreData=[]

    Cities=[
        ('Hyderabad','Telangana','South'),
        ('Bangalore','Karnataka','South'),
        ('Chennai','Tamil Nadu','South'),
        ('Mumbai','Maharashtra','West'),
        ('Pune','Maharashtra','West'),
        ('Ahmedabad','Gujarat','West'),
        ('Jaipur','Rajasthan','West'),
        ('Delhi','Delhi NCR','North'),
        ('Gurgaon','Haryana','North'),
        ('Noida','Uttar Pradesh','North'),
        ('Lucknow','Uttar Pradesh','North'),
        ('Kolkata','West Bengal','East'),
        ('Bhubaneswar','Odisha','East'),
        ('Patna','Bihar','East')
        ]
    
    Store_types=['Flagship','Mall','Outlet','Express']


    for i in range(NUM_STORES):

        City, State, Region = random.choice(Cities)

        StoreData.append({

            'StoreId': f'STORE{i+1:03}',

            'StoreName': f"RetailHub {City} {i+1}",

            'City': City,

            'State': State,

            'Region': Region,

            'OpeningDate': fake.date_between(start_date='-5y', end_date='today'),

            'StoreType': random.choice(Store_types)
        })

    
    df = pd.DataFrame(StoreData)

    df.to_csv('Dataset/StoreData.csv', index=False)

    print("Store Data Generated and Saved to StoreData.csv")

    return df


def generate_employees_data():

    Departments=['Sales','Marketing','Finance','Human Resources','IT','Operations']

    Designations=['Manager','Executive','Analyst','Coordinator','Specialist']

    EmployeeData=[]

    for i in range(NUM_EMPLOYEES):

        EmployeeData.append({

            'EmployeeId': f'EMP{i+1:04}',

            'FirstName': fake.first_name(),

            'LastName': fake.last_name(),

            'Department': random.choice(Departments),

            'Designation': random.choice(Designations),

            'StoreId':random.randint(1,NUM_STORES),

            'HireDate': fake.date_between(start_date='-5y', end_date='-1m'),

            'Salary': round(random.randint(20000, 100000),2),
        })


    df = pd.DataFrame(EmployeeData)

    df.to_csv('Dataset/EmployeesData.csv', index=False)

    print("Employee Data Generated and Saved to EmployeeData.csv")

    return df


def generate_suppliers_data():

    SuppliersData=[]

    for i in range(NUM_SUPPLIERS):

        SuppliersData.append({

            'SupplierId': f'SUPP{i+1:03}',

            'SupplierCode': f'SUPP{i+1:04}',

            'SupplierName': fake.company(),

            'ContactName': fake.name(),

            'Email': fake.company_email(),

            'Phone': fake.phone_number(),

            'City': fake.city(),

            'State': fake.state(),

            'Country': 'India',

            'Rating': round(random.uniform(1.0, 5.0), 1),
            
        })


    df = pd.DataFrame(SuppliersData)

    df.to_csv('Dataset/SuppliersData.csv', index=False)

    print("Suppliers Data Generated and Saved to SuppliersData.csv")

    return df


def generate_warehouses_data():

    Cities=[
        ('Hyderabad','Telangana','South'),
        ('Bangalore','Karnataka','South'), 
        ('Mumbai','Maharashtra','West'),
        ('Kolkata','West Bengal','East'),
        ('Delhi','Delhi NCR','North')

    ]

    WarehousesData=[]

    for i in range(NUM_WAREHOUSES):

        City, State, Region = Cities[i]

        WarehousesData.append({

            'WarehouseId': f'WH{i+1:03}',

            'WarehouseCode': f'WH{i+1:04}',

            'WarehouseName': f"RetailHubWarehouse {i+1}",

            'City': City,

            'State': State,

            'Region': Region,

            'Capacity': random.randint(1000, 10000)\
        })


    df = pd.DataFrame(WarehousesData)

    df.to_csv('Dataset/WarehousesData.csv', index=False)

    print("Warehouses Data Generated and Saved to WarehousesData.csv")

    return df


def generate_inventory_data():

    InventoryData=[]

    Inventory_Id=1

    for ProductId  in range(1, NUM_PRODUCTS + 1):

        for WarehouseId in range(1, NUM_WAREHOUSES + 1):

            Stock_Quantity = random.randint(10, 1000)

            InventoryData.append({

                'ProductId': ProductId,

                'WarehouseId': WarehouseId,

                'StockQuantity': Stock_Quantity,

                'ReorderLevel': random.randint(5, 50),

                'LastUpdated': fake.date_between(start_date='-30d', end_date='today')
            })

            Inventory_Id += 1

    df = pd.DataFrame(InventoryData)

    df.to_csv('Dataset/InventoryData.csv', index=False)

    print("Inventory Data Generated and Saved to InventoryData.csv")

    return df