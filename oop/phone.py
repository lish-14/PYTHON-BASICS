from item import Item


class Phone(Item):
   
    def __init__(self, name: str, price: float, quantity=0, broken_phones =0):
        # Call to super function to have access to all attribues
        super().__init__(
            name, price, quantity 
        )
        
        
        # Run valiDATIONS TO THE RECEIVED ARGUMENTS
        assert quantity >=0, f"broken Phones {broken_phones} is not greater than or equal to zero!"
        
        # Assign to self object
        self.broken_phones = broken_phones


