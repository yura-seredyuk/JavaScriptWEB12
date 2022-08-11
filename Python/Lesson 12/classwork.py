
TEST_STRING = """Lorem Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

email@invalid
em@ail@inmalid.com
evail@valid.com
email@valid.com.ua
email@@invalid.com

127.0.1.1

https://regex101.com/
http://regex101.com/
https://www.regex101.com/
https://github.com/yura-seredyuk/JavaScriptWEB12/tree/master/Python/Lesson%2011
https://logbook.itstep.org/#/presents
"""

import re


# pattern = re.compile(r"(https?://)(www\.)?([a-zA-Z0-9-\.\w+]+)([\w/#?%-]+)")
# # matches = pattern.findall(TEST_STRING)
# matches = pattern.finditer(TEST_STRING)

# # print(matches.__next__().group(1))
# for match in matches:
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.group(4))

# pattern = re.compile(r"Lorem")
# matches = pattern.findall(TEST_STRING)
# matches = pattern.finditer(TEST_STRING)

# matches = pattern.search(TEST_STRING)
# matches = pattern.match(TEST_STRING)
# matches = re.match(r"Lorem",TEST_STRING)

# print(matches)
# pattern = re.compile(r"Lorem")

# TEST_STRING = pattern.sub('IPSUM', TEST_STRING)

# print(TEST_STRING)

# def password_validator(password:str):
#     """
#     Password validator
#     :param password: - password string
#     :return result: - validation result
#     """

#     strong_pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
#     middle_pattern = re.compile(r"^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[a-z\d@$!#%*?&]{8,}$")
#     light_pattern = re.compile(r"^(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$")


#     if strong_pattern.search(password):
#         return "Strong password!"
#     elif middle_pattern.search(password):
#         return "Good password!"
#     elif light_pattern.search(password):
#         return "Easy password!"

#     return "Incorrect password"


# print(password_validator("1111"))
# print(password_validator("qwerty1111"))
# print(password_validator("Test1235"))
# print(password_validator("!est1235"))
# print(password_validator("!eTst1235"))