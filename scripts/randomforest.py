from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sns
from logger import Logger
import mlflow


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
    def randomforest(self,df,x_train,y_train,):
        mlflow.set_experiment('Breast cancer Causality')
        mlflow.log_param('input_rows_shape', df.shape[0])
        mlflow.log_param('input_cols_shape', df.shape[1])
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
        