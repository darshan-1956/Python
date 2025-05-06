products = {}
def add_product(product_id, name, price, quantity):
  products[product_id] = {
'name': name,
'price': price,
'quantity': quantity
}
def update_stock(product_id, quantity):
  if product_id in products:
    products[product_id]['quantity'] += quantity
  else:
    print("Product ID not found")
def get_product_info(product_id):
  if product_id in products:
    return products[product_id]
  else:
    return "Product not found"