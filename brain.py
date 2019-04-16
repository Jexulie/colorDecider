from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, Binarizer
import json
from random import randrange
import enum
import pickle
import os

FILE_NAME = 'THINKER'

def trainer(x, y):
    model = GaussianNB()
    model.fit(x, y)
    return model

def trainLogic():
    f = open('./train-data.json')
    js = json.loads(f.read())

    data = js['data']
    target = js['target']

    f.close()
    return trainer(data, target)

def saveLogic(model):
    pickle.dump(model, open(FILE_NAME, 'wb'))

def loadLogic():
    if os.path.exists(FILE_NAME):
        return pickle.load(open(FILE_NAME, 'rb'))
    else:
        return False

def think():
    p = loadLogic()

    if p:
        return p
    else:
        nm = trainLogic()
        saveLogic(nm)
        return nm
    