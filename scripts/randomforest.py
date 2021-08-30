from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sns
from logger import Logger
import mlflow
import mlflow.sklearn
import dvc.api
from preprocess import check_numeric, label_encode
import pandas as pd
import matplotlib.pyplot as plt
import os

train_store_path = 'input/data.csv'
repo = "https://github.com/nebasam/Industry---Casualty-Challenge/"

version = "v1"

train_store_url = dvc.api.get_url(
    path=train_store_path,
    repo=repo,
    rev=version
)

data = pd.read_csv("../input/data.csv")

print("DataFrame loaded")
data, non_numeric_cols = check_numeric(data)
df = label_encode(data, non_numeric_cols)
y = data.diagnosis                          # M or B 
list = ['Unnamed: 32','id','diagnosis']
x = data.drop(list,axis = 1 )
x.head()

print("DataFrame preprocessed")


mlflow.set_experiment('Breast cancer Causality')


class RandomForest:
    def __init__(self):
        self.logger = Logger().get_logger(__name__)

    def splitdata(self, x,y):
        """[summary]
    Args:
        x,y : feature and target for the model
    Returns:
        splitted data
    """
        try:
            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.3, random_state=42)
            self.logger.info(f'splits data successfully.')
            return self.x_train, self.x_test, self.y_train, self.y_test
        except Exception:
            self.logger.exception('splitting data failed.')
    def randomforest(self,x_train,y_train,):
        try:
            clf_rf = RandomForestClassifier(random_state=43)      
            clr_rf = clf_rf.fit(x_train,y_train)
            self.logger.exception('train model.')
            return clr_rf
        except Exception:
            self.logger.exception('failed to train a model.')

    def accuracy(self,x_train,y_train,x_test,y_test):
        try:
            clr_rf =  self.randomforest(x_train,y_train)
            ac = accuracy_score(y_test,clr_rf.predict(x_test))
            print('Accuracy is: ',ac)
            cm = confusion_matrix(y_test,clr_rf.predict(x_test))
            sns.heatmap(cm,annot=True,fmt="d")
            self.logger.exception('plot confusion matrix.')
        except Exception:
            self.logger.exception('failed to do confusion matrix.')
if(__name__ == '__main__'):
    
    polygon = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
    Fetch_data = FetchData(polygon=polygon, region="IA_FullState", epsg="4326") 
    print(Fetch_data.get_data())    