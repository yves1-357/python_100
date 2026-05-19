import pandas as pd 

# df['temperature'].sum()      # Somme
# df['temperature'].max()      # Maximum
# df['temperature'].min()      # Minimum
# df['temperature'].std()      # Écart-type
# df['temperature'].count()    # Nombre de valeurs
df = pd.read_csv('Squirrel_Data.csv')

gray_color = len(df[df["Primary Fur Color"] == "Gray"])
red_color = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_color = len(df[df["Primary Fur Color"] == "Black"])
print(gray_color)
print(red_color)
print(black_color)

data_dict = {
    "Fun color ": ["Gray", "Cinnamon", "Black"],
    "Count": ["gray_squirel", "red_squirel", "black_squirel"]}

df = pd.DataFrame(data_dict)
df.to_csv("squirel_count.csv")