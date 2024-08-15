"""
Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

"""

import pandas as pd

customers = {
    "id": [1, 2, 3, 4],
    "name": ["Joe", "Henry", "Sam", "Max"],
}

orders = {
    "id": [1, 2],
    "customerId": [3, 1],
}

customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)


def find_customers(customers, orders):
    # Select customers whose 'id' not present in table orders in 'customerId' column
    df = customers[~customers["id"].isin(orders["customerId"])]

    # Make a dataframe only contains 'name' and rename to Customers
    df = df[["name"]].rename(columns={"name": "Customers"})

    return df


print(find_customers(customers_df, orders_df))
