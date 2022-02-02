

class Village:
  def __init__(self, difficulty):
    self.difficulty = difficulty 
    self.upgrade = 0
  
  @staticmethod
  def buy_cost(difficulty):
    if difficulty == "HARD":
      return 1295
    return 1200

  def cost_multiplier(self):
    if self.upgrade == 1:
      return .9
    elif self.upgrade == 2:
      return .85
    return 1

  def purchase_upgrade(self):
    self.upgrade += 1

  def wants_upgrades(self):
    return self.upgrade < 2

  def upgrade_cost(self):
    if self.upgrade == 0:
      return self.monkey_business()
    return self.monkey_commerce()  

  
  def monkey_business(self):
    if self.difficulty == "HARD":
      return 540
    return 500

  def monkey_commerce(self):
    if self.difficulty == "HARD":
      return 540
    return 500