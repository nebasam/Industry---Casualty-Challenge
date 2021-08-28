from logger import Logger

class Jaccar:

    def __init__(self):
        self.logger = Logger().get_logger(__name__)

    def jaccard_similarity(self,g, h)-> int:
        """[summary]
    Args:
        receives the edge of two structures and computes similarity 
    Returns:
        similarity of two structures
    """
        try:
            i = set(g).intersection(h)
            self.logger.info(f'computes jaccard similarity.')
            return round(len(i) / (len(g) + len(h) - len(i)),3)
        except Exception:
            self.logger.exception('failed to compute jaccard similarity.')
    def jaccar_score(self,g, h)-> int:
        """[summary]
    Args:
        receives the edge of two structures and computes similarity score 
    Returns:
        score of the similarity oftwo structures
    """
        try:
            i = set(g).intersection(set(h))
            u = set(g).union(set(h))
            self.logger.info(f'computes jaccard similarity score.')
            return len(i) / float(len(u))
        except Exception:
            self.logger.exception('failed to compute jaccard similarity score.')
    


        