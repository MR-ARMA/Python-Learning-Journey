class Scorer:
    def __init__(self, initial_score=100):
        self.score = initial_score
    
    def decrement_score_false(self, penalty=1):
        self.score -= penalty
    
    def decrement_score_valid(self, penalty=5):
        self.score -= penalty

    def get_score(self):
        return self.score