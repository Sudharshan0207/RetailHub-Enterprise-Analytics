from faker import Faker 
import random

fake = Faker()

Regions = ['North', 'South', 'East', 'West']

Segments=['Regular', 'Premium', 'Corporate']

Tiers=[ 'Silver', 'Gold', 'Platinum']

Channels=['Online', 'Store', 'Mobile']

Payment_Methods=['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash']

Products={
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Smartwatch', 'Camera', 'Tablet', 'Gaming Console', 'Bluetooth Speaker', 'Printer', 'Router'],
    'Fashion': ['T-shirt', 'Jeans', 'Sneakers', 'Dress', 'Jacket', 'Sunglasses', 'Handbag', 'Watch', 'Belt', 'Scarf'],
    'Home & Kitchen': ['Blender', 'Microwave', 'Vacuum Cleaner', 'Coffee Maker', 'Toaster', 'Air Fryer', 'Cookware Set', 'Cutlery Set', 'Dinnerware Set', 'Food Processor'],
    'Sports': ['Football', 'Basketball', 'Tennis Racket', 'Yoga Mat', 'Dumbbells', 'Running Shoes', 'Cycling Helmet', 'Golf Club', 'Swimming Goggles', 'Fitness Tracker'],
    'Beauty': ['Lipstick', 'Foundation', 'Mascara', 'Eyeliner', 'Nail Polish', 'Perfume', 'Face Cream', 'Hair Shampoo', 'Body Lotion', 'Makeup Brush Set','Sunscreen'],
    'Grocery': ['Rice', 'Wheat Flour', 'Sugar', 'Salt', 'Cooking Oil', 'Tea', 'Coffee', 'Pasta', 'Cereal', 'Spices'],
    'Books': ['Fiction', 'Non-fiction', 'Science Fiction', 'Biography', 'Self-help', 'Mystery', 'Romance', 'Fantasy', 'History', 'Children\'s Books'],
    'Toys': ['Action Figures', 'Dolls', 'Board Games', 'Puzzles', 'Building Blocks', 'Remote Control Cars', 'Stuffed Animals', 'Educational Toys', 'Outdoor Play Equipment', 'Arts and Crafts Kits'],
    'Furniture': ['Sofa', 'Dining Table', 'Bed Frame', 'Wardrobe', 'Coffee Table', 'Bookshelf', 'TV Stand', 'Desk', 'Chair', 'Dresser'],
    'Automotive': ['Car Battery', 'Tire', 'Brake Pads', 'Oil Filter', 'Spark Plug', 'Windshield Wiper', 'Headlight Bulb', 'Car Cover', 'Car Vacuum Cleaner', 'Car Air Freshener'],
    'Pet Supplies': ['Dog Food', 'Cat Food', 'Bird Cage', 'Fish Tank', 'Pet Bed', 'Dog Toy', 'Cat Litter', 'Pet Carrier', 'Animal Collar', 'Veterinary Care']

}

Brands={
    'Electronics': ['Apple', 'Samsung', 'Sony', 'LG', 'Dell', 'HP', 'Lenovo', 'Asus', 'Microsoft',],
    'Fashion': ['Nike', 'Adidas', 'Puma', 'Levi\'s', 'Zara', 'H&M', 'Gucci', 'Prada', 'Louis Vuitton'],
    'Home & Kitchen': ['Philips', 'Panasonic', 'KitchenAid', 'Cuisinart', 'Breville', 'Tefal', 'Bosch', 'Whirlpool', 'Samsung'],
    'Sports': ['Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour', 'New Balance', 'ASICS', 'Mizuno', 'Salomon', 'Decathlon'],
    'Beauty': ['L\'Oreal', 'Maybelline', 'Revlon', 'Nivea', 'Dove', 'Garnier', 'Clinique', 'Estée Lauder', 'MAC'],
    'Grocery': ['Nestle', 'Kellogg\'s', 'PepsiCo', 'Unilever', 'Danone', 'General Mills', 'Mars', 'ConAgra', 'Campbell\'s'],
    'Books': ['Penguin Random House', 'HarperCollins', 'Simon & Schuster', 'Hachette Book Group', 'Macmillan Publishers', 'Scholastic', 'Oxford University Press', 'Cambridge University Press', 'Wiley'],
    'Toys': ['LEGO', 'Mattel', 'Hasbro', 'Fisher-Price', 'Playmobil', 'Bandai', 'Spin Master', 'VTech', 'Melissa & Doug'],
    'Furniture': ['IKEA', 'Ashley Furniture', 'Wayfair', 'La-Z-Boy', 'Herman Miller', 'Steelcase', 'West Elm', 'Crate & Barrel', 'Pottery Barn'],
    'Automotive': ['Bosch', 'Denso', 'Magneti Marelli', 'Valeo', 'Continental', 'ZF Friedrichshafen', 'Delphi Technologies', 'Aisin Seiki', 'Mahle'],
    'Pet Supplies': ['Purina', 'Hill\'s Science Diet', 'Royal Canin', 'Blue Buffalo', 'Wellness', 'Nutro', 'Iams', 'Pedigree', 'Eukanuba']  
}
