"""
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

"""

import pandas as pd

# Creating the DataFrame
data = {
    "product_id": [0, 1, 2, 3, 4],
    "low_fats": ["Y", "Y", "N", "Y", "N"],
    "recyclable": ["N", "Y", "Y", "Y", "N"],
}

products_df = pd.DataFrame(data)


def find_products(products):
    return products[(products.low_fats == "Y") & (products.recyclable == "Y")][
        ["product_id"]
    ]


print(find_products(products_df))
