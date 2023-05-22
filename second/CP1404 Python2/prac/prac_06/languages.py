
from prac_06.programing_language import Car


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programing_laguages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in programing_laguages:
    if language.is_dynamic():
        print(language.name)