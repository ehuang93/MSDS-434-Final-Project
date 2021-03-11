from main import predict
import pickle as pkl
from sklearn.linear_model

model = pkl.load(open('deployment.pkl','rb'))

def test_predict():
    assert 0 < predict(model=model, input_df={'Avg. Session Length':30.00000, 'Time on App':12.00000, 'Time on Website':37.00000, 'Length of Membership':3.0000})
