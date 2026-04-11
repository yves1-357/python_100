import pandas as pd 

# df['temperature'].sum()      # Somme
# df['temperature'].max()      # Maximum
# df['temperature'].min()      # Minimum
# df['temperature'].std()      # Écart-type
# df['temperature'].count()    # Nombre de valeurs

df = pd.read_csv('weather_data.csv')
print(df)

# exemple sur dictionnaires
df_dict = df.to_dict()
print(df_dict)

# calculer_moyenne

average = df['temp'].mean()
print(average)

# calcule le max et sortir le row data la ou le nombre max se trouve 

maximum = df['temp'].max() 
ligne_max = df[df['temp'] == maximum]
print(ligne_max)

#get data row
data = df[df.day == "Monday"]
print(data)

#create data frame from scratch
data_dict = {
    "names" :  ["Amy", "cano", "Georgia"], 
    "scores" : ["12", "13", "24"]
                }

#pour transformer en csv
# data.to_csv("")
frame = pd.DataFrame(data_dict)
print(frame)