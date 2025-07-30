import re


#
# text = "Hello, world! This test string."
#
# pattern = r"world"
#
# result = re.search(pattern, text)
#
# print(result.group(0))
# print(result.start())
# print(result.end())
# print(text[result.start(): result.end()])

# print(text)



#---------------
# text2 = "Номер телефону: 123-456-7890 або 987-654-3210."
# # pattern = r"(\d{3})-(\d{3})-(\d{4})"
# pattern = r"\d{3}-\d{3}-\d{4}"
# result = re.search(pattern, text2)
#
# print(result.group(0))
#
# result = re.findall(pattern, text2)
# for phone_num in result:
#     print(phone_num.split("-"))


#---------------

# text4 = "Мова програмування: Python."
# text3 = "Python - чудова мова програмування."
#
# pattern = r"Python"
# result = re.match(pattern, text3)
#
#
# if result:
#     print(result.group(0))
# else:
#     print("Not found")



# ---------------

# text5 = "Email: test@example.com, support@domain.org, info@mail.net."
#
# pattern = r"\b[A-Za-z0-9._-]+@\w+\.[a-z]{2,3}\b"
# # \w  еквівалентно [a-zA-Z0-9]
#
# result = re.findall(pattern, text5)
# print(result)


# ---------------
# text7 = "Ціни: $10.50, $25.00, $5.99."
# pattern = r"(\$\d+\.\d{2})"
# result = re.finditer(pattern, text7)
#
# for i in result:
#     print(i.group(0))


# ---------------

# text8 = "Chiko Python"
#
#
# pattern = r"Python"
# replacement = "HTML"
#
# # result = re.sub(pattern,replacement, text8)
# result = re.sub(pattern,replacement, text8, count=1)
# print(f"Original: {text8}")
# print(f"After replacement: {result}")

# ---------------

# long_text = "Це довгий текст з багатьма словами. Слово, слово, слово. Шукаємо слово."
# compiled_pattern = re.compile(r"\bслово\b", re.IGNORECASE)
#
# result = compiled_pattern.findall(long_text)
# print(result)

# ---------------
