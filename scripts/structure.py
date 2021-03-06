from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from logger import Logger
from IPython.display import Image
class Structure:
    
    def __init__(self):
        self.logger = Logger().get_logger(__name__)
    
    def drawgraph (self,sm):
        """Draws Causal graph
    Args:
        structural_model (from_pandas_lasso): Structural model of causalnex
    Returns:
        plot_structure
    """
        try:
            sm.remove_edges_below_threshold(0.8)
            viz = plot_structure( sm, graph_attributes={"scale": "2.0","size": "2.5"}, all_node_attributes=NODE_STYLE.WEAK, all_edge_attributes=EDGE_STYLE.WEAK)
            img =Image(viz.draw(format='png'))
            self.logger.info(f'plots causal graph successfully')
            return img
        
        except Exception:
            self.logger.exception('plots causal graph  failed.')
        
    def drawgraphs(self,sm):
        try:
            viz = plot_structure( sm, graph_attributes={"scale": "2.0","size": "2.5"}, all_node_attributes=NODE_STYLE.WEAK, all_edge_attributes=EDGE_STYLE.WEAK)
            img =Image(viz.draw(format='png'))
            self.logger.info(f'plots causal graph successfully')
            return img
        
        except Exception:
            self.logger.exception('plots causal graph  failed.')