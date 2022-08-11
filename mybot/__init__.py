from .bot_dp import bot
from .handlers.default import dp
from .models import engine, Base

from sqlalchemy.orm import create_session


conn = engine.connect()
Base.metadata.create_all(bind=engine)
session = create_session(bind=engine)