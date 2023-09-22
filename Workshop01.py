
# 1.จงเขขียนโปรแกรม Python คำนวณหาราคาขายสินค้าโดยรับฃื่อสินค้าและราคาสินค้า(ต้นทุน)
# ทางแป้นพิมพ์แล้วคำนวณหาราคาขายของสินค้าโดยราคาขายสินค้าจะคิดเพิ่มจากราคาสินค้า (ต้นทุน) ร้อยละ 10
# สูตร ราคาขายสินค้า = ราคาสินค้า(ต้นนทุน) + (ราคาสินค้า(ต้นทุน) * 10/100)

def calculate_sale_price(cost_price):
   markup_percentage = 10  # อัตราการเพิ่มราคาขาย 10%
   sale_price = cost_price + (cost_price * markup_percentage / 100)
   return sale_price

def get_product_info():
   product_name = input("กรุณาใส่ชื่อสินค้า: ")
   cost_price = float(input("กรุณาใส่ราคาสินค้า (ต้นทุน): "))
   return product_name, cost_price

def display_result(product_name, cost_price, sale_price):
   print(f"ชื่อสินค้า: {product_name}")
   print(f"ราคาสินค้า (ต้นทุน): {cost_price} บาท")
   print(f"ราคาขายสินค้า: {sale_price:.2f} บาท")

product_name, cost_price = get_product_info()
sale_price = calculate_sale_price(cost_price)
display_result(product_name, cost_price, sale_price)