from main import predict
import pickle as pkl
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

model = pkl.load(open('deployment.pkl','rb'))

input_dict = {'Avg. Session Length':30.00000, 'Time on App':12.00000, 'Time on Website':37.00000, 'Length of Membership':3.00000}
input_df = pd.DataFrame([input_dict])

def test_predict():
    assert 0 < predict(model=model, input_df=input_df)
