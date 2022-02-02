from money_from_rounds import money_from_rounds 
from BananaFarm import BananaFarm
from Village import Village

start_money = 650
difficulty = "HARD"
farm_count = 8

def village_first_max_farms():
  village = None
  money = start_money 
  farms = []
  village_cost = Village.buy_cost(difficulty)
  farm_cost = BananaFarm.buy_cost(difficulty)

  for current_round in range(80):
    if not village:
      if money > village_cost:
        village = Village(difficulty)
        money -= village_cost
    if village:
      while (village.wants_upgrades() and money > village.upgrade_cost()):
          money -= village.upgrade_cost()
          village.purchase_upgrade()
    
    if len(farms) == 0 and village:
      if money > farm_cost * village.cost_multiplier():
        farms.append(BananaFarm(difficulty))
        money -= farm_cost * village.cost_multiplier()
    if len(farms) > 0 and village:
      while (farms[-1].wants_upgrades() and money > farms[-1].upgrade_cost() * village.cost_multiplier()):
        money -= farms[-1].upgrade_cost() * village.cost_multiplier()
        farms[-1].purchase_upgrade()
      if len(farms) == farm_count and not farms[-1].wants_upgrades():
        break
      if not farms[-1].wants_upgrades():
        if money > farm_cost * village.cost_multiplier():
          farms.append(BananaFarm(difficulty))
          money -= farm_cost * village.cost_multiplier()
    for farm in farms:
      money += farm.generate_money()
    money += money_from_rounds[current_round]
  print("money:", money)
  return current_round

def farms_at_two_zero(farms):
  for farm in farms:
    if farm.upgrade_level() < 2:
      return False
  return True

def village_first_two_zero_farms():
  village = None
  money = start_money 
  farms = []
  village_cost = Village.buy_cost(difficulty)
  farm_cost = BananaFarm.buy_cost(difficulty)

  for current_round in range(80):
    if not village:
      if money >= village_cost:
        village = Village(difficulty)
        money -= village_cost
    if village:
      while (village.wants_upgrades() and money >= village.upgrade_cost()):
          money -= village.upgrade_cost()
          village.purchase_upgrade()
    
    if len(farms) == 0 and village:
      if money >= farm_cost * village.cost_multiplier():
        farms.append(BananaFarm(difficulty))
        money -= farm_cost * village.cost_multiplier()
    if len(farms) > 0 and village:
      while len(farms) < farm_count:
        while not farms_at_two_zero(farms):
          if money >= farms[-1].upgrade_cost() * village.cost_multiplier():
            money -= farms[-1].upgrade_cost() * village.cost_multiplier()
            farms[-1].purchase_upgrade()
          else:
            break
        if farms_at_two_zero(farms):
          if money >= farm_cost * village.cost_multiplier():
            farms.append(BananaFarm(difficulty))
            money -= farm_cost * village.cost_multiplier()
          else:
            break
        else:
          break
      while not farms_at_two_zero(farms):
        while farms[-1].upgrade_level() < 2:
          if money >= farms[-1].upgrade_cost() * village.cost_multiplier():
            money -= farms[-1].upgrade_cost() * village.cost_multiplier()
            farms[-1].purchase_upgrade()
          else:
            break
        if money < farms[-1].upgrade_cost() * village.cost_multiplier():
          break
      if len(farms) == farm_count:
        if not farms[-1].wants_upgrades():
          break
        elif farms_at_two_zero(farms):
          for farm in farms:
            while farm.wants_upgrades() and money >= farm.upgrade_cost() * village.cost_multiplier():
              money -= farm.upgrade_cost() * village.cost_multiplier()
              farm.purchase_upgrade()              
            if farm.wants_upgrades():
              break
    for farm in farms:
      money += farm.generate_money()
    money += money_from_rounds[current_round]
  print("money:", money)
  return current_round

def two_zero_farms_then_village():
  village = None
  money = start_money 
  farms = []
  village_cost = Village.buy_cost(difficulty)
  farm_cost = BananaFarm.buy_cost(difficulty)

  for current_round in range(80):
    if len(farms) == 0:
      if money >= farm_cost:
        farms.append(BananaFarm(difficulty))
        money -= farm_cost
    if len(farms) > 0:
      while len(farms) < farm_count:
        while not farms_at_two_zero(farms):
          if money >= farms[-1].upgrade_cost():
            money -= farms[-1].upgrade_cost()
            farms[-1].purchase_upgrade()
          else:
            break
        if farms_at_two_zero(farms):
          if money >= farm_cost:
            farms.append(BananaFarm(difficulty))
            money -= farm_cost
          else:
            break
        else:
          break
      while not farms_at_two_zero(farms):
        while farms[-1].upgrade_level() < 2:
          if money >= farms[-1].upgrade_cost():
            money -= farms[-1].upgrade_cost()
            farms[-1].purchase_upgrade()
          else:
            break
        if money < farms[-1].upgrade_cost():
          break
      if len(farms) == farm_count:
        if not farms[-1].wants_upgrades():
          break
        elif farms_at_two_zero(farms):
          if not village:
            if money >= village_cost:
              village = Village(difficulty)
              money -= village_cost
          if village:
            while (village.wants_upgrades() and money >= village.upgrade_cost()):
                money -= village.upgrade_cost()
                village.purchase_upgrade()
            if not village.wants_upgrades():
              for farm in farms:
                while farm.wants_upgrades() and money >= farm.upgrade_cost() * village.cost_multiplier():
                  money -= farm.upgrade_cost() * village.cost_multiplier()
                  farm.purchase_upgrade()              
                if farm.wants_upgrades():
                  break
    for farm in farms:
      money += farm.generate_money()
    money += money_from_rounds[current_round]
  print("money:", money)
  return current_round

def two_zero_farms_no_village():
  money = start_money 
  farms = []
  farm_cost = BananaFarm.buy_cost(difficulty)

  for current_round in range(80):
    if len(farms) == 0:
      if money >= farm_cost:
        farms.append(BananaFarm(difficulty))
        money -= farm_cost
    if len(farms) > 0:
      while len(farms) < farm_count:
        while not farms_at_two_zero(farms):
          if money >= farms[-1].upgrade_cost():
            money -= farms[-1].upgrade_cost()
            farms[-1].purchase_upgrade()
          else:
            break
        if farms_at_two_zero(farms):
          if money >= farm_cost:
            farms.append(BananaFarm(difficulty))
            money -= farm_cost
          else:
            break
        else:
          break
      while not farms_at_two_zero(farms):
        while farms[-1].upgrade_level() < 2:
          if money >= farms[-1].upgrade_cost():
            money -= farms[-1].upgrade_cost()
            farms[-1].purchase_upgrade()
          else:
            break
        if money < farms[-1].upgrade_cost():
          break
      if len(farms) == farm_count:
        if not farms[-1].wants_upgrades():
          break
        elif farms_at_two_zero(farms):
          for farm in farms:
            while farm.wants_upgrades() and money >= farm.upgrade_cost():
              money -= farm.upgrade_cost()
              farm.purchase_upgrade()              
            if farm.wants_upgrades():
              break
    for farm in farms:
      money += farm.generate_money()
    money += money_from_rounds[current_round]
  print("money:", money)
  return current_round

def max_farms_no_village():
  money = start_money 
  farms = []
  farm_cost = BananaFarm.buy_cost(difficulty)

  for current_round in range(80):
    if len(farms) == 0:
      if money > farm_cost:
        farms.append(BananaFarm(difficulty))
        money -= farm_cost
    if len(farms) > 0:
      while (farms[-1].wants_upgrades() and money > farms[-1].upgrade_cost()):
        money -= farms[-1].upgrade_cost()
        farms[-1].purchase_upgrade()
      if len(farms) == farm_count and not farms[-1].wants_upgrades():
        break
      if not farms[-1].wants_upgrades():
        if money > farm_cost:
          farms.append(BananaFarm(difficulty))
          money -= farm_cost
    for farm in farms:
      money += farm.generate_money()
    money += money_from_rounds[current_round]
  print("money:", money)
  return current_round

print("Results of running the simulation for", farm_count, "farms on", difficulty, "difficulty")
print("----------------------------------")
print("village first max farms",village_first_max_farms())
print("village first then two zero farms before max",village_first_two_zero_farms())
print("two zero farms then village",two_zero_farms_then_village())
print("two zero farms then max no village",two_zero_farms_no_village())
print("max farms no village",max_farms_no_village())




