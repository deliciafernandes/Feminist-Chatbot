import pandas
import random

# Data formatting
stakeholders = pandas.read_csv("data/stakeholders.csv")
purposes = pandas.read_csv("data/purposes.csv")

stakeholders_list = stakeholders["Stackholders"].to_list()
purposes_list = purposes["Purposes"].to_list()

# Result generation
choice = int(input("How many options would you like? "))
print()
while choice > 0:
    stakeholder = random.choice(stakeholders_list)
    purpose = random.choice(purposes_list)

    result = "How could a chatbot help " + stakeholder + " " + purpose + "?"
    print(result)

    choice -= 1
