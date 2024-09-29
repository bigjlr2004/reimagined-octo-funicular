ORDERS = [
    {
      "metalId": 4,
      "sizeId": 4,
      "styleId": 2,
      "id": 1
    },
    {
      "metalId": 3,
      "sizeId": 5,
      "styleId": 1,
      "id": 2
    },
    {
      "metalId": 2,
      "sizeId": 2,
      "styleId": 2,
      "id": 3
    }
  ]

def get_all_orders():
   return ORDERS

def get_single_order(id):
   selected_order = None
   for order in ORDERS:
      if order["id"] == id:
         selected_order = order
   return selected_order

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