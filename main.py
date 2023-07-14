# arr = ["test!", "test2", "testR"]
# for item in arr:
#     print(item)
# print(f"_______{arr}_______")

# count = 0
# while count < len(arr):
#     print(arr[count])
#     count += 1

# for i in range(1,3):
#     print(i)
#     print(arr[i])

# test = [ x for x in arr if x == "test!" ]
# test_two = []
# for i in arr:
#     if i == "test2":
#         test_two.append(i)
# print(test)
# print(test_two)

# number = []
# for i in range(1, 101, 1):
#     number.append(i)
# print(number)

# even = []
# odd = []
# for i in number:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# sort
# arr = [4, 56, 2, 6, 3, 89]
# arr_two = arr.copy()
# flag = True
# while flag:
#     flag = False
#     status_chack = True
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             temp = arr[i]
#             arr[i] = arr[i + 1]
#             arr[i + 1] = temp

#     for item in range(len(arr) - 1):
#         if arr[item] > arr[item + 1] and flag == False:
#             flag = True

# print(arr)


# sort mrthods
# new_val = sorted(arr_two)
# print(sorted(arr_two))
# arr_two.sort()

# arr_two.sort()
# print(arr_two)
# new_val_desc = sorted(arr_two, reverse=True)'

# str_arr = ["Jonny", "Anna", "Ketty", "Zak"]
# ________ A-Z _________
# sort_str_arr = sorted(str_arr)
# print(sort_str_arr)
#_________ Z-A _________
# sort_str_arr_desc = sorted(str_arr, reverse=True)
# print(sort_str_arr_desc)
import json
str_title = []
with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

products.sort(key=lambda x: x["price"])
sorted_product = sorted(products, key=lambda product: product["price"], reverse=True)
print(sorted_product)
#     for item in products:
#         str_title.append(item["title"])
#         sort_str_title = sorted(str_title)
#         sort_str_title = sort_str_title.pop(0)
#         sort_str_title_desc = sorted(str_title, reverse=True)
# print(sort_str_title)
# print(sort_str_title_desc)
# with open("products.json", "w", encoding="utf-8") as file:
#     json.dump(productds, file)
        