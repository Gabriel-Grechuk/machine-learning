import pandas as pd
import matplotlib.pyplot as plt

pumpkins = pd.read_csv("data/US-pumpkins.csv")

columns_to_select = ["Package", "Low Price", "High Price", "Date"]
pumpkins = pumpkins[pumpkins["Package"].str.contains("bushel", case=True, regex=True)]
pumpkins = pumpkins.loc[:, columns_to_select]

price = (pumpkins["Low Price"] + pumpkins["High Price"]) / 2
month = pd.DatetimeIndex(pumpkins["Date"]).month

new_pumpkins = pd.DataFrame(
    {
        "Month": month,
        "Package": pumpkins["Package"],
        "Low Price": pumpkins["Low Price"],
        "Hight Price": pumpkins["High Price"],
        "Price": price,
    }
)

new_pumpkins.loc[new_pumpkins["Package"].str.contains("1 1/9"), "Price"] = price / (
    1 + 1 / 9
)
new_pumpkins.loc[new_pumpkins["Package"].str.contains("1/2"), "Price"] = price / (1 / 2)

new_pumpkins.groupby(["Month"])["Price"].mean().plot(kind="bar")
plt.ylabel("Pumpkin Price")
plt.show()
