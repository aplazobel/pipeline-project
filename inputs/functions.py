import pandas as pd


def ShowCharacterData(nombre=None):
    data = pd.read_csv("character_deaths_set.csv")
    df = pd.DataFrame(data)
    return df.loc[df['name']== nombre]
    