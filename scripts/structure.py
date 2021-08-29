from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from logger import Logger
import mlflow
from IPython.display import Image
import os
import matplotlib.pyplot as plt
class Structure:
    def __init__(self):
        self.logger = Logger().get_logger(__name__)
    
    def drawgraph(self,sm,path):
        """Draws Causal graph
    Args:
        structural_model (from_pandas_lasso): Structural model of causalnex
    Returns:
        plot_structure
    """
    
        try:
            mlflow.set_experiment('Breast cancer Causality')
            sm.remove_edges_below_threshold(0.8)
            viz = plot_structure( sm, graph_attributes={"scale": "2.0","size": "2.5"}, all_node_attributes=NODE_STYLE.WEAK, all_edge_attributes=EDGE_STYLE.WEAK)
            img = Image(viz.draw(format='png'))
            self.logger.info(f'plots causal graph successfully')
            if (not os.path.isdir('../output')):
                os.mkdir("../output")
            print("writing graph image")
            with open(f"{path}", "wb") as png:
                png.write(img.data)
            mlflow.log_artifact(path)

            return img
        
        except Exception:
            self.logger.exception('plots causal graph  failed.')
        
    def drawgraphs(self,sm,path):
        """Draws Causal graph
    Args:
        structural_model (from_pandas_lasso): Structural model of causalnex
    Returns:
        plot_structure
    """
        try:
            mlflow.set_experiment('Breast cancer Causality')
            viz = plot_structure( sm, graph_attributes={"scale": "2.0","size": "2.5"}, all_node_attributes=NODE_STYLE.WEAK, all_edge_attributes=EDGE_STYLE.WEAK)
            img = Image(viz.draw(format='png'))
            if (not os.path.isdir('../output')):
                os.mkdir("../output")
            print("writing graph image")
            with open(f"{path}", "wb") as png:
                png.write(img.data)
            fig = plt.imread(path)
            mlflow.log_artifact(fig, path)
            self.logger.info(f'plots causal graph successfully')
            return img
        
        except Exception:
            self.logger.exception('plots causal graph  failed.')