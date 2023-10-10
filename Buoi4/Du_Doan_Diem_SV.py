import pandas as pd
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split


data = pd.read_csv("Student_Performance.csv")

features=data[['Hours Studied','Previous Scores','Extracurricular Activities','Sleep Hours','Sample Question Papers Practiced','Performance Index']]
target=data['Performance Index']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=(X_train.shape[1],))])


model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=50)
y_pred = model.predict(X_test)

def  mean_squared_error(y_true,y_pred):
    n = len(y_true)  # Số lượng điểm dữ liệu
    mse = sum([(y_true[i] - y_pred[i]) ** 2 for i in range(n)]) / n
    return mse


def r_squared(y_true, y_pred):

    n = len(y_true)
    sse = sum([(y_true[i] - y_pred[i]) ** 2 for i in range(n)])
    y_mean = sum(y_true) / n
    sst = sum([(y_true[i] - y_mean) ** 2 for i in range(n)])
    r_squared = 1 - (sse / sst)
    return r_squared

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r_squared(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R-squared:", r2)
