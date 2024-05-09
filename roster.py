# link to the roster webpage https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster =  ["Okonkwo", "Ingram", "Farris"]
player = {"Last Name": roster}
data = pd.DataFrame(roster)
print(data)
