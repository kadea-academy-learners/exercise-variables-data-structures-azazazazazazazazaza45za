# Exercise 1.3: Variables & Data Structures
# TODO: Complète ce fichier pour passer les tests.

def main():
    # 1) Inputs (respecte exactement les prompts)
    name = input("Enter full name: ")
    city = input("Enter city: ")
    birth_year = int(input("Enter birth year: "))
    current_year = int(input("Enter current year: "))
    foods_raw = input("Enter favorite foods (comma-separated): ")

    # 2) Variables & structures de données (TODO)
    age = current_year - birth_year  # TODO: current_year - birth_year

    foods_list = []  # TODO: split foods_raw by ',' then strip each element
    foods_list = foods_raw.split(",")

    foods = []
    for x in foods_list:
        foods = x.strip()
    foods_list = foods
    
    foods_set = set(foods_list)  # TODO: set(foods_list)

    profile_dict = {'name': name, 'city': city, 'age': age, 'foods': foods_list} # TODO: {'name': name, 'city': city, 'age': age, 'foods': foods_list}
    summary_tuple = tuple([name,age,city])  # TODO: (name, age, city)

    # 3) Output (garde exactement ces libellés)
    print("--------------------")
    print(f"Name: {name}")
    print(f"City: {city}")
    print(f"Age: {age}")
    print(f"Foods (list): {foods_list}")
    print(f"Foods count: {len(foods_list)}")
    print(f"Unique foods: {len(foods_set)}")
    print(f"Profile (dict): {profile_dict}")
    print(f"Summary (tuple): {summary_tuple}")
    print("--------------------")

if __name__ == "__main__":
    main()
