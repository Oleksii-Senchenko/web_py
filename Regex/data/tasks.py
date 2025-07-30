import re

# task_text_1 = "Я вивчаю python. Python - це круто!"
#
#
# # 1. pattern = r".ython"
# # 2. pattern = r"python|Python"
# # 3. pattern = r"[Pp]ython"
#
# result = re.findall(pattern, task_text_1)
# print(result)

# ---------------
# task_text_2_1 = "https://www.google.com"
# task_text_2_2 = "www.google.com"
#
#
# pattern = r"https"
# result = re.match(pattern, task_text_2_1)
# # result = re.match(pattern, task_text_2_2)
#
#
# if result:
#     print(result.group(0))
# else:
#     print("Not found")


# ---------------

# task_text_3 = "Температура: 25.5 градусів. Тиск: 1012.3 гПа. Швидкість: -1.2 м/с."
#
# # pattern = r"-?\d+\.\d*"
# pattern = r"-?\d+\.\d*\s\w+\b"
# print(re.findall(pattern, task_text_3))

# ---------------

# task_text_4 = "Контакти: alice@example.org, bob.smith@mail.com."
#
# pattern = r"\b([A-Za-z0-9._-]+)@([A-Za-z.]{1,})"
#
#
#
# result = re.finditer(pattern, task_text_4)
#
# for match_obj in result:
#     print(f"Name: {match_obj.group(1)}\nDomen: {match_obj.group(2)}")
#     print(20 * "-")

# ---------------


# task_text_5 = "Мій cat любить спати. У мене є ще один Cat. А де мій Cat?"
#
#
# pattern = r"Cat|cat"
# replacement = "dog"
#
# result = re.sub(pattern,replacement, task_text_5)
# print(f"Original: {task_text_5}")
# print(f"After replacement: {result}")
#
# for i in task_text_5:
#     result = re.findall(pattern, task_text_5)


# ---------------


task_text_5 = "Мій кіт любить спати. У мене є ще один Кіт. А де мій кіт?"

changes_to_do = [(r"Кіт", "Пес"), (r"кіт", "пес"), (r"любить", "ненавидить")]


result = task_text_5[:]
for pattern, replacement in changes_to_do:
    result = re.sub(pattern, replacement, result)

print(result)

