import json
import boto3
import random
import time
from decimal import Decimal


def mock_data_generator():
    orderId=str(random.randint(1,10000))
    product_name=random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity = random.randint(1,5)
    price = Decimal(str(round(random.uniform(10.0,500.0),2)))
    
    return{
        'orderId':orderId,
        'product_name':product_name,
        'quantity':quantity,
        'price':price
    }

dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')
table = dynamodb.Table('ordersFact')

def lambda_handler(event, context):
    try:
        i=0
        while (i<50):
            data=mock_data_generator()
            print(data)
            table.put_item(Item=data)
            i=i+1
            time.sleep(1)
    except Exception as e:
        print('error is :',e)