from faker import Faker


import os
import random


import file_operations


def main():
    os.makedirs("cards")
    abc = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '
        }
    fake = Faker("ru_RU")
    context = {
        "first_name": "Евсемпий",
        "last_name": "Пупидрович",
        "job": "Пархутехтор",
        "town": "Маркувиль",
        "strength": "5",
        "agility": "5",
        "endurance": "5",
        "intelligence": "5",
        "luck": "5",
        "skill_1": "Навык 1",
        "skill_2": "Навык 2",
        "skill_3": "Навык 3",
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
    for i in range(10):
        choise_skills = random.sample(skills, 3)
        skill_1 = choise_skills[0]
        skill_2 = choise_skills[1]
        skill_3 = choise_skills[2]
        for key in abc:
            skill_1 = skill_1.replace(key, abc[key])
            skill_2 = skill_2.replace(key, abc[key])
            skill_3 = skill_3.replace(key, abc[key])
        context["first_name"] = fake.first_name()
        context["last_name"] = fake.last_name()
        context["job"] = fake.job()
        context["town"] = fake.city()
        context["strength"] = random.randint(3, 18)
        context["agility"] = random.randint(3, 18)
        context["endurance"] = random.randint(3, 18)
        context["intelligence"] = random.randint(3, 18)
        context["luck"] = random.randint(3, 18)
        context["skill_1"] = skill_1
        context["skill_2"] = skill_2
        context["skill_3"] = skill_3
        i += 1
        name_card = "cards/form_" + str(i) + ".svg"

        file_operations.render_template("charsheet.svg", name_card, context)


if __name__ == '__main__':
    main()
