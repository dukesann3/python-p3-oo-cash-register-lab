#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.inventory = []
  
  def get_discount(self):
    return self._discount

  def set_discount(self, discount):
    if isinstance(discount, (float, int)) or discount == 0:
      self._discount = discount
    else:
      raise TypeError("Discount needs to be either int or float")
  
  discount = property(get_discount, set_discount)

  def add_item(self, title, price, qty=1):
    if isinstance(title, str) and isinstance(price, (float, int)) and isinstance(qty, int):
      items_to_add = title
      items_to_add_to_inventory = {"title": title, "price": price}
      self.inventory.append(items_to_add_to_inventory)
      self.items = self.items + [items_to_add] * qty
      self.total = self.total + price * qty
    else:
      raise TypeError("Items must be correct data type")
  
  def apply_discount(self):
    discount_quotient = (100-self._discount)/100
    if discount_quotient != 1:
      self.total = self.total * discount_quotient
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    popped_item_name = self.items.pop(-1)
    price_of_last_item = 0
    for item in self.inventory:
      if item.get("title") == popped_item_name:
        price_of_last_item = item.get("price")
        self.items.pop()
        self.total = self.total - price_of_last_item





