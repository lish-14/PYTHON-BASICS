from item import Item

item1 = Item("Myitem", 750)

item1.apply_increment(0.2)
item1.apply_discount()


print(item1.price)







#Setting an Attribute
item1.name = "OtherItem"

#Getting an Attribute
print(item1.name)



    
















