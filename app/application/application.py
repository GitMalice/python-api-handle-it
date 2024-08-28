class Application:
    
    def __init__(self):
        self.nom = 'Nom par défaut'
        self.version = '10.0'
        self.auteur = 'vanessa kovalsky'
        self.licence = 'GNU/GPL'

    def add(self, data):
        return 'Application ajoutée'
    
    def get_nom(self):
        return self.nom
    
    def liste(self):
        return 'Liste des applications'
