class Kola:
    def __init__(self,id,marka,model,godina):
        self.id = id
        self.marka = marka
        self.model = model
        self.godina = godina


    def __str__(self):
        return f"{self.marka} {self.model}"