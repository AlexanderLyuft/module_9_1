    # Домашнее задание по теме "Введение в функциональное программирование"


def apply_all_func(int_list, *functions):
    results = {}
    for i in range(0, len(functions)):
        results[(functions[i]).__name__] = functions[i](int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))




