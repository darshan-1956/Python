import product
import sales
product.add_product(101, "Notebook", 50.0, 100)
product.add_product(102, "Pen", 10.0, 200)
print(product.get_product_info(101))
print(sales.sell_product(101, 2))
print(sales.sell_product(102, 5))
print(product.get_product_info(101))
print(sales.show_sales())