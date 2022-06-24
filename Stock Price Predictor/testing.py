    self.pushButton.clicked.connect(self.predict) # adding function to Predict! button


    def predict(self): # predict function
        text = self.lineEdit.text()
        print()