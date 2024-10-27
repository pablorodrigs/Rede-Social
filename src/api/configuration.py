from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.api.routes import users

def configure_routes(app: FastAPI):
    app.include_router(users.router)

def configure_db(app: FastAPI):
    register_tortoise(
        app,
        config={
            'connections': {
                'default': 'sqlite://db.sqlite3'
            },
            'apps': {
                'models': {
                    'models': ['src.datalayer.models.user'],
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas = True,
        add_exception_handlers = True,
       

    )


