

class BananaFarm:
  def __init__(self, difficulty):
    self.difficulty = difficulty
    self.upgrade = 0
  
  def generate_money(self):
    if self.upgrade == 0:
      return 80
    elif self.upgrade == 1:
      return 120
    elif self.upgrade == 2:
      return 160
    elif self.upgrade == 3 or self.upgrade == 4:
      return 320
    return 400

  def upgrade_level(self):
    return self.upgrade

  def wants_upgrades(self):
    return self.upgrade < 4

  def purchase_upgrade(self):
    self.upgrade += 1

  @staticmethod
  def buy_cost(difficulty):
    if difficulty == "HARD":
      return 1350
    return 1250
  
  def upgrade_cost(self):
    if self.upgrade == 0:
      return self.increased_production()
    elif self.upgrade == 1:
      return self.greater_production()
    elif self.upgrade == 2:
      return self.banana_plantation()
    elif self.upgrade == 3:
      return self.long_life_bananas()
    else:
      return self.valuable_bananas()
    

  def increased_production(self):
    if self.difficulty == "HARD":
      return 540
    return 500
  
  def greater_production(self):
    if self.difficulty == "HARD":
      return 650
    return 600

  def banana_plantation(self):
    if self.difficulty == "HARD":
      return 3240
    return 3000

  def long_life_bananas(self):
    if self.difficulty == "HARD":
      return 325
    return 300

  def valuable_bananas(self):
    if self.difficulty == "HARD":
      return 865
    return 800




