from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def predict_play_probability(temperature, wind, sunshine):
    # Vstupní data
    data = [
        ["Cold", "Strong", "Cloudy", "No"],
        ["Warm", "Strong", "Cloudy", "No"],
        ["Warm", "None", "Sunny", "Yes"],
        ["Hot", "None", "Sunny", "No"],
        ["Hot", "Breeze", "Cloudy", "Yes"],
        ["Warm", "Breeze", "Sunny", "Yes"],
        ["Cold", "Breeze", "Cloudy", "No"],
        ["Cold", "None", "Sunny", "Yes"],
        ["Hot", "Strong", "Cloudy", "Yes"],
        ["Warm", "None", "Cloudy", "Yes"]
    ]

    # Vytvoření DataFrame
    df = pd.DataFrame(data, columns=["Temperature", "Wind", "Sunshine", "Play"])

    # Převod textových hodnot na čísla
    label_encoders = {}
    for column in df.columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

    # Rozdělení dat na vstupy (X) a výstup (y)
    X = df.drop("Play", axis=1)
    y = df["Play"]

    # Trénování Naive Bayes modelu
    model = MultinomialNB()
    model.fit(X, y)

    # Převod vstupních podmínek na čísla pomocí LabelEncoderů
    temperature_encoded = label_encoders["Temperature"].transform([temperature])[0]
    wind_encoded = label_encoders["Wind"].transform([wind])[0]
    sunshine_encoded = label_encoders["Sunshine"].transform([sunshine])[0]

    input_data = [[temperature_encoded, wind_encoded, sunshine_encoded]]

    # Předpověď pravděpodobnosti
    play_probability = model.predict_proba(input_data)[:, 1]  # Pravděpodobnost hraní venku (Yes)

    return play_probability[0]

# Příklad použití
temperature_input = "Warm"
wind_input = "Strong"
sunshine_input = "Sunny"

predicted_probability = predict_play_probability(temperature_input, wind_input, sunshine_input)
print(f"Predicted probability of playing outside: {predicted_probability:.2f}")
