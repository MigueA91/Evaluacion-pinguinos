import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import joblib

# Cargar el dataset
df = sns.load_dataset("penguins").dropna()

# Separar variables
X = df.drop("species", axis=1)
y = df["species"]

# One-hot encoding para columnas categóricas
X = pd.get_dummies(X, drop_first=True)

# Escalar datos (¡manteniendo nombres de columnas!)
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Codificar variable objetivo
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Guardar clases y columnas SIN encabezados ("0")
pd.Series(encoder.classes_).to_csv("clases.csv", index=False, header=False)
pd.Series(X.columns).to_csv("columnas.csv", index=False, header=False)  # 👈 CORREGIDO AQUÍ

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Crear modelo
model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compilar y entrenar
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.1)

# Guardar modelo y scaler
model.save("modelo_penguins.keras")
joblib.dump(scaler, "scaler.pkl")

print("✅ Modelo, scaler, clases y columnas guardados exitosamente.")
