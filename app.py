from pywebio.input import *
from pywebio.output import *

import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
model = pickle.load(open('regression_rf.pkl', 'rb'))


standard_to = StandardScaler()

def predict():
    Year = input("Enter the Model Year：", type=NUMBER)
    Year = 2021 - Year
    Present_Price = input("Enter the Present Price(in LAKHS)", type=FLOAT)
    Kms_Driven = input("Enter the distance it has travelled(in KMS)：", type=FLOAT)
    Kms_Driven2 = np.log(Kms_Driven)
    Owner = input("Enter the number of owners who have previously owned it(0 or 1 or 2 or 3)", type=NUMBER)
    Fuel_Type = select('What is the Fuel Type', ['Petrol', 'Diesel','CNG'])
    if (Fuel_Type == 'Petrol'):
        Fuel_Type = 239

    elif (Fuel_Type == 'Diesel'):
        Fuel_Type = 60

    else:
        Fuel_Type = 2
    Seller_Type = select('Are you a dealer or an individual', ['Dealer', 'Individual'])
    if (Seller_Type == 'Individual'):
        Seller_Type = 106

    else:
        Seller_Type = 195
    Transmission = select('Transmission Type', ['Manual Car', 'Automatic Car'])
    if (Transmission == 'Manual Car'):
        Transmission = 261
    else:
        Transmission = 40

    prediction = model.predict([[Present_Price, Kms_Driven2, Fuel_Type, Seller_Type, Transmission, Owner, Year]])
    output = round(prediction[0], 2)

    if output < 0:
        put_text("Sorry You can't sell this Car")

    else:
        put_text('You can sell this Car at price:',output)


if __name__=="__main__":
    predict()

