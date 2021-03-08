from app import app


#Importando rotas
from app.routes import *

#Importando models
from app.models import temperamento
from app.models import raca

if __name__ == "__main__":
    app.run()