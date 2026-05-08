import datetime

name = input("What's Your Name? ")
year_of_birth = int(input("What's Your Year Of Birth? "))

age = datetime.datetime.now().year - year_of_birth

print(f"Hello {name}, you are {age} years old" )