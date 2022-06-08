my_list = []
for i in range(1, 1001, 2):
    my_list.append(i**3)

def sum_list_1(dataset: list) -> int:
    total_sum = 0
    for number in dataset:
        init_number = number
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10
            number //= 10
        if digit_sum % 7 == 0:
            total_sum += init_number

    return total_sum

result_1 = sum_list_1(my_list)
print(result_1)

def sum_list_2(dataset: list) -> int:
    total_sum = 0
    for number in dataset:
        number += 17
        init_number = number
        digit_sum = 0
        while number > 0:
            digit_sum += (number % 10)
            number //= 10
        if digit_sum % 7 == 0:
            total_sum += init_number

    return total_sum

result_2 = sum_list_2(my_list)
print(result_2)

# Второй вариан решения задачи, какой из вариантов лучше и понятнее?
# my_list = []
# for num in range(1, 1001, 2):
#     my_list.append(num ** 3)
# # a
# final_sum = 0
# for num in my_list:
#     check_sum = 0
#     for check_num in str(num):
#         check_sum += int(check_num)
#     if check_sum % 7 == 0:
#         final_sum += num
# print(final_sum)
#
# # b and c
# final_sum = 0
# for num in my_list:
#     num += 17
#     check_sum = 0
#     for check_num in str(num):
#         check_sum += int(check_num)
#         if check_sum % 7 == 0:
#             final_sum += num
# print(final_sum)