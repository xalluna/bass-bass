from src.image_processor import ImageProcessor

sety: set[str]= {"foo", "bar", 'fizz', 'buzz'}
listy: list[list[int, str]] = [[1, "a"], [2, 'b'], [3, "c"], [4, "d"]]
list2: list[int] = [5, 6, 7, 8, 1]

# print([*zip(sety, listy, list2)])
# print([item for item in listy if item[0] not in list2])

# print([item[0] for item in listy])

# print([[item[0] for item in listy],[item[1] for item in listy]])
[num for num in [1, 5] if num in list2]
print('okay :)')
