import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import streamlit as st

# Load the dataset
df = pd.read_excel("cars.xls")
x= df.drop("Price", axis = 1)
y = df[["Price"]]

x_train,x_test,y_train,y_test = train_test_split(x, y,random_state=42, test_size=.2)

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(),["Mileage","Cylinder","Liter","Doors"]),
        ("cat", OneHotEncoder(),["Make","Model","Trim","Type"])
    ]
)
model = LinearRegression()

pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("regressor", model)])

pipeline.fit(x_train,y_train)

pred = pipeline.predict(x_test)

rmse = mean_squared_error(pred,y_test)**.5
r2=r2_score(pred,y_test)

def price_pred(make,model,trim,mileage,car_type,cylinder,liter,doors,cruise,sound,leather):
    input_data = pd.DataFrame({
        "Make": [make],
        "Model": [model],
        "Trim": [trim],
        "Mileage": [mileage],
        "Type": [car_type],
        "Cylinder": [cylinder],
        "Liter": [liter],
        "Doors": [doors],
        "Cruise": [cruise],
        "Sound": [sound],
        "Leather": [leather]
    })

    prediction = pipeline.predict(input_data)[0]
    return prediction

def main():
    st.title("MLOps Car Price Prediction :red_car:")
    st.write("Enter Car Details to predict the price")

    make = st.selectbox("Make", df["Make"].unique())
    model = st.selectbox("Model", df[df["Make"]==make]["Model"].unique())
    trim = st.selectbox("Trim", df[(df["Make"]==make) & (df["Model"] == model)]["Trim"].unique())
    mileage = st.number_input("Mileage:",200,60000)
    car_type = st.selectbox("Type", df["Type"].unique())
    cylinder = st.number_input("Cylinder:",4,8)
    liter = st.number_input("Liter:",1,6)
    doors = st.selectbox("Doors:",df["Doors"].unique())
    cruise = st.radio("Cruise Control:",[0,1])
    sound = st.radio("Sound:",[0,1])
    leather = st.radio("Leather:",[0,1])

    if st.button("Predict"):
        price = price_pred(make,model,trim,mileage,car_type,cylinder,liter,doors,cruise,sound,leather)
        price = float(price)
        st.write(f"The predicted price is: $ {price:.2f}")

if __name__=="__main__":
    main()