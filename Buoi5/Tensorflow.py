from tensorflow import keras
import pandas as pd



data=pd.read_csv('Student_Performance.csv')

X=data.drop('Performance Index',axis=1)
Y=data['Performance Index']

##Xay dung mo hinh
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1) ])
model.compile(optimizer='adam', loss='mean_squared_error')


#Huan luyen mo hinh voi so lan hhuan luyen la 100
model.fit(X, Y, epochs=100, batch_size=32)

#data thu
testdata = pd.DataFrame({
    'Hours Studied': [6, 4, 7],
    'Previous Scores': [88, 75, 92],
    'Extracurricular Activities': [1, 0, 1],
    'Sleep Hours': [7, 6, 8],
    'Sample Question Papers Practiced': [3, 5, 2]
})
#in ket qua cuar testdata
predictions = model.predict(testdata)
print(predictions)
##Ket qua thu duoc
# [[77.29513]
# [57.75451]
# [84.51058]]