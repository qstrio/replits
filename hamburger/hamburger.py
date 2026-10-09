class Hamburger:

  def __init__(self,toppings,patty_type,bun_type):
    self.__toppings = toppings
    self.__patty_type = patty_type
    self.__bun_type = bun_type
  
  # complete getters
  
  def getToppings(self):
    return self.__toppings

  def getPatty(self):
    return self.__patty_type

  def getBun(self):
    return self.__bun_type

  def total_price(self):
    total = self.__toppings_price() + self.__patty_price() + self.__bun_price()
    return "Your burger costs $" + str(total)

  def __toppings_price(self):
    price = 0

    if "tomato" in self.__toppings:
      price += 0.3
    if "lettuce" in self.__toppings:
      price += 0.1
    if "onions" in self.__toppings:
      price += 0.2
    if "caramalized onions" in self.__toppings:
      price += 0.4
    
    return price
  
  def __patty_price(self):
    price = 0

    if self.__patty_type == "beef":
      price += 5
    elif self.__patty_type == "chicken" or self.__patty_type == "turkey":
      price += 6
    elif self.__patty_type == "veggie":
      price += 7
    
    return price

  def __bun_price(self):
    price = 0

    if self.__bun_type == "gluten free":
      price += 1.5
    else:
      price += 0.5
      
    return price