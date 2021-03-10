from main import predict

def test_predict():
    assert 0 < predict({'Avg. Session Length':30.00000, 'Time on App':12.00000, 'Time on Website':37.00000, 'Length of Membership':3.0000})
