# def get_info(name: str, town: str, age: int) -> str:
#     """
#     :param name: input name
#     :param town: input town
#     :param age: input age
#     :return: modified string
#     """
#     result = f"This is {name} from {town} and he is {age} years old"
#     return result
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
# data = {"name": "George", "town": "Sofia", "age": 20}
# print(get_info(data['name'], data['town'], data['age']))
# print(get_info(**data))
# print(get_info(name=data['name'], town=data['town'], age=data['age']))
