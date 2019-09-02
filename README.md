# Cuy Learning - Hackathon 2019 
_Predicción y optimización de tronaduras_

## Comenzando 🚀

### Pre-requisitos 📋
* Python 3.7 se recomienda usar [Anaconda](https://www.anaconda.com/distribution/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Pandas](https://pandas.pydata.org/)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Matplotlib](https://matplotlib.org/)


### Ejecutando el programa ⚙️
Selecionar el directorio del proyecto por CLI
```
cd <path proyecto>
```
Limpiar el dataset "BaseDatosHistorica_Tronadura_Hackathon.xlsx", los datos resultantes se guardan en "clean_database.xls"
```
python 0_Data_cleansing.py
```
Generar matriz de coorrelación, la matriz se almacena en "correlation_matrix.xls"
```
python 1_Correlation_analysis.py
```
Preparar los datos para entrenar, el dataset se separa en 70-30% para test y train. Los datos quedan guardados en "train_test_data.npy"
```
python 3_train_test_split.py
```
Entrenar una multilayer perceptron implementada con keras-tensorflow, el modelo entrenado se guarda como "nn_model.h5"
```
python 4_train_model.py
```
Testear el modelo con el 30% del dataset y obtener las métricas [MSE](https://en.wikipedia.org/wiki/Mean_squared_error), [R2](https://en.wikipedia.org/wiki/Coefficient_of_determination) y [MAE](https://en.wikipedia.org/wiki/Mean_absolute_error)
```
python 5_test.py
```
Transformar los datos "Datos_Entregable2_Hackathon.xlsx" en features que pueda iterpretar el modelo entrenado 
```
python feature_extractor.py
```
Utilizar el modelo entrenado con los features del entregable 2 "Datos_Entregable2_Hackathon_clean.xlsx"
```
python 6_evaluate.py
```
Las prediccion de los valores P10-P100 del entregable 2 quedan en el archivo "Datos_Entregable2_Hackathon_predicted.xlsx"