import matplotlib.pyplot as plt
import seaborn as sns
from logger import Logger

class Exploration:

    def __init__(self):
        self.logger = Logger().get_logger(__name__)

    def countplots(self, col1, text1, text2):
        try:
            ax = sns.countplot(col1,label = 'count')       
            B, M = col1.value_counts()
            print(text1,B)
            print(text2,M)
            self.logger.info(f'countplots successfully.')
        except Exception:
            self.logger.exception('countplots failed.')
        

    