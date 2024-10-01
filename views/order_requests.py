import sqlite3
import json
from models import Order

ORDERS = [
    {"metalId": 4, "sizeId": 4, "styleId": 2, "id": 1},
    {"metalId": 3, "sizeId": 5, "styleId": 1, "id": 2},
    {"metalId": 2, "sizeId": 2, "styleId": 2, "id": 3},
]


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            id,
            metal_id,
            size_id,
            style_id
        FROM Orders
        """
        )

        # Initialize an empty list to hold all animal representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            order = Order(
                row["id"],
                row["metal_id"],
                row["size_id"],
                row["style_id"],
            )

            orders.append(
                order.__dict__
            )  # see the notes below for an explanation on this line of code.

    return orders


def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            id,
            metal_id,
            size_id,
            style_id
        FROM Orders
        WHERE id = ?
        """,
            (id,),
        )

        data = db_cursor.fetchone()
        order = Order(data["id"], data["metal_Id"], data["size_Id"], data["style_Id"])
        return order.__dict__


def create_order(order):
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an 'id' property to the order dictionary
    order["id"] = new_id

    # Add the animal dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with 'id' property added
    return order


def delete_order(id):
    # Initial -1 value for the index in case one isn't found
    order_index = -1

    # Iterate the ORDERS list, use enumerate to access the
    # index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
