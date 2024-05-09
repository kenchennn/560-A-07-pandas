# link to the roster webpage https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster =  ["Okonkwo", "Ingram", "Farris"]
player = {"Last Name": roster,
         "First Name" : ["James", "Harrison", "Duwe"],
         "Height" : [68, 67, 67],
         "Weight" : [230, 225, 210]}}
data = pd.DataFrame(player)
print(data)
