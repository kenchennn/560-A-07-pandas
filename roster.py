# link to the roster webpage https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name" : ["Okonkwo", "Ingram", "Duwe"],
            "First Name" : ["James", "Harrison", "Farris"],
            "Height" : [68, 67, 67],
            "Weight" : [230, 225, 210]}

data = pd.DataFrame(player)

#bmi
data["bmi"] = ((data["Weight"])/(data["Height"])**2) * 703

print(data)

data.to_csv("bmi.csv")
