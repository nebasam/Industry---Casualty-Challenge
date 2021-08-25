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
        

    def violinplots(self,data):
        try:
            plt.figure(figsize=(12, 6))
            sns.violinplot(data = data ,x = 'features' , y = "value" ,hue = 'diagnosis', split=True, inner="quart")
            plt.xticks(rotation=90)
            self.logger.info(f'violinplots successfully')
        except Exception:
            self.logger.exception('violinplots failed.')
    def boxplots(self,data):
        try: 
            plt.figure(figsize=(10,10))
            sns.boxplot(x="features", y="value", hue="diagnosis", data=data)
            plt.xticks(rotation=90)
            self.logger.info(f'boxplots successfully')
        except Exception:
            self.logger.exception('boxplots failed.')
    def boxplots(self,data):
        try: 
            plt.figure(figsize=(10,10))
            sns.boxplot(x="features", y="value", hue="diagnosis", data=data)
            plt.xticks(rotation=90)
            self.logger.info(f'boxplots successfully')
        except Exception:
            self.logger.exception('boxplots failed.')
    def jointplots(self,data,col1,col2):
        try: 
            sns.jointplot(data.loc[:,col1], data.loc[:,col2], kind="reg", color="#ce1414")
            self.logger.info(f'jointplots successfully')
        except Exception:
            self.logger.exception('jointplots failed.')
    def pairplots(self,data,col1,col2,col3):
        try: 
            sns.set(style="white")
            df = data.loc[:,[col1,col2,col3]]
            g = sns.PairGrid(df, diag_sharey=False)
            g.map_lower(sns.kdeplot, cmap="Blues_d")
            g.map_upper(plt.scatter)
            g.map_diag(sns.kdeplot, lw=3)
            self.logger.info(f'pairplots successfully')
        except Exception:
            self.logger.exception('pairplots failed.')
    def swarmplots(self,data):
        try: 
            plt.figure(figsize=(10,10))
            sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)
            plt.xticks(rotation=90)
            self.logger.info(f'swarmplots successfully')
        except Exception:
            self.logger.exception('swarmplots failed.')
    def correlation(self,data):
        try:
            f,ax = plt.subplots(figsize=(18, 18))
            sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
            self.logger.info(f'plots correlation map successfully')
        except Exception:
            self.logger.exception('plots of correlation map failed.')
        



            
    
        
        
        
       
        

     