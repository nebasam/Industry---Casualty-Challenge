from IPython.display import Image
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from logger import Logger
class Structure:
    
    def __init__(self):
        self.logger = Logger().get_logger(__name__)
    
    def drawgraph (self,sm):
        try:
            sm.remove_edges_below_threshold(0.8)
            viz = plot_structure( sm, graph_attributes={"scale": "2.0","size": "2.5"}, all_node_attributes=NODE_STYLE.WEAK, all_edge_attributes=EDGE_STYLE.WEAK)
            self.logger.info(f'plots causal graph successfully')
            Image(viz.draw(format='png'))
            
        
        except Exception:
            self.logger.exception('plots causal graph  failed.')
        
