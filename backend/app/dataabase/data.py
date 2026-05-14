from typing import Literal
from datetime import date

CATEGORY_DEFINITIONS = {
    1: {
        "name": "Laptop",
        "fields": 
          {
              "cpu_type": (str, ...), 
              "ram_gb": (int, ...)
          }
        },
    2: {
        "name": "T-Shirt",
        "fields": 
          {
              "color": (str, ...), 
              "size": (Literal['S','M','L','XL'], ...)
          }
        },
    3: {
        "name": "Equipment",
        "fields": 
          {
              "voltage": (int, 220), 
              "warranty_expires_on": (date, ...)
          }
        }
}



PRODUCT_DATABASE = {
    101: 
    {
        "category_id": 1, 
        "sku": "DELL-XPS-15", 
        "price": 1899.99, 
        "attributes": 
        {
            "cpu_type": "Intel i9", 
            "ram_gb": 32
        }
      },
    202: 
    {
        "category_id": 2, 
        "sku": "PLAIN-WHITE-T", 
        "price": 15.50, 
        "attributes": 
        {
            "color": "White", 
            "size": "L"
        }
    },
    303: 
    {
        "category_id": 3,
        "sku": "CNC-MILL-01", 
        "price": 75000.00, 
        "attributes": 
        {
            "voltage": 220, 
            "warranty_expires_on": "2027-12-31"
        }
    }
}

TEST_DATA= {
    "1" : "Test Data"
}
