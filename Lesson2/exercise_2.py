import collections

persons = [
    {
        "name": "Anna",
        "age": 25,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Dima",
        "age": "19",
        "gender": "male"
    }, {
        "name": "Makar",
        "age": "10",
        "gender": "male"
    }, {
        "name": "Lena",
        "age": "40",
        "gender": "female"
    }, {
        "name": "Fred",
        "age": "42",
        "gender": "male"
    }, {
        "name": "Agata",
        "age": "17",
        "gender": "female"
    }, {
        "name": "Igor",
        "age": "15",
        "gender": "male"
    }, {
        "name": "Kate",
        "age": "19",
        "gender": "female"
    }, {
        "name": "Alina",
        "age": "37",
        "gender": "female"
    }, {
        "name": "Dima",
        "age": "12",
        "gender": "male"
    }, {
        "name": "Floyd",
        "age": "60",
        "gender": "male"
    }, {
        "name": "Agata",
        "age": "30",
        "gender": "female"
    }, {
        "name": "Dima",
        "age": "40",
        "gender": "male"
    }
    , {
        "name": "Makar",
        "age": "19",
        "gender": "male"
    }
]

# Колличество всех людей
number_of_all_people = len(persons)
print(f"Number of all people = {number_of_all_people}")

# Сколько мужчин, сколько женщин, сколько совершеннолетних
count_male = 0
count_female = 0
numbers_of_adults = 0
# Первый способ
for person in persons:
    if person.get("gender") == "male":
        count_male += 1
    elif person.get("gender") == "female":
        count_female += 1
    if int(person.get("age")) >= 18:
        numbers_of_adults += 1

print(f"Numbers of men {count_male} and women {count_female}")
print(f"Numbers of adults {numbers_of_adults}")
# Второй способ
male_female = [person.get("gender") for person in persons]
count_male = male_female.count("male")
count_female = male_female.count("female")

print(f"Numbers of men {count_male} and women {count_female}")
# Список всех имен
names = [person.get("name") for person in persons]
print(f"Names : {names}")
# Отсортированный список всх возрастов без повторений
ages = list(set([int(person.get("age")) for person in persons]))
ages.sort()
print(f"Ages without repeat : {ages}")
# 3 самых встречающихся имени
counter = collections.Counter(names)
print(f"Names and their frequencies : {counter}")
name_times_tuple = [(name, times) for name, times in counter.items()]


def key(item):
    return item[1]


name_times_tuple.sort(key=key, reverse=True)
top_3 = [name for name, times in name_times_tuple[0:3]]
print(f"The three most common names : {top_3}")
# Вывести все имена мужчин старше 35, имя которых начинается с F
names_male_greater_than_35_f = [person.get("name") for person in persons if
                           int(person.get("age")) > 35 and person.get("name").startswith('F')]
print(f"Names of men over 35 and names beginning with the letter 'F' : {names_male_greater_than_35_f}")
