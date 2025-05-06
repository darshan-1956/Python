import product

sales_log = []

def sell_product(product_id, quantity):
    if product_id in product.products:
        prod = product.products[product_id]
        if prod['quantity'] >= quantity:
            prod['quantity'] -= quantity
            total_price = prod['price'] * quantity
            sales_log.append({
                'product_id': product_id,
                'quantity': quantity,
                'total_price': total_price
            })
            return "Sold {} units. Total: {}".format(quantity, total_price)
        else:
            return "Insufficient stock"
    else:
        return "Product not found"

def show_sales():
    return sales_log
