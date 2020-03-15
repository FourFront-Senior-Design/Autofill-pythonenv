class Word:
    text = ""
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    def __init__(self, string, X1, Y1, X2, Y2):
        self.text = string
        self.x1 = X1
        self.y1 = Y1
        self.x2 = X2
        self.y2 = Y2
        
    def __str__(self):
        return self.text + "\n\tx1: " + str(self.x1) + "\n\ty1: " + str(self.y1) + "\n\tx2: " + str(self.x2) + "\n\ty2: " + str(self.y2)
        
    def getText(self):
        return self.text
        
    def getBoundingBox(self):
        return self.x1, self.y1, self.x2, self.y2