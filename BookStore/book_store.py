class Book:
    def __init__(self, book_id, author, title, price, stock):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.price = price
        self.stock = stock
        self.reviews = []
        
    
    def add_review(self, review):
        self.reviews.append(review)
    
    
    def update_stock(self, quantity):
        self.stock += quantity
        
  
  class Order:
      def __init__(self, user_id, items):
          self.order_id = self.generate_order_id()
          self.user_id = user_id
          self.items = items
          self.status = 'Pending'
          self.total_price = sum(item[0] * item[1] for item in items)
          
          
        def generate_order_id(self):
            pass
        
        
        def view_order_details(self):
            return {
                'order_id': self.order_id,
                'user_id': self.user_id,
                'items': self.items,
                'status': self.status,
                'total_price': self.total_price
            }
            
            
        def update_status(self, status):
            self.status = status
            

class ShoppingCart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []
        
        
    def add_item(self, book, quantity):
        self.items.append((book, quantity))
    
    
    def remove_item(self, book):
        self.items = [item for item in self.items if item[0] != book]
        # for item in self.items:
        #     if item[0] == book:
        #         self.items.remove(item)
        #         break
        
        
    def view_items(self):
        return self.items
    
    
    def clear(self):
        self.items = []
  
        
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.shopping_cart = ShoppingCart(self)
        self.orders = []
        
    
    def view_profile(self):
        return f'User: {self.name}, Email: {self.email}'
    
    
    def edit_profile(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
            
            
    def place_order(self):
        if not self.shopping_cart.items:
            return None
        order = Order(self.user_id, self.shopping_cart.items)
        self.orders.append(order)
        self.shopping_cart.clear()
        return order
    
    
    def view_order_history(self):
        return self.orders
            