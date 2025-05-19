class Order:
    def __init__(self,order_id,status="pending"):
        self.order_id=order_id
        self.status=status
    def updated_status(self,new_status):
        self.status=new_status
    def show_status(self):
        print(f"Order {self.order_id} status:{self.status}")
o=Order("ORD123")
o.updated_status("shipped")
o.show_status()