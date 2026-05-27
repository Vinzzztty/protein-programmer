"""
Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation: 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
"""

import pandas as pd

data = {
    "product_id": [0, 1],
    "store1": [95, 70],
    "store2": [100, None],
    "store3": [105, 80],
}

product_df = pd.DataFrame(data)


def rearrange_products_table(products):
    # create an empty list rearranged rows
    rearranged_rows = []

    # Iterate each row in original table products
    for _, row in products.iterrows():
        product_id = row["product_id"]

        # Checkn store for price availability
        for store_col in ["store1", "store2", "store3"]:
            price = row[store_col]

            if pd.notna(price):
                rearranged_rows.append((product_id, store_col, price))

    result_table = pd.DataFrame(
        rearranged_rows, columns=["product_id", "store", "price"]
    )

    return result_table


print(rearrange_products_table(product_df))
