prod_name=input("Enter product name:")
price=int(input("Enter price:"))
qty=int(input("Enter quantity:"))
tot_price=price*qty
gst=int(input("Enter GST:"))
Final_Amount=tot_price+(tot_price*(gst/100))
print("Total price:",tot_price)
print("GST:",gst)
print("Final Amount:",Final_Amount)
