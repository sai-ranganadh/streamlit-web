import streamlit as st
import joblib

st.title('House price prediction in California')
st.markdown(
    """
    <style>
   
.stApp {
            display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: seashell;
    height: 90vh; /* Makes sure the content takes the full height of the viewport */
        }
.my-button{
    color:saddlebrown;
    width: 100px;
    height: 30px;
    font-size: 16px;
}
    </style>
    """,unsafe_allow_html=True
)



bedrooms = st.number_input("Enter no. of bedrooms: ",min_value=0,step=1)
totalrooms = st.number_input("Enter total no. of rooms: ",step=1,min_value=1)
age = st.number_input("Enter age of the house: ",step=1)
ocean_proximity = st.radio('Choose Ocean Proximity',('INLAND','<1H OCEAN','NEAR OCEAN','NEAR BAY','ISLAND'))
ocean_proximity_map = {'INLAND':0,'<1H OCEAN':1,'NEAR OCEAN':2,'NEAR BAY':3,'ISLAND':4}
ocean_proximity = ocean_proximity_map[ocean_proximity]

longitude = -118.49
latittude = 34.26
population = 1166
households = 409
income = 3.53


if st.button('Predict price',key="my-button"):
    households_rooms = totalrooms/households
    bedroom_ratio = bedrooms/totalrooms
    features = [longitude, latittude, age, totalrooms, bedrooms, population, households, income, ocean_proximity, households_rooms, bedroom_ratio]
    model = joblib.load('linear_regression_model.pkl')
    predicted_price = round(model.predict([features])[0],2)
    val = f"Predicted Price: {predicted_price} $"
    st.write(val)