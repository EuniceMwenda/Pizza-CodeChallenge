from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Create restaurants
    restaurant1 = Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201")
    restaurant2 = Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019")
    db.session.add_all([restaurant1, restaurant2])
    db.session.commit()

    # Create pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([pizza1, pizza2])
    db.session.commit()

    # Create restaurant pizzas
    restaurant_pizza1 = RestaurantPizza(price=10, pizza=pizza1, restaurant=restaurant1)
    restaurant_pizza2 = RestaurantPizza(price=12, pizza=pizza2, restaurant=restaurant1)
    restaurant_pizza3 = RestaurantPizza(price=15, pizza=pizza1, restaurant=restaurant2)
    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
