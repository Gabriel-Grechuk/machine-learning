import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# from imblearn.over_sampling import SMOTE

df = pd.read_csv("data/cuisines.csv")

thai_df = df[(df.cuisine == "thai")]
japanese_df = df[(df.cuisine == "japanese")]
chinese_df = df[(df.cuisine == "chinese")]
indian_df = df[(df.cuisine == "idian")]
korean_df = df[(df.cuisine == "korean")]

print(f"thai df: {thai_df.shape}")
print(f"df: {thai_df.shape}")
print(f"japanese df: {japanese_df.shape}")
print(f"chinese df: {chinese_df.shape}")
print(f"indian df: {indian_df.shape}")
print(f"korean df: {korean_df.shape}")


def create_ingredient_df(df):
    ingredient_df = df.T.drop(["cuisine", "Unnamed: 0"]).sum(axis=1).to_frame("value")
    ingredient_df = ingredient_df[(ingredient_df.T != 0).any()]
    ingredient_df = ingredient_df.sort_values(
        by="value", ascending=False, inplace=False
    )

    return ingredient_df


def plot_data(frame):
    frame.head(10).plot.barh()
    plt.show()


thai_ingredient_df = create_ingredient_df(thai_df)
japanese_ingredientes_df = create_ingredient_df(japanese_df)
chinese_ingredients_df = create_ingredient_df(chinese_df)
indian_ingredient_df = create_ingredient_df(indian_df)
korean_ingredients_df = create_ingredient_df(korean_df)


# plot_data(thai_ingredient_df)
# plot_data(thai_ingredient_df)
# plot_data(japanese_ingredientes_df)
# plot_data(chinese_ingredients_df)
# plot_data(indian_ingredient_df)
# plot_data(korean_ingredients_df)

# thai_ingredient_df.head(10).plot.barh()
# plt.show()
