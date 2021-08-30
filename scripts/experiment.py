from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, plot_confusion_matrix
import seaborn as sns
from logger import Logger
import mlflow
import matplotlib.pyplot as plt
import mlflow.sklearn
import dvc.api
from preprocess import check_numeric, label_encode
import pandas as pd
import os
train_store_path = 'input/data.csv'
repo = "https://github.com/nebasam/Industry---Casualty-Challenge/"

rev = "v2"

train_store_url = dvc.api.get_url(
    path=train_store_path,
    repo=repo,
)

data = pd.read_csv("../input/data.csv")

print("DataFrame loaded")
data, non_numeric_cols = check_numeric(data)
df = label_encode(data, non_numeric_cols)
df = df[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean','diagnosis']]
y = df.diagnosis                          # M or B 
x = df.drop['diagnosis']

print("DataFrame preprocessed")


mlflow.set_experiment('Breast cancer Causality')

class Logistic:
    def __init__(self):
        mlflow.set_experiment('Breast cancer Causality')
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
    def logistic(self,df,x_train,y_train,):
        try:
            mlflow.set_experiment('Breast cancer Causality')
            mlflow.log_param('input_rows_shape', df.shape[0])
            mlflow.log_param('input_cols_shape', df.shape[1])  
            clf_rf = LogisticRegression(random_state=43)   
            clr_rf = clf_rf.fit(x_train,y_train)
            mlflow.sklearn.log_model(clr_rf, "Logistic Regression model")
            self.logger.info('train model.')
            return clr_rf
        except Exception:
            self.logger.exception('failed to train a model.')

    def accuracy(self,df, x_train,y_train,x_test,y_test,path):
        try:
            clr_rf =  self.logistic(df,x_train,y_train)
            ac = accuracy_score(y_test,clr_rf.predict(x_test))
            mlflow.log_metrics({"accuracy": ac})
            print('Accuracy is: ',ac)
            # Plot and save metrics details    
            cm = plot_confusion_matrix(clr_rf, x_test, y_test, display_labels=['Benign', 'Malignant'],cmap='magma')
            plt.title('Confusion Matrix')
            filename = f'{path}_test_confusion_matrix.png'
            plt.savefig(filename)
            # log model artifacts
            mlflow.log_artifact(filename)
            # cm = confusion_matrix(y_test,clr_rf.predict(x_test))
            # cm = sns.heatmap(cm,annot=True,fmt="d")
            self.logger.info('plot confusion matrix.')
            # filename = f'{path}'
            # plt.savefig(filename)
            return cm
        except Exception:
            self.logger.exception('failed to do confusion matrix.')
        plt.title('failed to plot Confusion Matrix')
if(__name__ == '__main__'):
    log = Logistic() 
    x_train, x_test, y_train, y_test = log.splitdata(x,y)
    path = "../output/whole_data_set"
    log.accuracy(df, x_train,y_train,x_test,y_test,path)