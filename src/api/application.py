from fastapi import FastAPI
from src.api.configuration import configure_db, configure_routes

def creat_app():
  app = FastAPI()
 
  #inicializa tortoise
  configure_db(app)
  configure_routes(app)
  return app
app = creat_app()

