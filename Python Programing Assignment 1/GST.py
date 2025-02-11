#Write a Python program to calculate GST Goods and Service Tax
Item=input("Enter item name:")
sp_cost=float(input("How much is selling price: "))
gst_rate=float(input("The GST rate %: "))
cgst=sp_cost*((gst_rate/2)/100)
sgst=cgst
amt=sp_cost+cgst*sgst
print("CGST:",cgst)
print("SGST:",sgst)
print("Amount Payable",amt)