from faker import Faker

import random

import file_operations


fake = Faker("ru_RU")

context = {
    "first_name": "Евсемпий",
    "last_name": "Пупидрович",
    "job": "Пархутехтор",
    "town" : "Маркувиль",
    "strength" : "5",
    "agility" : "5",
    "endurance" : "5",
    "intelligence" : "5",
    "luck" : "5",
    "skill_1" : "Навык 1",
    "skill_2" : "Навык 2",
    "skill_3" : "Навык 3",
  }
skills = ["Стремительный прыжок",
          "Электрический выстрел",
          "Ледяной удар",
          "Стремительный удар",
          "Кислотный взгляд",
          "Тайный побег",
          "Ледяной выстрел",
          "Огненный заряд"
          ]

choise_skills = random.sample(skills, 3)

context["first_name"] = fake.first_name()
context["last_name"] = fake.last_name()
context["job"] = fake.job()
context["town"] = fake.city()
context["strength"] = random.randint(3, 18)
context["agility"] = random.randint(3, 18)
context["endurance"] = random.randint(3, 18)
context["intelligence"] = random.randint(3, 18)
context["luck"] = random.randint(3, 18)
context["skill_1"] = choise_skills[0]
context["skill_2"] = choise_skills[1]
context["skill_3"] = choise_skills[3]




file_operations.render_template("charsheet.svg", "result.svg", context)