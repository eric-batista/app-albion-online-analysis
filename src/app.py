import fastapi
from devtools.exceptions.handlers import add_exception_handlers
from devtools.utils.api import EventTypes, on_event
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from src import __version__
from src.core import database, settings
from src.routes import router


def get_application():
    origins = [
        "http://localhost",
        "http://localhost:8080",
        "https://eric-batista.github.com",
    ]

    application = fastapi.FastAPI(
        default_response_class=ORJSONResponse,
        version=__version__,
        docs_url=f"{settings.BASE_PATH}/docs",
        redoc_url=f"{settings.BASE_PATH}/redoc",
        openapi_url=f"{settings.BASE_PATH}/openapi.json",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    on_event(application, EventTypes.STARTUP, database.initialize_database())

    add_exception_handlers(application)

    application.include_router(router, prefix=f"{settings.BASE_PATH}")

    return application


app = get_application()
